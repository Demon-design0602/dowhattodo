#!/bin/bash

# 🔥 Firebase Deployment Script for Aura
echo "🔥 Deploying Aura to Firebase..."

# Check if firebase-tools is installed
if ! command -v firebase &> /dev/null; then
    echo "❌ Firebase CLI not found. Installing..."
    npm install -g firebase-tools
fi

# Check if user is logged in
echo "🔐 Checking Firebase authentication..."
firebase projects:list &> /dev/null
if [ $? -ne 0 ]; then
    echo "🔑 Please log in to Firebase:"
    firebase login
fi

# Deploy frontend only (backend goes to Render)
echo "🚀 Deploying frontend to Firebase Hosting..."
firebase deploy --only hosting

echo "✅ Frontend deployed to Firebase!"
echo "📍 Your app should be live at: https://image-95a5c.web.app"
echo ""
echo "📋 Next steps:"
echo "1. Deploy backend to Render.com using render.yaml"
echo "2. Add GEMINI_API_KEY environment variable to Render"
echo "3. Update API URLs if backend domain is different"
