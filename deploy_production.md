# 🚀 Aura - Production Deployment Guide

## Quick Deployment Options

### Option 1: Render.com (Recommended - Free Tier Available)

1. **Create Render.com Account:**
   - Visit https://render.com
   - Sign up with GitHub/Google

2. **Connect GitHub Repository:**
   - Push your code to GitHub first
   - Connect repository to Render

3. **Backend Deployment:**
   ```bash
   # Render will use these files automatically:
   - render.yaml (✅ Already configured)
   - backend/requirements.txt (✅ Ready)
   - backend/main.py (✅ Entry point)
   ```

4. **Environment Variables in Render:**
   ```
   GEMINI_API_KEY=your_actual_gemini_key
   FLASK_ENV=production
   ```

5. **Frontend Deployment:**
   - Deploy as static site pointing to `/public` folder
   - Or use Firebase Hosting (see Option 2)

### Option 2: Firebase Hosting (Google's Platform)

1. **Install Firebase CLI:**
   ```bash
   npm install -g firebase-tools
   firebase login
   ```

2. **Deploy Frontend:**
   ```bash
   firebase deploy --only hosting
   ```

3. **Backend on Cloud Run/Functions:**
   - Convert backend to Cloud Functions
   - Or deploy backend separately on Render

### Option 3: Vercel (Alternative)

1. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   vercel login
   ```

2. **Deploy:**
   ```bash
   vercel --prod
   ```

## Required Setup Before Deployment

### 1. Firebase Service Account (For History Feature)

1. Go to Firebase Console: https://console.firebase.google.com
2. Select project: `image-95a5c`
3. Go to Project Settings → Service Accounts
4. Generate new private key
5. Download as `serviceAccountKey.json`
6. Place in `backend/` folder

### 2. Environment Variables

Create `.env` file in backend/:
```
GEMINI_API_KEY=your_actual_gemini_api_key
FIREBASE_PROJECT_ID=image-95a5c
FLASK_ENV=production
```

### 3. Update API URLs

The frontend is configured to use:
- Local: `http://localhost:8080` 
- Production: `https://aura-new-site.onrender.com`

If deploying to different domain, update in:
- `public/js/analysis.js` (line 85-86)
- `public/js/history.js` (line 34)

## Quick Deploy Commands

I'll create automated scripts for each platform below...
