# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
r"""
Metadata database utilities for Airflow REST API.

:meta private:
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import func, inspect, select, text

from airflow.models.base import Base

if TYPE_CHECKING:
    from sqlalchemy.orm import Session
    from sqlalchemy.schema import Table

    from airflow.api_fastapi.core_api.datamodels.metadata_db import (
        MetadataDbIndexInfo,
        MetadataDbSchemaIndexesResponse,
        MetadataDbStatsResponse,
        MetadataDbTableStatsResponse,
    )


def _bytes_to_mb(size_bytes: int | None) -> float | None:
    """Convert bytes to megabytes with 4 decimal places."""
    if size_bytes is None:
        return None
    return round(size_bytes / (1024 * 1024), 4)


def _get_table_row_count(session: Session, table: Table) -> int | None:
    """Get row count for a specific table using SQLAlchemy."""
    try:
        count_stmt = select(func.count()).select_from(table)
        return session.execute(count_stmt).scalar() or 0
    except Exception:
        return None


def _get_table_size_bytes(session: Session, table_name: str) -> int | None:
    """Get table size in bytes using dialect-specific queries."""
    dialect = session.get_bind().dialect.name

    try:
        if dialect == "postgresql":
            query = text("SELECT pg_total_relation_size(:table_name)")
            result = session.execute(query, {"table_name": table_name}).scalar()
            return result
        if dialect in ("mysql", "mariadb"):
            query = text(
                """
                SELECT (data_length + index_length)
                FROM information_schema.tables
                WHERE table_schema = DATABASE() AND table_name = :table_name
                """
            )
            result = session.execute(query, {"table_name": table_name}).scalar()
            return result
        # SQLite and other dialects don't have a reliable way to get table size
        return None
    except Exception:
        return None


def _build_table_stats(
    session: Session, table_name: str, table: Table, include_row_count: bool
) -> MetadataDbTableStatsResponse:
    """Build statistics for a single table."""
    from airflow.api_fastapi.core_api.datamodels.metadata_db import MetadataDbTableStatsResponse

    table_size_bytes = _get_table_size_bytes(session, table_name)
    row_count = _get_table_row_count(session, table) if include_row_count else None

    return MetadataDbTableStatsResponse(
        table_name=table_name,
        table_size_mb=_bytes_to_mb(table_size_bytes),
        row_count=row_count,
    )


def _get_single_table_stats(
    session: Session, table_name: str, include_row_count: bool
) -> MetadataDbStatsResponse:
    """Get statistics for a specific table."""
    from sqlalchemy.exc import NoSuchTableError

    from airflow.api_fastapi.core_api.datamodels.metadata_db import MetadataDbStatsResponse

    airflow_tables = Base.metadata.tables
    if table_name not in airflow_tables:
        raise NoSuchTableError(f"Table '{table_name}' not found in Airflow metadata")

    table = airflow_tables[table_name]
    table_stats = _build_table_stats(session, table_name, table, include_row_count)

    return MetadataDbStatsResponse(
        tables=[table_stats],
        total_tables=1,
    )


def _get_all_tables_stats(session: Session, include_row_count: bool) -> MetadataDbStatsResponse:
    """Get statistics for all Airflow metadata tables."""
    from airflow.api_fastapi.core_api.datamodels.metadata_db import MetadataDbStatsResponse

    airflow_tables = Base.metadata.tables
    table_stats_list = [
        _build_table_stats(session, tbl_name, table, include_row_count)
        for tbl_name, table in airflow_tables.items()
    ]

    return MetadataDbStatsResponse(
        tables=table_stats_list,
        total_tables=len(table_stats_list),
    )


def get_metadata_db_stats(
    session: Session, table_name: str | None = None, include_row_count: bool = False
) -> MetadataDbStatsResponse:
    """
    Get database statistics for Airflow metadata tables.

    If table_name is provided, returns statistics for that specific table only.
    Otherwise, returns global statistics across all Airflow metadata tables.

    By default, only table sizes are returned. Row counts can be included by setting
    include_row_count=True (this is more expensive as it requires full table scans).

    :param session: Database session
    :param table_name: Optional table name to get stats for a specific table
    :param include_row_count: Whether to include row counts (default False)
    :return: MetadataDbStatsResponse
    """
    if table_name is not None:
        return _get_single_table_stats(session, table_name, include_row_count)

    return _get_all_tables_stats(session, include_row_count)


def _get_index_size_bytes(session: Session, table_name: str, index_name: str) -> int | None:
    """Get index size in bytes using dialect-specific queries."""
    dialect = session.get_bind().dialect.name

    try:
        if dialect == "postgresql":
            query = text("SELECT pg_relation_size(:index_name)")
            result = session.execute(query, {"index_name": index_name}).scalar()
            return result
        if dialect in ("mysql", "mariadb"):
            query = text(
                """
                SELECT index_length
                FROM information_schema.tables
                WHERE table_schema = DATABASE() AND table_name = :table_name
                """
            )
            result = session.execute(query, {"table_name": table_name}).scalar()
            return result
        # SQLite and other dialects don't have a reliable way to get index size
        return None
    except Exception:
        return None


def _build_index_info(session: Session, table_name: str, index_data: dict) -> MetadataDbIndexInfo:
    """Build index info with name and size."""
    from airflow.api_fastapi.core_api.datamodels.metadata_db import MetadataDbIndexInfo

    index_name = index_data["name"]
    size_bytes = _get_index_size_bytes(session, table_name, index_name)

    return MetadataDbIndexInfo(
        name=index_name,
        size_mb=_bytes_to_mb(size_bytes),
    )


def get_schema_indexes(session: Session) -> list[MetadataDbSchemaIndexesResponse]:
    """
    Get index information for all Airflow metadata tables.

    :param session: Database session
    :return: List of MetadataDbSchemaIndexesResponse, one per table
    """
    from airflow.api_fastapi.core_api.datamodels.metadata_db import MetadataDbSchemaIndexesResponse

    inspector = inspect(session.get_bind())
    airflow_tables = Base.metadata.tables
    results = []

    for table_name in sorted(airflow_tables.keys()):
        try:
            indexes = inspector.get_indexes(table_name)
            index_info_list = [_build_index_info(session, table_name, idx) for idx in indexes]

            results.append(
                MetadataDbSchemaIndexesResponse(
                    table_name=table_name,
                    indexes=index_info_list,
                )
            )
        except Exception:
            # If we can't get indexes for a table, skip it
            continue

    return results


def get_table_indexes(session: Session, table_name: str) -> MetadataDbSchemaIndexesResponse:
    """
    Get index information for a specific Airflow metadata table.

    :param session: Database session
    :param table_name: Name of the table
    :return: MetadataDbSchemaIndexesResponse
    :raises NoSuchTableError: If the table doesn't exist in Airflow metadata
    """
    from sqlalchemy.exc import NoSuchTableError

    from airflow.api_fastapi.core_api.datamodels.metadata_db import MetadataDbSchemaIndexesResponse

    airflow_tables = Base.metadata.tables
    if table_name not in airflow_tables:
        raise NoSuchTableError(f"Table '{table_name}' not found in Airflow metadata")

    inspector = inspect(session.get_bind())
    indexes = inspector.get_indexes(table_name)
    index_info_list = [_build_index_info(session, table_name, idx) for idx in indexes]

    return MetadataDbSchemaIndexesResponse(
        table_name=table_name,
        indexes=index_info_list,
    )
