# 78 HTTP Operators

## Overview

HTTP operators enable interaction with REST APIs, webhooks, and web services from Airflow workflows. This section covers SimpleHttpOperator, HttpSensor, authentication methods, request handling, and response processing for Airflow 3.x.

## Research & Background

### Key Concepts
- **SimpleHttpOperator**: Makes HTTP requests to endpoints
- **HttpSensor**: Waits for HTTP endpoint to return expected response
- **HTTP Connection**: Stores base URL and credentials
- **Request/Response Handling**: Data serialization and parsing
- **Authentication**: Various auth methods for APIs

### Airflow 3.x Features
- Improved response handling
- Better error messages
- Deferrable HTTP sensor support
- Enhanced authentication options
- Request/response logging

### Prerequisites
- Airflow 3.x with http provider
- Understanding of REST APIs
- Basic HTTP concepts (methods, headers, status codes)

### Learning Objectives
After completing the DAGs in this section, users will be able to:
1. Configure HTTP connections for APIs
2. Make GET, POST, PUT, DELETE requests
3. Handle authentication securely
4. Process API responses
5. Build robust API integration workflows

---

# 78.1 HTTP Connection Setup

## Overview
Configuring connections for HTTP endpoints.

## Tasks

### - [ ] 78.1.1 Basic HTTP Connection
Filename: `78_01_01_basic_http_connection.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Create HTTP connection

- [ ] Connection type http
- [ ] Host and port configuration
- [ ] Schema (http/https)
- [ ] Extra parameters

**Expected Behavior**: Connection accessible

---

### - [ ] 78.1.2 Authentication in Connections
Filename: `78_01_02_auth_in_connections.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Store credentials in connection

- [ ] Login/password for basic auth
- [ ] API key in extra field
- [ ] Bearer token storage
- [ ] Secure credential handling

**Expected Behavior**: Auth credentials used

---

### - [ ] 78.1.3 Default Headers Configuration
Filename: `78_01_03_default_headers.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Set default request headers

- [ ] Content-Type header
- [ ] Accept header
- [ ] Custom headers in extra
- [ ] Header inheritance

**Expected Behavior**: Headers applied to requests

---

### - [ ] 78.1.4 Multiple API Connections
Filename: `78_01_04_multiple_connections.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Manage multiple APIs

- [ ] Separate connection per API
- [ ] Environment-specific connections
- [ ] Connection naming conventions
- [ ] Connection selection at runtime

**Expected Behavior**: Correct API connection used

---

### - [ ] 78.1.5 Connection Testing
Filename: `78_01_05_connection_testing.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Verify HTTP connections

- [ ] Test connection via UI
- [ ] Health check endpoints
- [ ] Connection validation DAG
- [ ] Troubleshoot connectivity

**Expected Behavior**: Connection status verified

---

# 78.2 SimpleHttpOperator

## Overview
Making HTTP requests from tasks.

## Tasks

### - [ ] 78.2.1 GET Request
Filename: `78_02_01_get_request.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Make HTTP GET request

- [ ] SimpleHttpOperator with method='GET'
- [ ] endpoint parameter
- [ ] http_conn_id reference
- [ ] Response handling

**Expected Behavior**: GET request succeeds

---

### - [ ] 78.2.2 POST Request with JSON
Filename: `78_02_02_post_json.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Send JSON data via POST

- [ ] method='POST'
- [ ] data parameter with dict
- [ ] JSON serialization
- [ ] Content-Type header

**Expected Behavior**: JSON POST succeeds

---

### - [ ] 78.2.3 PUT and DELETE Requests
Filename: `78_02_03_put_delete.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Update and delete via HTTP

- [ ] PUT request for updates
- [ ] DELETE request
- [ ] PATCH request
- [ ] Idempotency considerations

**Expected Behavior**: Update/delete operations work

---

### - [ ] 78.2.4 Query Parameters
Filename: `78_02_04_query_parameters.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Pass URL query parameters

- [ ] data parameter for GET queries
- [ ] URL encoding
- [ ] Multiple query params
- [ ] Template query values

**Expected Behavior**: Query params in request

---

### - [ ] 78.2.5 Custom Headers per Request
Filename: `78_02_05_custom_headers.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Override headers per request

- [ ] headers parameter
- [ ] Merge with connection headers
- [ ] Authorization headers
- [ ] Request-specific headers

**Expected Behavior**: Headers customized

---

# 78.3 Response Handling

## Overview
Processing API responses.

## Tasks

### - [ ] 78.3.1 Response to XCom
Filename: `78_03_01_response_xcom.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Store response for downstream

- [ ] response_filter for extraction
- [ ] Push to XCom
- [ ] JSON response parsing
- [ ] XCom size considerations

**Expected Behavior**: Response in XCom

---

### - [ ] 78.3.2 Response Validation
Filename: `78_03_02_response_validation.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Validate API responses

- [ ] response_check function
- [ ] Status code validation
- [ ] Response body validation
- [ ] Fail on invalid response

**Expected Behavior**: Invalid responses cause failure

---

### - [ ] 78.3.3 Parsing JSON Responses
Filename: `78_03_03_parsing_json.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Extract data from JSON

- [ ] response_filter with JSON parsing
- [ ] Nested field extraction
- [ ] Handle missing fields
- [ ] List/array responses

**Expected Behavior**: JSON data extracted

---

### - [ ] 78.3.4 Handling Non-JSON Responses
Filename: `78_03_04_non_json_responses.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Process XML, text, binary

- [ ] Text response handling
- [ ] XML parsing
- [ ] Binary data (files)
- [ ] Content-Type detection

**Expected Behavior**: Non-JSON responses handled

---

### - [ ] 78.3.5 Error Response Handling
Filename: `78_03_05_error_responses.py` | Tags: `['reference', 'core', 'intermediate', 'failure']`

**Purpose**: Handle API errors gracefully

- [ ] HTTP error status codes
- [ ] Error message extraction
- [ ] Retry on transient errors
- [ ] Log error details

**Expected Behavior**: Errors handled appropriately

---

# 78.4 Authentication Methods

## Overview
Securing API requests with authentication.

## Tasks

### - [ ] 78.4.1 Basic Authentication
Filename: `78_04_01_basic_auth.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Use HTTP basic auth

- [ ] Username/password in connection
- [ ] Authorization header
- [ ] Secure credential storage
- [ ] Connection test

**Expected Behavior**: Basic auth works

---

### - [ ] 78.4.2 Bearer Token Authentication
Filename: `78_04_02_bearer_token.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: JWT/OAuth bearer tokens

- [ ] Token in connection extra
- [ ] Authorization: Bearer header
- [ ] Token refresh patterns
- [ ] Token expiration handling

**Expected Behavior**: Bearer token auth works

---

### - [ ] 78.4.3 API Key Authentication
Filename: `78_04_03_api_key_auth.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: API key in header or query

- [ ] X-API-Key header
- [ ] Query string API key
- [ ] Key rotation handling
- [ ] Multiple key support

**Expected Behavior**: API key auth works

---

### - [ ] 78.4.4 OAuth2 Client Credentials
Filename: `78_04_04_oauth2_client.py` | Tags: `['reference', 'core', 'advanced', 'success']`

**Purpose**: OAuth2 machine-to-machine

- [ ] Token endpoint request
- [ ] Client ID and secret
- [ ] Token caching
- [ ] Auto-refresh on expiry

**Expected Behavior**: OAuth2 flow works

---

### - [ ] 78.4.5 Custom Authentication
Filename: `78_04_05_custom_auth.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Implement custom auth

- [ ] Custom auth hook
- [ ] Signature-based auth
- [ ] Multi-step auth
- [ ] Session-based auth

**Expected Behavior**: Custom auth works

---

# 78.5 HttpSensor and Advanced Patterns

## Overview
Waiting for APIs and complex integrations.

## Tasks

### - [ ] 78.5.1 Basic HttpSensor
Filename: `78_05_01_basic_http_sensor.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Wait for API condition

- [ ] HttpSensor configuration
- [ ] response_check function
- [ ] Poke interval
- [ ] Timeout handling

**Expected Behavior**: Sensor waits for condition

---

### - [ ] 78.5.2 Deferrable HttpSensor
Filename: `78_05_02_deferrable_http_sensor.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Async HTTP waiting

- [ ] deferrable=True parameter
- [ ] HttpSensorAsync
- [ ] Resource efficiency
- [ ] Long-running API waits

**Expected Behavior**: Worker freed while waiting

---

### - [ ] 78.5.3 Pagination Handling
Filename: `78_05_03_pagination.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Handle paginated APIs

- [ ] Page-based pagination
- [ ] Cursor-based pagination
- [ ] Aggregate all pages
- [ ] Rate limit compliance

**Expected Behavior**: All pages retrieved

---

### - [ ] 78.5.4 Webhook Trigger Integration
Filename: `78_05_04_webhook_trigger.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Send webhook notifications

- [ ] POST to webhook URL
- [ ] Slack/Teams webhooks
- [ ] Custom webhook payloads
- [ ] Retry on failure

**Expected Behavior**: Webhook delivered

---

### - [ ] 78.5.5 Rate Limiting and Retries
Filename: `78_05_05_rate_limiting.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Handle API rate limits

- [ ] Detect rate limit responses
- [ ] Implement backoff
- [ ] Retry-After header
- [ ] Request queuing

**Expected Behavior**: Rate limits respected

---

# 78.6 Anti-Patterns and Common Mistakes

## Overview
Avoiding common HTTP integration pitfalls.

## Tasks

### - [ ] 78.6.1 Ignoring HTTP Error Codes
Filename: `78_06_01_ignoring_error_codes.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Handle HTTP errors properly

- [ ] Not checking status codes
- [ ] Treating 4xx as success
- [ ] Missing 5xx handling
- [ ] Silent failures

**Expected Behavior**: Errors properly caught

---

### - [ ] 78.6.2 Hardcoded URLs Anti-Pattern
Filename: `78_06_02_hardcoded_urls.py` | Tags: `['reference', 'anti-pattern', 'beginner', 'failure']`

**Purpose**: Avoid static URL configuration

- [ ] URLs in DAG code
- [ ] Environment mismatch
- [ ] No connection abstraction
- [ ] Maintenance problems

**Expected Behavior**: Use connections instead

---

### - [ ] 78.6.3 Missing Timeout Configuration
Filename: `78_06_03_missing_timeouts.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Always configure timeouts

- [ ] Default infinite timeout
- [ ] Blocked workers
- [ ] Connection timeouts
- [ ] Read timeouts

**Expected Behavior**: Timeouts always set

---

### - [ ] 78.6.4 Credential Exposure Risks
Filename: `78_06_04_credential_exposure.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Protect API credentials

- [ ] Logging full requests
- [ ] Credentials in URLs
- [ ] Plain text storage
- [ ] Token in XCom

**Expected Behavior**: Credentials secured

---

### - [ ] 78.6.5 Ignoring Rate Limits
Filename: `78_06_05_ignoring_rate_limits.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Respect API rate limits

- [ ] No backoff strategy
- [ ] Ignoring 429 responses
- [ ] Parallel request storms
- [ ] API ban consequences

**Expected Behavior**: Rate limits respected

---

# 78.7 Testing HTTP Integrations

## Overview
Testing HTTP operators and API integrations.

## Tasks

### - [ ] 78.7.1 Mock API Testing with responses
Filename: `78_07_01_mock_api_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test with mocked HTTP responses

- [ ] responses library usage
- [ ] Mock different status codes
- [ ] Simulate API behavior
- [ ] Test error conditions

**Expected Behavior**: API calls mocked

---

### - [ ] 78.7.2 Local API Server Testing
Filename: `78_07_02_local_api_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test with local API server

- [ ] Flask test server
- [ ] Docker-based APIs
- [ ] Realistic responses
- [ ] Network conditions

**Expected Behavior**: Local API testing works

---

### - [ ] 78.7.3 WireMock Integration Testing
Filename: `78_07_03_wiremock_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Use WireMock for API mocking

- [ ] WireMock setup
- [ ] Stub configuration
- [ ] Request matching
- [ ] Response templating

**Expected Behavior**: WireMock tests pass

---

### - [ ] 78.7.4 Contract Testing for APIs
Filename: `78_07_04_contract_testing.py` | Tags: `['reference', 'testing', 'advanced', 'success']`

**Purpose**: Verify API contracts

- [ ] Pact contract testing
- [ ] Schema validation
- [ ] Breaking change detection
- [ ] Consumer-driven contracts

**Expected Behavior**: API contracts verified

---

### - [ ] 78.7.5 Performance Testing HTTP Tasks
Filename: `78_07_05_performance_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test HTTP task performance

- [ ] Response time assertions
- [ ] Concurrent request testing
- [ ] Timeout behavior
- [ ] Retry performance

**Expected Behavior**: Performance tested

---

# 78.8 Performance Optimization

## Overview
Optimizing HTTP operator performance.

## Tasks

### - [ ] 78.8.1 Connection Pooling
Filename: `78_08_01_connection_pooling.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Reuse HTTP connections

- [ ] Connection keep-alive
- [ ] Pool size configuration
- [ ] Session reuse
- [ ] Connection lifecycle

**Expected Behavior**: Connections reused efficiently

---

### - [ ] 78.8.2 Parallel HTTP Requests
Filename: `78_08_02_parallel_requests.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Execute requests in parallel

- [ ] Task mapping for parallel calls
- [ ] Async HTTP patterns
- [ ] Result aggregation
- [ ] Rate limit compliance

**Expected Behavior**: Parallel requests efficient

---

### - [ ] 78.8.3 Response Caching Strategies
Filename: `78_08_03_response_caching.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Cache API responses

- [ ] Cache-Control headers
- [ ] External cache integration
- [ ] Cache invalidation
- [ ] ETag support

**Expected Behavior**: Responses cached appropriately

---

### - [ ] 78.8.4 Compression for Large Payloads
Filename: `78_08_04_compression_payloads.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Handle large request/response bodies

- [ ] gzip compression
- [ ] Content-Encoding header
- [ ] Chunked transfer
- [ ] Memory efficiency

**Expected Behavior**: Large payloads handled

---

### - [ ] 78.8.5 Optimizing Pagination Performance
Filename: `78_08_05_pagination_performance.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Efficient paginated data retrieval

- [ ] Page size optimization
- [ ] Parallel page fetching
- [ ] Cursor vs offset
- [ ] Early termination

**Expected Behavior**: Pagination efficient

---

# 78.9 Debugging HTTP Issues

## Overview
Troubleshooting HTTP integration problems.

## Tasks

### - [ ] 78.9.1 Request/Response Logging
Filename: `78_09_01_request_response_logging.py` | Tags: `['reference', 'debugging', 'beginner', 'success']`

**Purpose**: Log HTTP traffic for debugging

- [ ] Enable request logging
- [ ] Response body logging
- [ ] Header inspection
- [ ] Redact sensitive data

**Expected Behavior**: HTTP traffic visible

---

### - [ ] 78.9.2 SSL Certificate Debugging
Filename: `78_09_02_ssl_debugging.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Diagnose SSL/TLS issues

- [ ] Certificate verification errors
- [ ] Self-signed certificates
- [ ] Certificate chain issues
- [ ] TLS version problems

**Expected Behavior**: SSL issues resolved

---

### - [ ] 78.9.3 Proxy Configuration Issues
Filename: `78_09_03_proxy_issues.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Debug proxy-related problems

- [ ] Proxy environment variables
- [ ] HTTPS proxy setup
- [ ] No-proxy configuration
- [ ] Proxy authentication

**Expected Behavior**: Proxy issues fixed

---

### - [ ] 78.9.4 Timeout and Retry Debugging
Filename: `78_09_04_timeout_debugging.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Diagnose timeout issues

- [ ] Identify timeout source
- [ ] Network vs server timeout
- [ ] Retry loop diagnosis
- [ ] Exponential backoff tuning

**Expected Behavior**: Timeouts understood

---

### - [ ] 78.9.5 Authentication Failure Debugging
Filename: `78_09_05_auth_debugging.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Debug auth failures

- [ ] 401 vs 403 distinction
- [ ] Token expiration
- [ ] OAuth flow debugging
- [ ] Credential verification

**Expected Behavior**: Auth issues resolved

---

# 78.10 Real-World Examples

## Overview
Production HTTP integration patterns.

## Tasks

### - [ ] 78.10.1 REST API Data Ingestion Pipeline
Filename: `78_10_01_api_data_ingestion.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Ingest data from REST APIs

- [ ] Paginated data fetch
- [ ] Incremental ingestion
- [ ] Data validation
- [ ] Error recovery

**Expected Behavior**: API data ingested

---

### - [ ] 78.10.2 Multi-Service Orchestration
Filename: `78_10_02_multi_service_orchestration.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Coordinate multiple APIs

- [ ] Service dependencies
- [ ] Data passing between services
- [ ] Error propagation
- [ ] Transaction semantics

**Expected Behavior**: Services orchestrated

---

### - [ ] 78.10.3 Webhook-Triggered Processing
Filename: `78_10_03_webhook_processing.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Process incoming webhooks

- [ ] Webhook endpoint setup
- [ ] Payload validation
- [ ] Triggered processing
- [ ] Acknowledgment patterns

**Expected Behavior**: Webhooks processed

---

### - [ ] 78.10.4 Third-Party SaaS Integration
Filename: `78_10_04_saas_integration.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Integrate with SaaS APIs

- [ ] OAuth2 authentication
- [ ] Rate limit handling
- [ ] Data synchronization
- [ ] Error notifications

**Expected Behavior**: SaaS integration works

---

### - [ ] 78.10.5 Health Check and Monitoring Pipeline
Filename: `78_10_05_health_monitoring.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Monitor external services

- [ ] Endpoint health checks
- [ ] Response time tracking
- [ ] Availability metrics
- [ ] Alert on failures

**Expected Behavior**: Services monitored

---

# Summary

## Topic Completion Checklist
- [ ] HTTP connection setup covered
- [ ] SimpleHttpOperator documented
- [ ] Response handling patterns included
- [ ] Authentication methods explained
- [ ] Sensors and advanced patterns provided
- [ ] Anti-patterns identified
- [ ] Testing strategies covered
- [ ] Performance optimization included
- [ ] Debugging guidance provided
- [ ] Real-world examples included

## Related Topics
- Section 08: Sensors
- Section 51: Deferrable Operators
- Section 81: Connections

## Notes for Implementation
- Use httpbin.org for examples
- Show various auth methods
- Include error scenarios
- Demonstrate pagination
- Cover rate limiting
