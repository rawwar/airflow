#!/bin/bash
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

set -e

echo "🚀 Starting Apache Airflow Codespaces setup..."

# Install uv if not already installed
if ! command -v uv &> /dev/null; then
    echo "📦 Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="/root/.cargo/bin:$PATH"
    echo "export PATH=\"/root/.cargo/bin:\$PATH\"" >> ~/.bashrc
else
    echo "✅ uv is already installed"
fi

# Update package lists
echo "🔄 Updating package lists..."
apt-get update

# Navigate to workspace
cd /workspaces/airflow

# Create virtual environment
echo "🐍 Creating Python 3.11 virtual environment..."
uv venv .venv -p 3.11

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source .venv/bin/activate

# Install prek
echo "📋 Installing prek..."
uv tool install prek

# Install pre-commit hooks
echo "🪝 Installing pre-commit hooks..."
prek install -f
prek install -t pre-push

# Install Breeze
echo "💨 Installing Breeze..."
uv tool install -e ./dev/breeze

# Create airflow-breeze-config directory and environment file
echo "⚙️ Creating Airflow configuration..."
mkdir -p files/airflow-breeze-config
cat > files/airflow-breeze-config/environment_variables.env << EOF
AIRFLOW__CORE__SIMPLE_AUTH_MANAGER_ALL_ADMINS=True
AIRFLOW__API__EXPOSE_CONFIG=True
EOF

echo "✅ Setup completed successfully!"
echo "🎉 Your Apache Airflow development environment is ready!"
