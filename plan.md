# FastAPI Endpoint Metrics Tracking Implementation Plan

## Executive Summary
This plan details the implementation of comprehensive metrics tracking for all FastAPI endpoints in Apache Airflow. The metrics will track API call counts, response times, error rates, and provide endpoint-specific statistics that integrate with Airflow's existing metrics infrastructure (StatsD, DataDog, OpenTelemetry).

## Goals
- Track API endpoint usage patterns (call counts, frequency)
- Monitor endpoint performance (response times, latency percentiles)
- Capture error rates and status code distributions
- Provide granular per-endpoint and aggregated statistics
- Ensure minimal performance overhead
- Support all existing metrics backends (StatsD, DataDog, OpenTelemetry)

## Current State Analysis

### Existing Metrics Infrastructure
1. **Stats Module** (`airflow/stats.py`):
   - Central metrics facade using metaclass pattern
   - Supports multiple backends: StatsD, DataDog, OpenTelemetry
   - Provides methods: `incr()`, `decr()`, `gauge()`, `timing()`, `timer()`

2. **Metrics Backends** (`airflow/metrics/`):
   - `base_stats_logger.py`: Protocol definition for stats loggers
   - `statsd_logger.py`: StatsD implementation
   - `datadog_logger.py`: DataDog specific implementation
   - `otel_logger.py`: OpenTelemetry implementation

3. **Configuration** (`[metrics]` section in airflow.cfg):
   - `statsd_on`: Enable StatsD metrics
   - `otel_on`: Enable OpenTelemetry metrics
   - `statsd_datadog_enabled`: Enable DataDog integration
   - `metrics_allow_list`/`metrics_block_list`: Metric filtering

4. **Current FastAPI App Structure** (`airflow/api_fastapi/`):
   - Main app creation in `app.py`
   - Core API routes in `core_api/routes/`
   - Execution API in `execution_api/`
   - Middleware support via `init_middlewares()`

## Implementation Design

### 1. Metrics Middleware Component

#### Location: `airflow/api_fastapi/common/middleware/metrics.py`

Core metrics middleware that intercepts all requests/responses:
- Track request count, duration, status, errors
- Report metrics via Airflow Stats system
- Support path normalization and tagging

#### Metrics to Collect:
- **Request Count**: `api.request.count` (tags: endpoint, method, status)
- **Request Duration**: `api.request.duration` (tags: endpoint, method, status)
- **Active Requests**: `api.request.active` (gauge)
- **Error Count**: `api.request.error` (tags: endpoint, method, error_type)
- **Request Size**: `api.request.size.bytes` (tags: endpoint, method)
- **Response Size**: `api.response.size.bytes` (tags: endpoint, method)
- **Authentication**: `api.auth.count` (tags: auth_type, success)

### 2. Endpoint Registry System

#### Location: `airflow/api_fastapi/common/metrics_registry.py`

Registry to track endpoint metadata and statistics:
- Register endpoints with metadata
- Track per-endpoint statistics
- Provide aggregated metrics
- Support metric reset and cleanup

### 3. Metrics API Endpoints

#### New Router: `airflow/api_fastapi/core_api/routes/public/metrics.py`

Endpoints to expose:
- `GET /api/v2/metrics/endpoints` - List all tracked endpoints with statistics
- `GET /api/v2/metrics/endpoints/{endpoint_path}` - Get specific endpoint metrics
- `GET /api/v2/metrics/summary` - Aggregated API metrics summary
- `GET /api/v2/metrics/health` - API health metrics

### 4. Database Storage (Optional)

#### New Models: `airflow/models/api_metrics.py`

Periodic snapshots of API metrics for historical analysis with columns:
- endpoint, method, timestamp
- request_count, error_count
- avg_duration_ms, p50_duration_ms, p95_duration_ms, p99_duration_ms

## Implementation Steps

### Phase 1: Core Metrics Infrastructure

**TODO 1.1**: Create metrics middleware base implementation
- [ ] Create `airflow/api_fastapi/common/middleware/metrics.py`
- [ ] Implement `APIMetricsMiddleware` class with ASGI interface
- [ ] Add request start/end timing logic
- [ ] Extract endpoint path, method, and normalize for metrics
- [ ] Handle async request/response flow

**TODO 1.2**: Integrate with Stats system
- [ ] Import and use `airflow.stats.Stats` for metric emission
- [ ] Add configuration to enable/disable API metrics
- [ ] Implement metric name formatting with configurable prefix
- [ ] Add tags support for dimensional metrics

**TODO 1.3**: Add middleware to FastAPI apps
- [ ] Update `airflow/api_fastapi/core_api/app.py` to register middleware
- [ ] Update `airflow/api_fastapi/execution_api/app.py` to register middleware
- [ ] Ensure middleware ordering (metrics should be early in chain)
- [ ] Add configuration option `[api] metrics_enabled`

### Phase 2: Metrics Collection Enhancement

**TODO 2.1**: Implement comprehensive metrics collection
- [ ] Track request/response sizes
- [ ] Capture authentication method and success/failure
- [ ] Record database query counts per request (via context)
- [ ] Track rate limiting hits and quota usage

**TODO 2.2**: Add endpoint path normalization
- [ ] Convert path parameters to placeholders (e.g., `/dags/{dag_id}`)
- [ ] Group similar endpoints for aggregation
- [ ] Handle regex patterns in routes
- [ ] Prevent high-cardinality metric explosion

**TODO 2.3**: Implement error tracking
- [ ] Capture exception types and messages
- [ ] Track HTTP error codes separately
- [ ] Add stack trace sampling for 5xx errors
- [ ] Report validation errors separately

### Phase 3: Metrics Registry and Storage

**TODO 3.1**: Create endpoint metrics registry
- [ ] Implement `airflow/api_fastapi/common/metrics_registry.py`
- [ ] Track per-endpoint statistics in memory
- [ ] Add LRU cache for recent metrics
- [ ] Implement periodic stats calculation

**TODO 3.2**: Add database persistence (optional)
- [ ] Create migration for `api_metric_snapshots` table
- [ ] Implement periodic snapshot task
- [ ] Add retention policy for old metrics
- [ ] Create cleanup command

**TODO 3.3**: Implement metrics aggregation
- [ ] Calculate percentiles (p50, p95, p99)
- [ ] Track moving averages
- [ ] Implement rate calculation
- [ ] Add trend detection

### Phase 4: Metrics API Endpoints

**TODO 4.1**: Create metrics router
- [ ] Create `airflow/api_fastapi/core_api/routes/public/metrics.py`
- [ ] Define Pydantic models for responses
- [ ] Add authentication/authorization checks
- [ ] Implement caching for expensive queries

**TODO 4.2**: Implement endpoint statistics API
- [ ] `GET /api/v2/metrics/endpoints` - paginated list
- [ ] `GET /api/v2/metrics/endpoints/{path}` - detailed stats
- [ ] Add filtering by time range, status codes
- [ ] Support CSV/JSON export formats

**TODO 4.3**: Create metrics summary endpoint
- [ ] Aggregate total requests, errors, latency
- [ ] Calculate API availability percentage
- [ ] Show top endpoints by various metrics
- [ ] Add comparison with previous period

**TODO 4.4**: Add health metrics endpoint
- [ ] Current request rate and latency
- [ ] Error rate threshold alerting
- [ ] Circuit breaker status
- [ ] Resource utilization metrics

### Phase 5: Integration with Existing Systems

**TODO 5.1**: StatsD integration optimization
- [ ] Batch metric submissions
- [ ] Add local aggregation before sending
- [ ] Implement sampling for high-volume endpoints
- [ ] Add metric buffering with overflow protection

**TODO 5.2**: OpenTelemetry trace correlation
- [ ] Link metrics with distributed traces
- [ ] Add trace ID to metric tags
- [ ] Export metrics via OTLP
- [ ] Implement exemplar support

**TODO 5.3**: DataDog APM integration
- [ ] Add DataDog trace correlation
- [ ] Implement custom DataDog dashboards
- [ ] Set up automatic alerting rules
- [ ] Add service map integration

### Phase 6: Performance Optimization

**TODO 6.1**: Minimize overhead
- [ ] Use async metrics emission
- [ ] Implement metric sampling strategies
- [ ] Add circuit breaker for metrics system
- [ ] Profile and optimize hot paths

**TODO 6.2**: Add caching layer
- [ ] Cache expensive metric calculations
- [ ] Implement incremental updates
- [ ] Use Redis for distributed cache (optional)
- [ ] Add cache warming strategies

**TODO 6.3**: Implement batching
- [ ] Batch database writes for snapshots
- [ ] Aggregate metrics locally before emission
- [ ] Use bulk APIs where available
- [ ] Implement write-through caching

### Phase 7: Monitoring and Alerting

**TODO 7.1**: Create default alerts
- [ ] High error rate (>5% 5xx errors)
- [ ] Slow response times (p95 > threshold)
- [ ] Unusual traffic patterns
- [ ] Authentication failures spike

**TODO 7.2**: Add Grafana dashboards
- [ ] Create dashboard templates
- [ ] Add to Airflow helm chart
- [ ] Document dashboard usage
- [ ] Include example queries

**TODO 7.3**: Implement SLO tracking
- [ ] Define default SLO targets
- [ ] Track error budget consumption
- [ ] Add burndown visualizations
- [ ] Generate SLO reports

### Phase 8: Documentation and Testing

**TODO 8.1**: Write comprehensive documentation
- [ ] Add metrics configuration guide
- [ ] Document available metrics and tags
- [ ] Create troubleshooting guide
- [ ] Add performance tuning guide

**TODO 8.2**: Create unit tests
- [ ] Test middleware with mock ASGI apps
- [ ] Test metric emission with mock Stats
- [ ] Test path normalization edge cases
- [ ] Test error handling scenarios

**TODO 8.3**: Add integration tests
- [ ] Test with real FastAPI endpoints
- [ ] Verify metrics with different backends
- [ ] Test database persistence
- [ ] Load test metric overhead

**TODO 8.4**: Add example configurations
- [ ] StatsD configuration example
- [ ] DataDog configuration example
- [ ] OpenTelemetry configuration example
- [ ] Grafana dashboard JSON exports

## Configuration Schema

### New Configuration Options

```ini
[api]
# Enable metrics collection for API endpoints
metrics_enabled = True

# Endpoints to exclude from metrics (comma-separated)
metrics_excluded_endpoints = /health,/api/v2/metrics

# Enable detailed metrics (may impact performance)
metrics_detailed = False

# Sampling rate for metrics (0.0-1.0)
metrics_sample_rate = 1.0

[metrics]
# API metrics specific prefix
api_metrics_prefix = airflow.api

# Enable metric persistence to database
api_metrics_persistence = False

# Retention days for persisted metrics
api_metrics_retention_days = 30

# Snapshot interval in seconds
api_metrics_snapshot_interval = 300
```

## Testing Strategy

1. **Unit Tests**:
   - Middleware logic isolation
   - Metric calculation accuracy
   - Error handling paths
   - Configuration validation

2. **Integration Tests**:
   - End-to-end metric flow
   - Multiple backend verification
   - Performance regression tests
   - Load testing with metrics enabled

3. **Performance Tests**:
   - Measure overhead per request
   - Test under high load
   - Memory leak detection
   - CPU profiling

## Migration Plan

1. **Rollout Strategy**:
   - Start with metrics disabled by default
   - Enable for specific endpoints first
   - Gradual rollout with sampling
   - Full enablement after validation

2. **Backward Compatibility**:
   - No breaking changes to existing APIs
   - Metrics endpoints are additive
   - Configuration is optional
   - Graceful degradation if metrics fail

## Success Criteria

1. **Functional**:
   - All API endpoints tracked
   - Metrics visible in configured backends
   - Historical data available
   - Alerting functioning

2. **Performance**:
   - < 1ms overhead per request
   - < 5% CPU increase
   - < 10MB memory overhead
   - No impact on p99 latency

3. **Operational**:
   - Dashboard adoption by teams
   - Reduced MTTR for API issues
   - Proactive issue detection
   - Improved capacity planning

## Risks and Mitigations

1. **Performance Impact**:
   - Risk: Metrics add latency
   - Mitigation: Async emission, sampling, circuit breaker

2. **Metric Cardinality**:
   - Risk: Too many unique metric names
   - Mitigation: Path normalization, aggregation

3. **Storage Growth**:
   - Risk: Database size explosion
   - Mitigation: Retention policies, compression

4. **Complexity**:
   - Risk: Hard to debug metrics issues
   - Mitigation: Comprehensive logging, health checks

## Timeline Estimate

- Phase 1 (Core Infrastructure): 1 week
- Phase 2 (Enhanced Collection): 1 week
- Phase 3 (Registry & Storage): 1 week
- Phase 4 (API Endpoints): 3 days
- Phase 5 (System Integration): 1 week
- Phase 6 (Optimization): 3 days
- Phase 7 (Monitoring): 3 days
- Phase 8 (Documentation): 3 days

**Total: ~5-6 weeks** for full implementation

## References

- [Airflow Metrics Documentation](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/logging-monitoring/metrics.html)
- [FastAPI Middleware](https://fastapi.tiangolo.com/tutorial/middleware/)
- [StatsD Best Practices](https://www.datadoghq.com/blog/statsd-performance-improvements/)
- [OpenTelemetry Metrics](https://opentelemetry.io/docs/concepts/signals/metrics/)
