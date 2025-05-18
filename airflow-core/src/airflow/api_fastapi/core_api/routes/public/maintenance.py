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

from airflow.api_fastapi.common.router import AirflowRouter

maintenance_router = AirflowRouter(tags=["Maintenance"], prefix="/maintenance")


@maintenance_router.post(
    "/db/cleanup",
    dependencies=[],  # Create a new `require_access_db(method="POST")` dependency
)
def db_cleanup():
    pass


@maintenance_router.post(
    "/db/backup",
    dependencies=[],  # Create a new `require_access_db(method="POST")` dependency
)
def db_backup():
    pass


@maintenance_router.get(
    "/db/list_backups",
    dependencies=[],  # Create a new `require_access_db(method="GET")` dependency
)
def db_list_backups():
    pass


@maintenance_router.post(
    "/db/restore",
    dependencies=[],  # Create a new `require_access_db(method="POST")` dependency
)
def db_restore():
    pass


@maintenance_router.delete(
    "db/delete_backup_tables",
    dependencies=[],  # Create a new `require_access_db(method="DELETE")` dependency
)
@maintenance_router.get(
    "/db/table_stats",
    dependencies=[],  # Create a new `require_access_db(method="GET")` dependency
)
def db_table_stats():
    pass


@maintenance_router.post(
    "/db/reindex",
    dependencies=[],  # Create a new `require_access_db(method="POST")` dependency
)
def db_reindex():
    pass
