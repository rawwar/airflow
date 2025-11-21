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

from pydantic import BaseModel


class MetadataDbTableStatsResponse(BaseModel):
    """Response model for individual table metadata statistics."""

    table_name: str
    table_size_mb: float | None
    row_count: int | None = None


class MetadataDbStatsResponse(BaseModel):
    """Response model for global metadata DB statistics."""

    tables: list[MetadataDbTableStatsResponse]
    total_tables: int


class MetadataDbIndexInfo(BaseModel):
    """Response model for individual index metadata."""

    name: str
    size_mb: float | None


class MetadataDbSchemaIndexesResponse(BaseModel):
    """Response model for schema-wide index inventory."""

    table_name: str
    indexes: list[MetadataDbIndexInfo]
