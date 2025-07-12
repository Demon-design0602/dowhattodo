# 🚀 SUPER SIMPLE DEPLOYMENT - Just 5 Steps!

## What you're doing:
Making your photo analysis feature work by putting your code on a free website.

---

## STEP 1: Create Free Account (2 minutes)
1. Go to: **https://www.pythonanywhere.com**
2. Click the **big blue button** that says "Start running Python online"
3. Fill in:
   - Username: `deepanshu2025`
   - Email: your email
   - Password: make one up
4. Choose: **"Beginner (Free)"**
5. Click **"Create account"**

✅ **You now have a free account!**

---

## STEP 2: Get Your Code (3 minutes)
1. In PythonAnywhere, click **"Console"** (top menu)
2. Click **"Bash"** (opens a black window)
3. Copy this **EXACTLY** and paste it in the black window:

```bash
cd ~
git clone https://github.com/Demon-design0602/dowhattodo.git aura-new-site
cd aura-new-site
pip3.10 install --user -r backend/requirements.txt
```

4. Press **Enter** and wait (takes ~2 minutes)

✅ **Your code is now on PythonAnywhere!**

---

## STEP 3: Create Web App (2 minutes)
1. Click **"Web"** (top menu)
2. Click **"Add a new web app"**
3. Click **"Next"** (accept the free domain)
4. Choose **"Manual configuration"**
5. Choose **"Python 3.10"**
6. Click **"Next"**

✅ **Web app created!**

---

## STEP 4: Connect Your Code (3 minutes)
1. Find section called **"Code"**
2. Click the **WSGI configuration file** link
3. **DELETE everything** in that file
4. Copy and paste this **EXACTLY**:

```python
import sys
import os

project_home = '/home/deepanshu2025/aura-new-site'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

backend_path = os.path.join(project_home, 'backend')
if backend_path not in sys.path:
    sys.path = [backend_path] + sys.path

os.environ['FLASK_ENV'] = 'production'

from backend.main import app as application
```

5. Click **"Save"**

✅ **Code connected!**

---

## STEP 5: Add Secret Key (2 minutes)
1. Find section called **"Environment variables"**
2. Click **"Add new environment variable"**
3. Name: `GEMINI_API_KEY`
4. Value: `AIzaSyDgLtdBctXD81eHEKIH34NLNKvAqnpQQow`
5. Click **"Save"**
6. Add another one:
   - Name: `FLASK_ENV`
   - Value: `production`
7. Click **"Save"**

✅ **Secret keys added!**

---

## STEP 6: Start Your App (1 minute)
1. Find the **big green "Reload" button**
2. Click it
3. Wait for it to say "reloaded successfully"
4. Click your domain link: `https://deepanshu2025.pythonanywhere.com`

✅ **YOUR APP IS LIVE!**

---

## 🎉 TEST IT OUT:
1. Go to: **https://image-95a5c.web.app**
2. Click **"Analyze Your Photo"**
3. Upload any photo with a face
4. Watch the AI analyze it!

---

## ❓ If something doesn't work:
- Check the **error logs** in the Web tab
- Make sure you copied everything exactly
- The free account has limited usage per day

## 🎊 CONGRATULATIONS!
Your AI-powered facial symmetry analyzer is now live on the internet!
