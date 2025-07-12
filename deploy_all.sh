#!/bin/bash

# 🌟 Aura - Complete Deployment Helper
echo "=================================="
echo "🌟 AURA DEPLOYMENT HELPER"
echo "=================================="
echo ""

# Check requirements
echo "🔍 Checking requirements..."

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git not found. Please install Git first."
    exit 1
fi

# Check if node/npm is available for Firebase CLI
if ! command -v npm &> /dev/null; then
    echo "⚠️  NPM not found. Firebase deployment will be skipped."
    FIREBASE_AVAILABLE=false
else
    FIREBASE_AVAILABLE=true
fi

echo ""
echo "📋 Deployment Options:"
echo "1. 🐙 Setup GitHub repository (Required for Render)"
echo "2. 🔥 Deploy to Firebase Hosting (Frontend only)"
echo "3. 📊 Show deployment status"
echo "4. 🛠️ Setup production environment"
echo "5. 📱 Deploy everything (GitHub + Firebase)"
echo ""

read -p "Choose option (1-5): " choice

case $choice in
    1)
        echo "🐙 Setting up GitHub..."
        chmod +x setup_github.sh
        ./setup_github.sh
        ;;
    2)
        if [ "$FIREBASE_AVAILABLE" = true ]; then
            echo "🔥 Deploying to Firebase..."
            chmod +x deploy_firebase.sh
            ./deploy_firebase.sh
        else
            echo "❌ NPM not available. Please install Node.js first."
        fi
        ;;
    3)
        echo "📊 Current Status:"
        echo ""
        echo "📁 Local Files:"
        echo "  ✅ Frontend: public/ folder ready"
        echo "  ✅ Backend: backend/ folder ready"
        echo "  ✅ Config: firebase.json, render.yaml ready"
        echo ""
        
        if [ -d ".git" ]; then
            echo "  ✅ Git initialized"
        else
            echo "  ❌ Git not initialized"
        fi
        
        if git remote get-url origin &> /dev/null; then
            echo "  ✅ GitHub remote configured"
            echo "  📡 Remote: $(git remote get-url origin)"
        else
            echo "  ❌ No GitHub remote found"
        fi
        
        echo ""
        echo "🔗 Deployment URLs:"
        echo "  🔥 Firebase: https://image-95a5c.web.app (if deployed)"
        echo "  🚀 Render: https://aura-new-site.onrender.com (if deployed)"
        ;;
    4)
        echo "🛠️ Setting up production environment..."
        echo ""
        echo "📋 Required Environment Variables:"
        echo "   GEMINI_API_KEY=your_actual_api_key"
        echo "   FLASK_ENV=production"
        echo ""
        echo "📋 Required Files:"
        echo "   backend/serviceAccountKey.json (Firebase credentials)"
        echo ""
        echo "🔧 Platform Setup Instructions:"
        echo ""
        echo "🚀 For Render.com:"
        echo "   1. Go to https://render.com"
        echo "   2. Connect GitHub repository"
        echo "   3. Create new Web Service"
        echo "   4. Use: render.yaml configuration"
        echo "   5. Add environment variables"
        echo ""
        echo "🔥 For Firebase:"
        echo "   1. Firebase project already configured"
        echo "   2. Run: ./deploy_firebase.sh"
        echo ""
        ;;
    5)
        echo "🚀 Deploying everything..."
        echo ""
        echo "Step 1: GitHub Setup"
        chmod +x setup_github.sh
        ./setup_github.sh
        echo ""
        echo "Step 2: Firebase Deployment"
        if [ "$FIREBASE_AVAILABLE" = true ]; then
            chmod +x deploy_firebase.sh
            ./deploy_firebase.sh
        else
            echo "❌ Skipping Firebase (NPM not available)"
        fi
        echo ""
        echo "🎉 Deployment complete!"
        echo "📋 Manual steps remaining:"
        echo "   1. Setup Render.com for backend"
        echo "   2. Add Firebase serviceAccountKey.json"
        echo "   3. Configure environment variables"
        ;;
    *)
        echo "❌ Invalid option"
        ;;
esac

echo ""
echo "📖 For detailed instructions, see: deploy_production.md"
