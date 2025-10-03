apt-get update

# Navigate to workspace
cd /workspaces/airflow

# Create virtual environment
echo "🐍 Creating Python 3.11 virtual environment..."
uv venv .venv -p 3.11

# Activate virtual environment
echo "Activating virtual environment..."
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

# Prompt for GitHub username and email, then set them globally
read -p "Enter your GitHub username: " github_username
read -p "Enter your GitHub email: " github_email

git config --global user.name "$github_username"
git config --global user.email "$github_email"

echo "🔧 Git global config set for user.name and user.email."
echo "✅ Setup completed successfully!"
echo "🎉 Your Apache Airflow development environment is ready!"
