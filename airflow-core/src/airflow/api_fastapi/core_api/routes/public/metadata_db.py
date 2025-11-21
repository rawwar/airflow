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
from __future__ import annotations

from typing import Annotated

from fastapi import Depends, HTTPException, Query, status
from sqlalchemy.exc import NoSuchTableError

from airflow.api_fastapi.common.db.common import SessionDep
from airflow.api_fastapi.common.db.metadata_db import get_metadata_db_stats, get_schema_indexes
from airflow.api_fastapi.common.router import AirflowRouter
from airflow.api_fastapi.core_api.datamodels.metadata_db import (
    MetadataDbSchemaIndexesResponse,
    MetadataDbStatsResponse,
)
from airflow.api_fastapi.core_api.openapi.exceptions import create_openapi_http_exception_doc
from airflow.api_fastapi.core_api.security import requires_metadata_db_access


metadata_db_router = AirflowRouter(prefix="/metadataDB", tags=["MetadataDB"])


@metadata_db_router.get(
    "/stats",
    dependencies=[Depends(requires_metadata_db_access())],
    responses=create_openapi_http_exception_doc([status.HTTP_500_INTERNAL_SERVER_ERROR]),
)
def get_global_stats(
    session: SessionDep,
    include_row_count: Annotated[bool, Query()] = False,
) -> MetadataDbStatsResponse:
    """
    Get statistics for all Airflow metadata tables.

    By default returns table sizes only. Set include_row_count=true to also get row counts
    (expensive operation requiring full table scans).
    """
    try:
        return get_metadata_db_stats(session, table_name=None, include_row_count=include_row_count)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve metadata statistics",
        )


@metadata_db_router.get(
    "/stats/{table_name}",
    dependencies=[Depends(requires_metadata_db_access())],
    responses=create_openapi_http_exception_doc(
        [status.HTTP_404_NOT_FOUND, status.HTTP_500_INTERNAL_SERVER_ERROR]
    ),
)
def get_table_stats(
    table_name: str,
    session: SessionDep,
    include_row_count: Annotated[bool, Query()] = False,
) -> MetadataDbStatsResponse:
    """
    Get statistics for a specific Airflow metadata table.

    By default returns table size only. Set include_row_count=true to also get row count
    (expensive operation requiring full table scan).
    """
    try:
        return get_metadata_db_stats(session, table_name=table_name, include_row_count=include_row_count)
    except NoSuchTableError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Table '{table_name}' not found in Airflow metadata schema",
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve table statistics",
        )


@metadata_db_router.get(
    "/indexes",
    dependencies=[Depends(requires_metadata_db_access())],
    responses=create_openapi_http_exception_doc([status.HTTP_500_INTERNAL_SERVER_ERROR]),
)
def get_schema_indexes_endpoint(
    session: SessionDep,
) -> list[MetadataDbSchemaIndexesResponse]:
    """
    Get index information for all Airflow metadata tables.

    Returns a list of tables with their associated indexes, including column names,
    uniqueness constraints, and dialect-specific options.
    """
    try:
        return get_schema_indexes(session)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve schema indexes",
        )


@metadata_db_router.get(
    "/indexes/{table_name}",
    dependencies=[Depends(requires_metadata_db_access())],
)
def get_table_indexes(table_name: str):
    """Get index information for a specific Airflow metadata table."""
    raise NotImplementedError
