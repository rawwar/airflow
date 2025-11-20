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

from airflow.api_fastapi.core_api.base import AirflowRouter
from fastapi import Depends

from airflow.api_fastapi.core_api.security import requires_metadata_db_access


metadata_db_router = AirflowRouter(prefix="/metadataDB", tags=["MetadataDB"])


@metadata_db_router.get(
    "/stats",
    dependencies=[Depends(requires_metadata_db_access())],
)
async def get_metadata_db_stats():
    raise NotImplementedError


@metadata_db_router.get(
    "/stats/{table_name}",
    dependencies=[Depends(requires_metadata_db_access())],
)
async def get_metadata_db_table_stats(table_name: str):
    raise NotImplementedError


@metadata_db_router.get(
    "/indexes",
    dependencies=[Depends(requires_metadata_db_access())],
)
async def get_metadata_db_indexes():
    raise NotImplementedError


@metadata_db_router.get(
    "/indexes/{table_name}",
    dependencies=[Depends(requires_metadata_db_access())],
)
async def get_metadata_db_table_indexes(table_name: str):
    raise NotImplementedError
