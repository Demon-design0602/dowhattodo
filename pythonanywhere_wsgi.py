#!/usr/bin/env python3
"""
WSGI configuration for Aura application on PythonAnywhere
This file should be uploaded to your PythonAnywhere web app configuration
"""

import sys
import os

# Add your project directory to Python path
project_home = '/home/asasasas3434/aura-new-site'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Add the backend directory to the path
backend_path = os.path.join(project_home, 'backend')
if backend_path not in sys.path:
    sys.path = [backend_path] + sys.path

# Set environment variables for production
os.environ['FLASK_ENV'] = 'production'

# Import your Flask application
from backend.main import app as application

if __name__ == "__main__":
    application.run()
