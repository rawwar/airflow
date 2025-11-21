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

import pytest

pytestmark = pytest.mark.db_test


class TestMetadataDbStatsEndpoint:
    """Base class for metadata DB endpoint tests."""


class TestGetGlobalStats(TestMetadataDbStatsEndpoint):
    def test_get_global_stats_success(self, test_client):
        """Test GET /metadataDB/stats returns 200 with table statistics."""
        response = test_client.get("/metadataDB/stats")
        assert response.status_code == 200

        body = response.json()
        assert "tables" in body
        assert "total_tables" in body
        assert isinstance(body["tables"], list)
        assert body["total_tables"] > 0

        # Check that we have table data
        assert len(body["tables"]) == body["total_tables"]

        # Verify table structure
        for table in body["tables"]:
            assert "table_name" in table
            assert "table_size_mb" in table
            # row_count should be None by default
            assert table.get("row_count") is None
            # table_size_mb should be a float or None
            if table["table_size_mb"] is not None:
                assert isinstance(table["table_size_mb"], float)
                assert table["table_size_mb"] >= 0

    def test_get_global_stats_with_row_count(self, test_client):
        """Test GET /metadataDB/stats?include_row_count=true includes row counts."""
        response = test_client.get("/metadataDB/stats?include_row_count=true")
        assert response.status_code == 200

        body = response.json()
        assert "tables" in body

        # At least one table should have a row count
        row_counts_present = any(table.get("row_count") is not None for table in body["tables"])
        assert row_counts_present

    def test_get_global_stats_without_row_count(self, test_client):
        """Test GET /metadataDB/stats with include_row_count=false."""
        response = test_client.get("/metadataDB/stats?include_row_count=false")
        assert response.status_code == 200

        body = response.json()
        # All tables should have None for row_count
        for table in body["tables"]:
            assert table.get("row_count") is None

    def test_should_respond_401(self, unauthenticated_test_client):
        response = unauthenticated_test_client.get("/metadataDB/stats")
        assert response.status_code == 401

    def test_should_respond_403(self, unauthorized_test_client):
        response = unauthorized_test_client.get("/metadataDB/stats")
        assert response.status_code == 403


class TestGetTableStats(TestMetadataDbStatsEndpoint):
    def test_get_table_stats_success(self, test_client):
        """Test GET /metadataDB/stats/dag returns 200 with table data."""
        # Use a known Airflow table
        response = test_client.get("/metadataDB/stats/dag")
        assert response.status_code == 200

        body = response.json()
        assert "tables" in body
        assert "total_tables" in body
        assert body["total_tables"] == 1
        assert len(body["tables"]) == 1

        # Verify the table data
        table = body["tables"][0]
        assert table["table_name"] == "dag"
        assert "table_size_mb" in table
        # row_count should be None by default
        assert table.get("row_count") is None
        # table_size_mb should be a float or None
        if table["table_size_mb"] is not None:
            assert isinstance(table["table_size_mb"], float)

    def test_get_table_stats_with_row_count(self, test_client):
        """Test GET /metadataDB/stats/dag?include_row_count=true returns row count."""
        response = test_client.get("/metadataDB/stats/dag?include_row_count=true")
        assert response.status_code == 200

        body = response.json()
        table = body["tables"][0]
        assert table["table_name"] == "dag"
        # row_count should be present and >= 0
        assert "row_count" in table
        assert table["row_count"] is not None
        assert table["row_count"] >= 0

    def test_should_respond_404(self, test_client):
        response = test_client.get("/metadataDB/stats/non_existent_table")
        assert response.status_code == 404

        body = response.json()
        assert "detail" in body
        assert body["detail"] == "Table 'non_existent_table' not found in Airflow metadata schema"

    def test_should_respond_401(self, unauthenticated_test_client):
        response = unauthenticated_test_client.get("/metadataDB/stats/dag")
        assert response.status_code == 401

    def test_should_respond_403(self, unauthorized_test_client):
        response = unauthorized_test_client.get("/metadataDB/stats/dag")
        assert response.status_code == 403

    @pytest.mark.parametrize(
        "table_name",
        [
            "dag",
            "dag_run",
            "task_instance",
            "connection",
            "variable",
        ],
    )
    def test_get_stats_for_various_tables(self, test_client, table_name):
        response = test_client.get(f"/metadataDB/stats/{table_name}")
        assert response.status_code == 200

        body = response.json()
        assert body["total_tables"] == 1
        assert body["tables"][0]["table_name"] == table_name


class TestGetSchemaIndexes(TestMetadataDbStatsEndpoint):
    def test_get_schema_indexes_success(self, test_client):
        """Test GET /metadataDB/indexes returns 200 with schema-wide index data."""
        response = test_client.get("/metadataDB/indexes")
        assert response.status_code == 200

        body = response.json()
        assert isinstance(body, list)
        assert len(body) > 0

        # Check structure of each table entry
        for table_entry in body:
            assert "table_name" in table_entry
            assert "indexes" in table_entry
            assert isinstance(table_entry["indexes"], list)

            # Verify index structure
            for index in table_entry["indexes"]:
                assert "name" in index
                assert "size_mb" in index
                # size_mb can be None for unsupported dialects (e.g., SQLite)
                if index["size_mb"] is not None:
                    assert isinstance(index["size_mb"], float)
                    assert index["size_mb"] >= 0

    def test_schema_indexes_includes_known_tables(self, test_client):
        """Test that response includes some known Airflow tables with indexes."""
        response = test_client.get("/metadataDB/indexes")
        assert response.status_code == 200

        body = response.json()
        table_names = [entry["table_name"] for entry in body]

        # Check that common Airflow tables are present
        known_tables = ["dag", "dag_run", "task_instance"]
        for table in known_tables:
            assert table in table_names, f"Expected table '{table}' not found in response"

    def test_should_respond_401(self, unauthenticated_test_client):
        response = unauthenticated_test_client.get("/metadataDB/indexes")
        assert response.status_code == 401

    def test_should_respond_403(self, unauthorized_test_client):
        response = unauthorized_test_client.get("/metadataDB/indexes")
        assert response.status_code == 403


class TestGetTableIndexes(TestMetadataDbStatsEndpoint):
    def test_get_table_indexes_success(self, test_client):
        """Test GET /metadataDB/indexes/{table_name} returns 200 with index data."""
        # Use a known Airflow table
        response = test_client.get("/metadataDB/indexes/dag")
        assert response.status_code == 200

        body = response.json()
        assert "table_name" in body
        assert body["table_name"] == "dag"
        assert "indexes" in body
        assert isinstance(body["indexes"], list)

        # Verify index structure if indexes exist
        for index in body["indexes"]:
            assert "name" in index
            assert "size_mb" in index
            # size_mb can be None for unsupported dialects (e.g., SQLite)
            if index["size_mb"] is not None:
                assert isinstance(index["size_mb"], float)
                assert index["size_mb"] >= 0

    def test_should_respond_404(self, test_client):
        """Test GET /metadataDB/indexes/{table_name} returns 404 for missing table."""
        response = test_client.get("/metadataDB/indexes/non_existent_table")
        assert response.status_code == 404

        body = response.json()
        assert "detail" in body
        assert body["detail"] == "Table 'non_existent_table' not found in Airflow metadata schema"

    def test_should_respond_401(self, unauthenticated_test_client):
        response = unauthenticated_test_client.get("/metadataDB/indexes/dag")
        assert response.status_code == 401

    def test_should_respond_403(self, unauthorized_test_client):
        response = unauthorized_test_client.get("/metadataDB/indexes/dag")
        assert response.status_code == 403

    @pytest.mark.parametrize(
        "table_name",
        [
            "dag",
            "dag_run",
            "task_instance",
            "connection",
            "variable",
        ],
    )
    def test_get_indexes_for_various_tables(self, test_client, table_name):
        """Test getting indexes for various Airflow tables."""
        response = test_client.get(f"/metadataDB/indexes/{table_name}")
        assert response.status_code == 200

        body = response.json()
        assert body["table_name"] == table_name
        assert "indexes" in body
