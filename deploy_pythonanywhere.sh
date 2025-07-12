#!/bin/bash

# 🐍 PythonAnywhere Deployment Helper for Aura
echo "🐍 PythonAnywhere Deployment Helper"
echo "===================================="
echo ""

# Check if we have git
if ! command -v git &> /dev/null; then
    echo "❌ Git not found. Please install Git first."
    exit 1
fi

echo "📋 Deployment Steps for PythonAnywhere:"
echo ""
echo "1. 🔧 Update frontend API URLs for PythonAnywhere"
echo "2. 📦 Commit changes to GitHub"
echo "3. 📝 Generate deployment instructions"
echo "4. 🌐 Open PythonAnywhere website"
echo ""

read -p "🚀 Do you want to proceed? (y/n): " choice

if [[ $choice != "y" && $choice != "Y" ]]; then
    echo "❌ Deployment cancelled"
    exit 0
fi

echo ""
echo "🔧 Step 1: Updating frontend API URLs..."

# Ask for PythonAnywhere username
read -p "Enter your PythonAnywhere username: " PA_USERNAME

if [ -z "$PA_USERNAME" ]; then
    echo "❌ Username cannot be empty"
    exit 1
fi

# Update API URLs in JavaScript files
echo "📝 Updating analysis.js..."
sed -i "s|https://aura-new-site.onrender.com|https://${PA_USERNAME}.pythonanywhere.com|g" public/js/analysis.js

echo "📝 Updating history.js..."
sed -i "s|https://aura-new-site.onrender.com|https://${PA_USERNAME}.pythonanywhere.com|g" public/js/history.js

# Update WSGI file with username
echo "📝 Updating WSGI configuration..."
sed -i "s/YOUR_USERNAME/${PA_USERNAME}/g" pythonanywhere_wsgi.py

echo "✅ Frontend URLs updated for: https://${PA_USERNAME}.pythonanywhere.com"
echo ""

echo "📦 Step 2: Committing changes to GitHub..."
git add .
git commit -m "🐍 Configure for PythonAnywhere deployment

- Updated API URLs to point to ${PA_USERNAME}.pythonanywhere.com
- Added PythonAnywhere WSGI configuration
- Ready for PythonAnywhere deployment"

git push origin main
echo "✅ Changes pushed to GitHub"
echo ""

echo "📝 Step 3: Generating deployment instructions..."

cat > deployment_instructions.txt << EOF
🐍 AURA - PythonAnywhere Deployment Instructions
===============================================

Your PythonAnywhere URL will be: https://${PA_USERNAME}.pythonanywhere.com

STEP-BY-STEP DEPLOYMENT:

1. 🌐 Go to: https://www.pythonanywhere.com
2. 📝 Sign up for FREE account (no credit card needed)
3. 🖥️ Open Console and run:
   cd ~
   git clone https://github.com/Demon-design0602/dowhattodo.git aura-new-site
   cd aura-new-site
   pip3.10 install --user -r backend/requirements.txt

4. 🌐 Go to Web tab → Add new web app
5. ⚙️ Choose Manual configuration → Python 3.10
6. 📄 Edit WSGI file → Replace with content from pythonanywhere_wsgi.py
7. 🔧 Add Environment Variables:
   - GEMINI_API_KEY: your_actual_gemini_api_key
   - FLASK_ENV: production

8. 🚀 Reload web app
9. ✅ Test: https://${PA_USERNAME}.pythonanywhere.com

FRONTEND LOCATION: https://image-95a5c.web.app
BACKEND LOCATION: https://${PA_USERNAME}.pythonanywhere.com

For detailed instructions, see: deploy_pythonanywhere.md
EOF

echo "✅ Instructions saved to: deployment_instructions.txt"
echo ""

echo "🎉 READY FOR DEPLOYMENT!"
echo "========================"
echo ""
echo "📍 Your app URLs will be:"
echo "   🔥 Frontend: https://image-95a5c.web.app"
echo "   🐍 Backend:  https://${PA_USERNAME}.pythonanywhere.com"
echo ""
echo "📋 Next steps:"
echo "1. Go to https://www.pythonanywhere.com"
echo "2. Create free account"
echo "3. Follow instructions in: deployment_instructions.txt"
echo "4. Or read detailed guide: deploy_pythonanywhere.md"
echo ""

# Ask if user wants to open PythonAnywhere
read -p "🌐 Open PythonAnywhere website now? (y/n): " open_choice

if [[ $open_choice == "y" || $open_choice == "Y" ]]; then
    if command -v xdg-open &> /dev/null; then
        xdg-open "https://www.pythonanywhere.com" &
        echo "🌐 Opening PythonAnywhere..."
    else
        echo "🌐 Please open: https://www.pythonanywhere.com"
    fi
fi

echo ""
echo "🚀 Happy deploying!"
