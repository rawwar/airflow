# 88 Containerization

## Overview

Running Airflow in containers provides consistent environments, simplified deployment, and cloud-native integration. Airflow 3.x has enhanced container support with improved Docker images, Kubernetes operators, and container orchestration patterns.

## Airflow 3.x Notes
- Official Docker image improvements
- Multi-stage build support
- Improved Kubernetes integration
- Container-optimized configurations
- Enhanced debugging in containers

---

# 88.1 Docker Fundamentals

## Overview
Building and running Airflow Docker containers.

## Tasks

### - [ ] 88.1.1 Official Airflow Docker Image
Filename: `88_01_01_official_docker_image.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Use official Airflow images

- [ ] Image tags and versions
- [ ] Image variants (slim, full)
- [ ] Environment configuration
- [ ] Basic docker run commands

**Expected Behavior**: Official image runs correctly

---

### - [ ] 88.1.2 Custom Airflow Dockerfile
Filename: `88_01_02_custom_dockerfile.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Build custom Airflow images

- [ ] Extending official image
- [ ] Adding Python packages
- [ ] System dependencies
- [ ] Custom configurations

**Expected Behavior**: Custom image builds successfully

---

### - [ ] 88.1.3 Multi-Stage Docker Builds
Filename: `88_01_03_multi_stage_builds.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Optimize image size with multi-stage

- [ ] Build stage for dependencies
- [ ] Runtime stage optimization
- [ ] Separating dev/prod images
- [ ] Cache layer optimization

**Expected Behavior**: Smaller optimized images

---

### - [ ] 88.1.4 Docker Compose Development Setup
Filename: `88_01_04_docker_compose_dev.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Local development with Docker Compose

- [ ] Service definitions
- [ ] Volume mounts for DAGs
- [ ] Environment variables
- [ ] Hot reload configuration

**Expected Behavior**: Local dev environment works

---

### - [ ] 88.1.5 Docker Compose Production Setup
Filename: `88_01_05_docker_compose_prod.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Production-like Docker Compose

- [ ] Multiple workers
- [ ] External database
- [ ] Redis/Celery configuration
- [ ] Resource limits

**Expected Behavior**: Production-like local setup

---

# 88.2 Container Configuration

## Overview
Configuring Airflow containers properly.

## Tasks

### - [ ] 88.2.1 Environment Variable Configuration
Filename: `88_02_01_env_configuration.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Configure via environment

- [ ] AIRFLOW__ prefix convention
- [ ] Connection URIs
- [ ] Executor configuration
- [ ] Feature flags

**Expected Behavior**: Config via env works

---

### - [ ] 88.2.2 Secrets in Containers
Filename: `88_02_02_container_secrets.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Secure secret handling

- [ ] Docker secrets
- [ ] Kubernetes secrets
- [ ] _CMD and _SECRET suffixes
- [ ] Secret file mounting

**Expected Behavior**: Secrets handled securely

---

### - [ ] 88.2.3 Volume Configuration
Filename: `88_02_03_volume_configuration.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure container volumes

- [ ] DAG folder mounts
- [ ] Log persistence
- [ ] Plugin volumes
- [ ] Configuration file mounts

**Expected Behavior**: Volumes properly mounted

---

### - [ ] 88.2.4 Container Networking
Filename: `88_02_04_container_networking.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure container networking

- [ ] Service discovery
- [ ] Port exposure
- [ ] Internal networking
- [ ] External access

**Expected Behavior**: Networking works correctly

---

### - [ ] 88.2.5 Resource Limits and Requests
Filename: `88_02_05_resource_limits.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Set container resources

- [ ] CPU limits/requests
- [ ] Memory limits/requests
- [ ] Per-component sizing
- [ ] OOM killer configuration

**Expected Behavior**: Resources properly allocated

---

# 88.3 Kubernetes Deployment

## Overview
Deploying Airflow on Kubernetes.

## Tasks

### - [ ] 88.3.1 Helm Chart Deployment
Filename: `88_03_01_helm_deployment.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Deploy with official Helm chart

- [ ] Helm chart installation
- [ ] values.yaml customization
- [ ] Upgrade procedures
- [ ] Chart versioning

**Expected Behavior**: Helm deployment successful

---

### - [ ] 88.3.2 Kubernetes Manifests
Filename: `88_03_02_k8s_manifests.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Raw Kubernetes manifests

- [ ] Deployment definitions
- [ ] Service configurations
- [ ] ConfigMaps and Secrets
- [ ] Ingress setup

**Expected Behavior**: Manifests deploy correctly

---

### - [ ] 88.3.3 Pod Template Configuration
Filename: `88_03_03_pod_templates.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure pod templates

- [ ] Worker pod templates
- [ ] Scheduler pod template
- [ ] Webserver pod template
- [ ] Init containers

**Expected Behavior**: Pod templates applied

---

### - [ ] 88.3.4 Service Account Configuration
Filename: `88_03_04_service_accounts.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure K8s service accounts

- [ ] RBAC configuration
- [ ] Pod creation permissions
- [ ] Namespace access
- [ ] Cloud provider integration

**Expected Behavior**: Permissions work correctly

---

### - [ ] 88.3.5 Persistent Volume Setup
Filename: `88_03_05_persistent_volumes.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure persistent storage

- [ ] PVC for logs
- [ ] DAG storage options
- [ ] Shared storage patterns
- [ ] Storage class selection

**Expected Behavior**: Persistent storage works

---

# 88.4 Container Image Management

## Overview
Managing container images for Airflow.

## Tasks

### - [ ] 88.4.1 Image Registry Setup
Filename: `88_04_01_image_registry.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure container registries

- [ ] Docker Hub usage
- [ ] Private registry setup
- [ ] Cloud registries (ECR, GCR, ACR)
- [ ] Image pull secrets

**Expected Behavior**: Registry access works

---

### - [ ] 88.4.2 Image Versioning Strategy
Filename: `88_04_02_image_versioning.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Version container images

- [ ] Semantic versioning
- [ ] Git SHA tagging
- [ ] Environment-specific tags
- [ ] Latest tag management

**Expected Behavior**: Images versioned properly

---

### - [ ] 88.4.3 Image Security Scanning
Filename: `88_04_03_image_scanning.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Scan images for vulnerabilities

- [ ] Trivy scanning
- [ ] Snyk integration
- [ ] CI/CD scanning
- [ ] Vulnerability remediation

**Expected Behavior**: Images scanned regularly

---

### - [ ] 88.4.4 Base Image Updates
Filename: `88_04_04_base_image_updates.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Manage base image updates

- [ ] Automated rebuild triggers
- [ ] Dependency updates
- [ ] Security patches
- [ ] Testing updated images

**Expected Behavior**: Images updated regularly

---

### - [ ] 88.4.5 Image Size Optimization
Filename: `88_04_05_image_optimization.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Minimize image size

- [ ] Layer optimization
- [ ] Removing unnecessary files
- [ ] Alpine vs Debian tradeoffs
- [ ] Build cache strategies

**Expected Behavior**: Images optimized for size

---

# 88.5 Container Debugging

## Overview
Debugging containerized Airflow.

## Tasks

### - [ ] 88.5.1 Container Log Access
Filename: `88_05_01_container_logs.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Access container logs

- [ ] docker logs command
- [ ] kubectl logs command
- [ ] Log streaming
- [ ] Multi-container logging

**Expected Behavior**: Logs accessible

---

### - [ ] 88.5.2 Container Shell Access
Filename: `88_05_02_container_shell.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Interactive shell access

- [ ] docker exec commands
- [ ] kubectl exec commands
- [ ] Debugging tools installation
- [ ] Ephemeral containers

**Expected Behavior**: Shell access works

---

### - [ ] 88.5.3 Container Health Checks
Filename: `88_05_03_container_health.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure health checks

- [ ] Liveness probes
- [ ] Readiness probes
- [ ] Startup probes
- [ ] Health check endpoints

**Expected Behavior**: Health checks configured

---

### - [ ] 88.5.4 Container Resource Monitoring
Filename: `88_05_04_resource_monitoring.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Monitor container resources

- [ ] CPU/memory usage
- [ ] Container metrics
- [ ] cAdvisor integration
- [ ] Resource alerts

**Expected Behavior**: Resources monitored

---

### - [ ] 88.5.5 Common Container Issues
Filename: `88_05_05_common_issues.py` | Tags: `['reference', 'core', 'intermediate', 'failure']`

**Purpose**: Troubleshoot common problems

- [ ] OOMKilled debugging
- [ ] CrashLoopBackOff diagnosis
- [ ] ImagePullBackOff fixes
- [ ] Permission issues

**Expected Behavior**: Issues diagnosed and fixed

---

# 88.6 Anti-Patterns and Common Mistakes

## Overview
Avoiding containerization pitfalls.

## Tasks

### - [ ] 88.6.1 Running as Root
Filename: `88_06_01_running_as_root.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Use non-root containers

- [ ] Security risks
- [ ] Volume permission issues
- [ ] Non-root user setup
- [ ] Security contexts

**Expected Behavior**: Non-root containers

---

### - [ ] 88.6.2 Latest Tag Usage
Filename: `88_06_02_latest_tag.py` | Tags: `['reference', 'anti-pattern', 'beginner', 'failure']`

**Purpose**: Pin image versions

- [ ] Reproducibility issues
- [ ] Unexpected updates
- [ ] Version pinning
- [ ] Tag strategies

**Expected Behavior**: Versions pinned

---

### - [ ] 88.6.3 Fat Container Images
Filename: `88_06_03_fat_images.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Minimize image size

- [ ] Bloated images
- [ ] Long pull times
- [ ] Storage costs
- [ ] Optimization techniques

**Expected Behavior**: Images optimized

---

### - [ ] 88.6.4 Missing Health Probes
Filename: `88_06_04_missing_probes.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Configure health checks

- [ ] No liveness probe
- [ ] No readiness probe
- [ ] Hung containers
- [ ] Proper probe config

**Expected Behavior**: Probes configured

---

### - [ ] 88.6.5 Hardcoded Configuration
Filename: `88_06_05_hardcoded_config.py` | Tags: `['reference', 'anti-pattern', 'beginner', 'failure']`

**Purpose**: Externalize configuration

- [ ] Config in image
- [ ] Rebuild for changes
- [ ] Environment variables
- [ ] ConfigMaps/Secrets

**Expected Behavior**: Config externalized

---

# 88.7 Testing Containerized Airflow

## Overview
Testing container configurations.

## Tasks

### - [ ] 88.7.1 Container Build Testing
Filename: `88_07_01_build_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test image builds

- [ ] Build validation
- [ ] Layer caching
- [ ] Size verification
- [ ] Security scanning

**Expected Behavior**: Builds tested

---

### - [ ] 88.7.2 Container Startup Testing
Filename: `88_07_02_startup_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test container startup

- [ ] Startup time
- [ ] Configuration loading
- [ ] Dependency availability
- [ ] Health check pass

**Expected Behavior**: Startup tested

---

### - [ ] 88.7.3 Container Integration Testing
Filename: `88_07_03_integration_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test container integration

- [ ] Service connectivity
- [ ] Database connection
- [ ] Inter-container comm
- [ ] End-to-end tests

**Expected Behavior**: Integration tested

---

### - [ ] 88.7.4 Kubernetes Manifest Testing
Filename: `88_07_04_manifest_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test K8s manifests

- [ ] Kubeval validation
- [ ] Conftest policies
- [ ] Dry-run testing
- [ ] Schema validation

**Expected Behavior**: Manifests valid

---

### - [ ] 88.7.5 Helm Chart Testing
Filename: `88_07_05_helm_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test Helm charts

- [ ] helm lint
- [ ] helm template
- [ ] Chart testing framework
- [ ] Values validation

**Expected Behavior**: Charts tested

---

# 88.8 Performance Optimization

## Overview
Optimizing container performance.

## Tasks

### - [ ] 88.8.1 Container Startup Optimization
Filename: `88_08_01_startup_optimization.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Speed up startup

- [ ] Minimal init process
- [ ] Lazy loading
- [ ] Parallel startup
- [ ] Pre-warming

**Expected Behavior**: Fast startup

---

### - [ ] 88.8.2 Image Layer Optimization
Filename: `88_08_02_layer_optimization.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Optimize image layers

- [ ] Layer ordering
- [ ] Cache utilization
- [ ] Multi-stage builds
- [ ] Layer squashing

**Expected Behavior**: Layers optimized

---

### - [ ] 88.8.3 Resource Request Tuning
Filename: `88_08_03_resource_tuning.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Right-size resources

- [ ] CPU tuning
- [ ] Memory tuning
- [ ] QoS classes
- [ ] Resource monitoring

**Expected Behavior**: Resources right-sized

---

### - [ ] 88.8.4 Network Optimization
Filename: `88_08_04_network_optimization.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Optimize container networking

- [ ] DNS caching
- [ ] Connection pooling
- [ ] Service mesh tuning
- [ ] Network policies

**Expected Behavior**: Network optimized

---

### - [ ] 88.8.5 Storage Optimization
Filename: `88_08_05_storage_optimization.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Optimize container storage

- [ ] Volume performance
- [ ] Storage class selection
- [ ] Cache volumes
- [ ] Ephemeral storage

**Expected Behavior**: Storage optimized

---

# 88.9 Advanced Container Patterns

## Overview
Advanced containerization patterns.

## Tasks

### - [ ] 88.9.1 Sidecar Patterns for Airflow
Filename: `88_09_01_sidecar_patterns.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Implement sidecars

- [ ] Log shipping sidecar
- [ ] Secrets injection
- [ ] git-sync sidecar
- [ ] Proxy sidecar

**Expected Behavior**: Sidecars working

---

### - [ ] 88.9.2 Init Container Patterns
Filename: `88_09_02_init_patterns.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Use init containers

- [ ] Dependency wait
- [ ] Configuration setup
- [ ] Migration runners
- [ ] Permission setup

**Expected Behavior**: Init containers work

---

### - [ ] 88.9.3 Distroless and Minimal Images
Filename: `88_09_03_minimal_images.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Ultra-minimal containers

- [ ] Distroless base
- [ ] Scratch images
- [ ] Security benefits
- [ ] Debugging challenges

**Expected Behavior**: Minimal images work

---

### - [ ] 88.9.4 Multi-Architecture Images
Filename: `88_09_04_multi_arch.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Support multiple architectures

- [ ] ARM64 support
- [ ] buildx usage
- [ ] Manifest lists
- [ ] CI/CD integration

**Expected Behavior**: Multi-arch works

---

### - [ ] 88.9.5 Rootless Containers
Filename: `88_09_05_rootless_containers.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Fully rootless setup

- [ ] User namespaces
- [ ] Rootless podman/docker
- [ ] Security hardening
- [ ] Compatibility issues

**Expected Behavior**: Rootless works

---

# 88.10 Real-World Examples

## Overview
Production container implementations.

## Tasks

### - [ ] 88.10.1 Production Docker Compose
Filename: `88_10_01_production_compose.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Production-ready compose

- [ ] All services configured
- [ ] Resource limits
- [ ] Health checks
- [ ] Logging setup

**Expected Behavior**: Production compose works

---

### - [ ] 88.10.2 Minimal Custom Dockerfile
Filename: `88_10_02_minimal_dockerfile.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Optimized custom image

- [ ] Multi-stage build
- [ ] Dependency caching
- [ ] Security hardening
- [ ] Minimal size

**Expected Behavior**: Optimized image builds

---

### - [ ] 88.10.3 Enterprise Helm Deployment
Filename: `88_10_03_enterprise_helm.py` | Tags: `['reference', 'example', 'advanced', 'success']`

**Purpose**: Enterprise Helm setup

- [ ] Complete values.yaml
- [ ] Security configuration
- [ ] Resource allocation
- [ ] Integration settings

**Expected Behavior**: Enterprise Helm works

---

### - [ ] 88.10.4 GitOps Container Pipeline
Filename: `88_10_04_gitops_pipeline.py` | Tags: `['reference', 'example', 'advanced', 'success']`

**Purpose**: Container GitOps

- [ ] Image build pipeline
- [ ] Automated deployment
- [ ] Version promotion
- [ ] Rollback procedures

**Expected Behavior**: GitOps pipeline works

---

### - [ ] 88.10.5 Air-Gapped Deployment
Filename: `88_10_05_air_gapped.py` | Tags: `['reference', 'example', 'advanced', 'success']`

**Purpose**: Deploy without internet

- [ ] Private registry
- [ ] Image mirroring
- [ ] Offline dependencies
- [ ] Update procedures

**Expected Behavior**: Air-gapped works

---

# Summary

## Topic Completion Checklist
- [ ] Docker fundamentals covered
- [ ] Container configuration documented
- [ ] Kubernetes deployment explained
- [ ] Image management included
- [ ] Debugging guidance provided
- [ ] Anti-patterns identified
- [ ] Testing strategies covered
- [ ] Performance optimization included
- [ ] Advanced patterns documented
- [ ] Real-world examples included

## Related Topics
- Section 76: Kubernetes Operators (K8s tasks)
- Section 85: Deployment Patterns (deployment)
- Section 89: CI/CD Integration (automation)
- Section 35: Executors (container executors)

## Notes for Implementation
- Include Dockerfile examples
- Show docker-compose files
- Provide Helm values examples
- Demonstrate debugging commands
