#!/bin/bash

# 🐙 GitHub Setup Script for Aura
echo "🐙 Setting up GitHub repository for Aura..."

# Initialize git if not already done
if [ ! -d ".git" ]; then
    echo "📁 Initializing Git repository..."
    git init
fi

# Create .gitignore if it doesn't exist
if [ ! -f ".gitignore" ]; then
    echo "📝 Creating .gitignore..."
    cat > .gitignore << EOF
# Environment variables
.env
backend/.env

# Firebase credentials (security)
backend/serviceAccountKey.json

# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
venv/
env/
.venv/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log
pglite-debug.log

# Firebase
.firebase/
firebase-debug.log
EOF
fi

# Stage all files
echo "📦 Staging files..."
git add .

# Commit
echo "💾 Creating commit..."
git commit -m "🚀 Initial commit - Aura Symmetry Score Application

Features:
- AI-powered facial symmetry analysis
- Firebase authentication and storage
- Responsive modern UI
- Local development support
- Production deployment ready"

# Check if remote exists
if ! git remote get-url origin &> /dev/null; then
    echo "📡 No remote repository found."
    echo "Please create a GitHub repository and run:"
    echo "git remote add origin https://github.com/YOUR_USERNAME/aura-new-site.git"
    echo "git branch -M main"
    echo "git push -u origin main"
else
    echo "🚀 Pushing to GitHub..."
    git push -u origin main
fi

echo "✅ GitHub setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Go to https://render.com"
echo "2. Connect your GitHub repository"
echo "3. Deploy using the render.yaml configuration"
