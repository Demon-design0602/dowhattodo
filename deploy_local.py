#!/usr/bin/env python3
"""
Local deployment script for Aura application
This script sets up and runs the Aura application locally for development/testing
"""

import os
import sys
import subprocess
import threading
import time
import webbrowser
from pathlib import Path

def print_banner():
    """Print application banner"""
    print("=" * 60)
    print("🌟 AURA - The Symmetry Score Application 🌟")
    print("=" * 60)
    print("Local Development Deployment")
    print("=" * 60)

def check_environment():
    """Check if virtual environment is activated"""
    if sys.prefix == sys.base_prefix:
        print("❌ Virtual environment not activated!")
        print("Please run: source venv/bin/activate")
        return False
    print("✅ Virtual environment is active")
    return True

def check_dependencies():
    """Check if all dependencies are installed"""
    try:
        import flask
        import firebase_admin
        import google.generativeai
        print("✅ All required dependencies found")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please run: pip install -r backend/requirements.txt")
        return False

def setup_environment():
    """Setup environment variables for local development"""
    print("🔧 Setting up environment variables...")
    
    # Set development mode
    os.environ['FLASK_ENV'] = 'development'
    os.environ['FLASK_DEBUG'] = 'True'
    
    # Check for API keys
    if 'GEMINI_API_KEY' not in os.environ:
        print("⚠️  GEMINI_API_KEY not found in environment")
        api_key = input("Enter your Gemini API key (or press Enter to skip): ").strip()
        if api_key:
            os.environ['GEMINI_API_KEY'] = api_key
        else:
            print("⚠️  Running without Gemini API - analysis features will be limited")
    else:
        print("✅ Gemini API key found")
    
    print("✅ Environment setup complete")

def start_backend():
    """Start the Flask backend server"""
    print("🚀 Starting backend server...")
    os.chdir("backend")
    
    # Use Python directly instead of gunicorn for development
    process = subprocess.Popen([
        sys.executable, "main.py"
    ], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    
    return process

def start_frontend():
    """Start a simple HTTP server for frontend"""
    print("🌐 Starting frontend server...")
    os.chdir("../public")
    
    # Start a simple HTTP server
    process = subprocess.Popen([
        sys.executable, "-m", "http.server", "3000"
    ], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    
    return process

def monitor_process(process, name):
    """Monitor a process and print its output"""
    for line in process.stdout:
        print(f"[{name}] {line.strip()}")

def main():
    """Main deployment function"""
    print_banner()
    
    # Change to project directory
    project_dir = Path(__file__).parent
    os.chdir(project_dir)
    
    # Pre-flight checks
    if not check_environment():
        sys.exit(1)
    
    if not check_dependencies():
        sys.exit(1)
    
    # Setup environment
    setup_environment()
    
    try:
        # Start backend
        backend_process = start_backend()
        
        # Give backend time to start
        time.sleep(3)
        
        # Start frontend
        frontend_process = start_frontend()
        
        # Give frontend time to start
        time.sleep(2)
        
        print("\n" + "=" * 60)
        print("🎉 AURA APPLICATION DEPLOYED SUCCESSFULLY!")
        print("=" * 60)
        print("📍 Frontend: http://localhost:3000")
        print("📍 Backend:  http://localhost:8080") 
        print("=" * 60)
        print("Press Ctrl+C to stop both servers")
        print("=" * 60)
        
        # Open browser
        try:
            webbrowser.open("http://localhost:3000")
        except:
            pass
        
        # Monitor both processes
        backend_thread = threading.Thread(
            target=monitor_process, 
            args=(backend_process, "BACKEND"),
            daemon=True
        )
        frontend_thread = threading.Thread(
            target=monitor_process, 
            args=(frontend_process, "FRONTEND"),
            daemon=True
        )
        
        backend_thread.start()
        frontend_thread.start()
        
        # Wait for processes
        while True:
            if backend_process.poll() is not None:
                print("❌ Backend process terminated")
                break
            if frontend_process.poll() is not None:
                print("❌ Frontend process terminated") 
                break
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n🛑 Shutting down servers...")
        
        if 'backend_process' in locals():
            backend_process.terminate()
        if 'frontend_process' in locals():
            frontend_process.terminate()
            
        print("✅ Servers stopped successfully")
        
    except Exception as e:
        print(f"❌ Error during deployment: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
