TODO Roadmap for Metadata DB FastAPI Endpoints (execute sequentially)

Complete every checklist item in a step before starting the next step.

## Step 1 – Security Capability Updates
- [ ] Update `airflow/api_fastapi/auth/managers/base_auth_manager.py`:
  - Introduce abstract `has_access_to_db(self, *, user: BaseUser) -> bool` raising `NotImplementedError` by default.
  - Provide reusable helper (e.g. `_raise_metadata_db_forbidden`) for consistent error messaging.
- [ ] Implement `has_access_to_db` in simple auth manager (`airflow/api_fastapi/auth/managers/simple/simple_auth_manager.py`): grant access only to `SimpleAuthManagerRole.ADMIN` (or higher) and add unit coverage in `airflow-core/tests/unit/api_fastapi/auth/managers/simple/test_simple_auth_manager.py`.
- [ ] Implement `has_access_to_db` in FAB auth manager (`providers/fab/src/airflow/providers/fab/auth_manager/fab_auth_manager.py`):
  - Map to a new FAB resource constant (e.g. `RESOURCE_METADATA_DB`) with read action through existing security manager.
  - Ensure FAB role sync seeds the permission; add/extend tests in `providers/fab/tests/unit/fab/auth_manager/test_fab_auth_manager.py` and related security manager tests.
- [ ] Implement `has_access_to_db` in AWS auth manager (`providers/amazon/src/airflow/providers/amazon/aws/auth_manager/aws_auth_manager.py`):
  - Introduce new `AvpEntities.METADATA_DB` constant and ensure schemas/CLI reference it.
  - Extend unit tests in `providers/amazon/tests/unit/amazon/aws/auth_manager/test_aws_auth_manager.py` to cover allow/deny.
- [ ] Implement `has_access_to_db` in Keycloak auth manager (`providers/keycloak/src/airflow/providers/keycloak/auth_manager/keycloak_auth_manager.py`):
  - Add `KeycloakResource.METADATA_DB` and enforce permission requests via `_is_authorized`.
  - Update unit tests in `providers/keycloak/tests/unit/keycloak/auth_manager/test_keycloak_auth_manager.py`.
- [ ] Update provider and core documentation if new permissions/entities require configuration (`providers/fab/docs/`, `providers/amazon/docs/`, `providers/keycloak/docs/`) and ensure release notes mention the new permission requirement where appropriate.

## Step 2 – Shared Dependency & Module Scaffolding
- [ ] Add `requires_metadata_db_access` dependency to `airflow/api_fastapi/core_api/security.py` using `get_auth_manager().has_access_to_db(user)` and returning HTTP 403 when false; add unit tests in `airflow-core/tests/unit/api_fastapi/test_security.py`.
- [ ] Create router module `airflow/api_fastapi/core_api/routes/public/metadata_db.py` with `AirflowRouter(prefix="/metadataDB", tags=["MetadataDB"])` and placeholder route functions guarded by the new dependency.
- [ ] Register the metadata router inside `authenticated_router` in `airflow/api_fastapi/core_api/routes/public/__init__.py`.
- [ ] Create datamodel scaffold `airflow/api_fastapi/core_api/datamodels/metadata_db.py` with placeholder Pydantic classes for stats and index responses (to be filled in later steps).

## Step 3 – Metadata Inspection Utilities
- [ ] Add `airflow/api_fastapi/common/db/metadata_db.py` implementing helper functions:
  - `fetch_global_stats(session)` returning table count, row totals, size metrics when dialect supports.
  - `fetch_table_stats(session, table_name)` returning column metadata, row count, optional size.
  - `fetch_table_indexes(session, table_name)` returning index details.
  - `fetch_schema_indexes(session)` aggregating indexes for all tables.
- [ ] Ensure helpers detect dialect via `session.get_bind().dialect.name` and handle Postgres, MySQL/MariaDB, MSSQL, SQLite with graceful fallbacks when metrics unsupported.
- [ ] Add unit tests in `airflow-core/tests/unit/api_fastapi/common/test_metadata_db.py` covering happy paths, missing table behaviour, and unsupported dialect fallbacks (use SQLite and mocked dialects).

## Step 4 – Endpoint Loop 1 (`GET /metadataDB/stats` and optional `/{table_name}`)
1. Models & Schema
   - [ ] Define Pydantic models in `datamodels/metadata_db.py` for global stats (`MetadataDbStatsResponse`) and table stats (`MetadataDbTableStatsResponse`, `MetadataDbColumnStats`).
   - [ ] Document optional `table_name` path parameter (meaning: when omitted use global stats).
2. Router Implementation
   - [ ] Implement routes in `routes/public/metadata_db.py`:
     - `GET /metadataDB/stats` (no path parameter) → global stats.
     - `GET /metadataDB/stats/{table_name}` → table-specific stats (handle schema-qualified names).
   - [ ] Apply `requires_metadata_db_access` dependency and action logging decorator consistent with other routes.
3. Business Logic
   - [ ] Wire routes to utilities (`fetch_global_stats`, `fetch_table_stats`) and translate exceptions to `HTTPException` (404 for missing table, 501 for unsupported metrics).
4. Tests
   - [ ] Add endpoint tests in `airflow-core/tests/unit/api_fastapi/core_api/test_metadata_db_routes.py` using FastAPI `TestClient` covering authorized success, forbidden access, missing table, and unsupported dialect responses.
   - [ ] Validate serialization for new Pydantic models in tests.
5. Documentation
   - [ ] Update API reference docs (`docs/apache-airflow/api-ref/` or corresponding FastAPI section) with endpoint description, request examples, and Deployment Manager/`has_access_to_db` requirement.

## Step 5 – Endpoint Loop 2 (`GET /metadataDB/indexes`)
1. Models & Schema
   - [ ] Extend `datamodels/metadata_db.py` with `MetadataDbIndexInfo` and `MetadataDbSchemaIndexesResponse` to represent schema-wide index data.
2. Router Implementation
   - [ ] Add route handler `GET /metadataDB/indexes` in `routes/public/metadata_db.py` guarded by `requires_metadata_db_access`.
3. Business Logic
   - [ ] Use `fetch_schema_indexes` utility, returning structured response and including partial-results notes when some tables lack data.
4. Tests
   - [ ] Extend unit tests for utilities (multi-table aggregation, partial failures) and add FastAPI route tests covering success, forbidden access, and partial failure messaging.
5. Documentation
   - [ ] Document schema-wide index endpoint and backend limitations in API docs.

## Step 6 – Endpoint Loop 3 (`GET /metadataDB/indexes/{table_name}`)
1. Models & Schema
   - [ ] Reuse or specialize models in `datamodels/metadata_db.py` for per-table index detail (`MetadataDbTableIndexResponse`).
2. Router Implementation
   - [ ] Add `GET /metadataDB/indexes/{table_name}` route in `routes/public/metadata_db.py`, sharing dependency and logging.
3. Business Logic
   - [ ] Call `fetch_table_indexes`, normalize identifier quoting, and map outcomes to HTTP errors (404 when table absent, 501 when unsupported).
4. Tests
   - [ ] Add unit tests ensuring table-specific index retrieval works (including composite/partial indexes) and FastAPI tests covering success, forbidden, missing table, unsupported dialect.
5. Documentation
   - [ ] Update API docs with per-table index usage examples and describe limitations.

## Step 7 – Final Integration
- [ ] Ensure router import ordering keeps alphabetical grouping in `public/__init__.py` and add any missing exports in `__all__` files.
- [ ] Regenerate or verify OpenAPI schema (without running Breeze) to confirm endpoints and models appear with correct security notes.
- [ ] Update release notes (`docs/apache-airflow/stable/changelog.rst` or relevant provider changelogs) summarizing metadata DB inspection endpoints and new `has_access_to_db` permission.
- [ ] Provide guidance in developer docs (e.g. `contributing-docs/` or provider READMEs) for configuring FAB roles, AWS AVP policies, and Keycloak resources to enable access.
