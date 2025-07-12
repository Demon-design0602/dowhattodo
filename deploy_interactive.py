#!/usr/bin/env python3
"""
Interactive Deployment Helper for Aura on PythonAnywhere
This script will guide you through each step of deployment
"""

import os
import webbrowser
import time
import sys

def print_banner():
    print("🐍" * 50)
    print("    AURA - Interactive PythonAnywhere Deployment")
    print("🐍" * 50)
    print()

def print_step(step_num, title, description=""):
    print(f"📋 STEP {step_num}: {title}")
    if description:
        print(f"   {description}")
    print()

def wait_for_user(message="Press Enter when ready to continue..."):
    input(f"⏳ {message}")
    print()

def open_url(url, description):
    print(f"🌐 Opening: {url}")
    try:
        webbrowser.open(url)
        print(f"✅ {description}")
    except:
        print(f"❌ Could not open browser. Please manually go to: {url}")
    print()

def check_completion(step_description):
    while True:
        response = input(f"✅ Have you completed: {step_description}? (y/n): ").lower()
        if response in ['y', 'yes']:
            print("✅ Great! Moving to next step...")
            print()
            break
        elif response in ['n', 'no']:
            print("⏳ Please complete this step before continuing.")
            print()
        else:
            print("❌ Please answer 'y' for yes or 'n' for no")

def main():
    print_banner()
    
    print("🎯 DEPLOYMENT OVERVIEW:")
    print("   📍 Frontend: Already LIVE at https://image-95a5c.web.app")
    print("   📍 Backend: Will be deployed to https://deepanshu2025.pythonanywhere.com")
    print("   💡 Total time: ~10-15 minutes")
    print()
    
    wait_for_user("Ready to start deployment?")
    
    # Step 1: Create Account
    print_step(1, "Create PythonAnywhere Account", 
               "Free account, no credit card required")
    
    open_url("https://www.pythonanywhere.com", "Opening PythonAnywhere website")
    
    print("📝 Account Creation Steps:")
    print("   1. Click 'Start running Python online in less than a minute!'")
    print("   2. Fill in your details (use username: deepanshu2025)")
    print("   3. Choose 'Beginner' (Free) plan")
    print("   4. Verify your email if required")
    print()
    
    check_completion("creating your PythonAnywhere account")
    
    # Step 2: Clone Repository
    print_step(2, "Clone Your Code Repository",
               "Get your code onto PythonAnywhere")
    
    print("📋 In PythonAnywhere Dashboard:")
    print("   1. Click on 'Console' tab")
    print("   2. Click 'Bash' to open a new console")
    print("   3. Copy and paste these commands:")
    print()
    print("   " + "="*50)
    print("   cd ~")
    print("   git clone https://github.com/Demon-design0602/dowhattodo.git aura-new-site")
    print("   cd aura-new-site")
    print("   pip3.10 install --user -r backend/requirements.txt")
    print("   " + "="*50)
    print()
    
    check_completion("cloning the repository and installing dependencies")
    
    # Step 3: Create Web App
    print_step(3, "Create Web Application",
               "Set up the web app configuration")
    
    print("📋 In PythonAnywhere Dashboard:")
    print("   1. Click on 'Web' tab")
    print("   2. Click 'Add a new web app'")
    print("   3. Choose your domain (deepanshu2025.pythonanywhere.com)")
    print("   4. Select 'Manual configuration'")
    print("   5. Choose 'Python 3.10'")
    print("   6. Click 'Next'")
    print()
    
    check_completion("creating the web app")
    
    # Step 4: Configure WSGI
    print_step(4, "Configure WSGI File",
               "Connect your Flask app to the web server")
    
    print("📋 In the Web tab:")
    print("   1. Find 'Code' section")
    print("   2. Click on the WSGI configuration file link")
    print("   3. DELETE all existing content")
    print("   4. Copy content from 'pythonanywhere_wsgi.py' file")
    print()
    
    # Display WSGI content
    try:
        with open('pythonanywhere_wsgi.py', 'r') as f:
            wsgi_content = f.read()
        
        print("📄 WSGI File Content to Copy:")
        print("   " + "="*50)
        print(wsgi_content)
        print("   " + "="*50)
        print()
    except:
        print("❌ Could not read WSGI file. Please check pythonanywhere_wsgi.py")
    
    check_completion("updating the WSGI configuration file")
    
    # Step 5: Environment Variables
    print_step(5, "Add Environment Variables",
               "Configure your API keys")
    
    print("📋 In the Web tab:")
    print("   1. Find 'Environment variables' section")
    print("   2. Add these variables:")
    print("      Name: GEMINI_API_KEY")
    print("      Value: AIzaSyDgLtdBctXD81eHEKIH34NLNKvAqnpQQow")
    print()
    print("      Name: FLASK_ENV")
    print("      Value: production")
    print()
    
    check_completion("adding environment variables")
    
    # Step 6: Reload and Test
    print_step(6, "Reload and Test",
               "Start your application")
    
    print("📋 Final steps:")
    print("   1. Click the green 'Reload' button")
    print("   2. Wait for reload to complete")
    print("   3. Click on your domain link to test")
    print()
    
    check_completion("reloading the web app")
    
    # Final Testing
    print("🎉" * 25)
    print("    DEPLOYMENT COMPLETE!")
    print("🎉" * 25)
    print()
    
    print("🌐 Your Application URLs:")
    print("   🔥 Frontend: https://image-95a5c.web.app")
    print("   🐍 Backend:  https://deepanshu2025.pythonanywhere.com")
    print()
    
    print("✅ Testing Steps:")
    print("   1. Visit your frontend: https://image-95a5c.web.app")
    print("   2. Try uploading a photo for analysis")
    print("   3. Check if the analysis works")
    print("   4. Test the history feature (if signed in)")
    print()
    
    # Open both URLs for testing
    test_choice = input("🧪 Open both URLs for testing? (y/n): ").lower()
    if test_choice in ['y', 'yes']:
        open_url("https://image-95a5c.web.app", "Opening Frontend")
        time.sleep(2)
        open_url("https://deepanshu2025.pythonanywhere.com", "Opening Backend")
    
    print()
    print("🎊 Congratulations! Your Aura application is now live!")
    print("📋 If you encounter any issues, check the error logs in PythonAnywhere Web tab")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Deployment interrupted")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        sys.exit(1)
