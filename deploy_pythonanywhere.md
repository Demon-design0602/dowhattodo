# 🐍 PythonAnywhere Deployment Guide for Aura

## Why PythonAnywhere?
- ✅ **Free Tier Available** (No credit card required)
- ✅ **Easy Python Deployment**
- ✅ **Built-in File Manager**
- ✅ **Console Access**
- ✅ **Custom Domains** (paid plans)

## Step-by-Step Deployment

### 1. Create PythonAnywhere Account
1. Go to https://www.pythonanywhere.com
2. Click "Start running Python online in less than a minute!"
3. Create a **free account** (no credit card needed)
4. Choose "Beginner" plan (Free)

### 2. Upload Your Code

#### Option A: Using Git (Recommended)
```bash
# In PythonAnywhere console:
cd ~
git clone https://github.com/Demon-design0602/dowhattodo.git aura-new-site
cd aura-new-site
```

#### Option B: Using File Upload
1. Use PythonAnywhere File Manager
2. Upload your project files to `/home/yourusername/aura-new-site/`

### 3. Install Dependencies
```bash
# In PythonAnywhere console:
cd ~/aura-new-site
pip3.10 install --user -r backend/requirements.txt
```

### 4. Create Web App
1. Go to **Web** tab in PythonAnywhere dashboard
2. Click **"Add a new web app"**
3. Choose **"Manual configuration"**
4. Select **Python 3.10**
5. Click **"Next"**

### 5. Configure WSGI File
1. In the **Web** tab, find **"Code"** section
2. Click on **WSGI configuration file** link
3. Replace content with our `pythonanywhere_wsgi.py` content
4. Update `YOUR_USERNAME` with your actual username

### 6. Set Environment Variables
1. In **Web** tab, find **"Environment variables"** section
2. Add these variables:
   ```
   Name: GEMINI_API_KEY
   Value: your_actual_gemini_api_key
   
   Name: FLASK_ENV
   Value: production
   ```

### 7. Configure Static Files (Optional)
1. In **Web** tab, find **"Static files"** section
2. Add mapping:
   ```
   URL: /static/
   Directory: /home/yourusername/aura-new-site/public/
   ```

### 8. Update Frontend API URLs
Update the API endpoints in your frontend to point to PythonAnywhere:
- Your app will be at: `https://yourusername.pythonanywhere.com`

## Free Tier Limitations
- **CPU seconds:** 100 seconds/day
- **Disk space:** 512MB
- **One web app** only
- **Custom domains:** Not available (paid feature)

## Upgrade Options
- **Hacker Plan ($5/month):** More CPU, custom domains
- **Web Developer Plan ($12/month):** Even more resources

## Troubleshooting

### Common Issues:
1. **Import errors:** Check Python path in WSGI file
2. **Dependencies missing:** Reinstall with `--user` flag
3. **Environment variables:** Make sure they're set correctly
4. **CORS errors:** Check if CORS is properly configured

### Debugging:
1. Check **Error logs** in Web tab
2. Use **Console** for testing imports
3. Test individual components first

## Security Notes
- Don't commit `serviceAccountKey.json` to Git
- Upload Firebase credentials via File Manager
- Use environment variables for API keys

## Post-Deployment
1. Test your API endpoints
2. Update frontend URLs to point to PythonAnywhere
3. Test full application workflow
4. Monitor usage in dashboard
