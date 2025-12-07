# Deployment Guide

## Render Deployment

### Prerequisites
- GitHub account
- Render account (free tier available)

### Steps

1. **Push to GitHub**
```bash
git init
git add .
git commit -m "added image analysis feature"
git branch -M v2
git remote add origin <your-repo-url>
git push -u origin v2
```

2. **Deploy Backend on Render**
- Go to Render Dashboard
- Click "New +" → "Web Service"
- Connect your GitHub repository
- Select branch: `v2`
- Configure:
  - Name: `suart-backend`
  - Environment: `Docker`
  - Dockerfile Path: `./Dockerfile`
  - Plan: Free
  - Health Check Path: `/health`
- Click "Create Web Service"

3. **Deploy Frontend on Render**
- Click "New +" → "Static Site"
- Connect same repository
- Configure:
  - Name: `suart-frontend`
  - Build Command: `cd react-interface && npm install && npm run build`
  - Publish Directory: `react-interface/build`
- Click "Create Static Site"

4. **Update Frontend API URL**
- After backend deploys, copy the backend URL
- Update `react-interface/src/App.jsx`:
  - Replace `http://127.0.0.1:8001` with your backend URL
- Commit and push changes

### Important Notes

**Backend:**
- First deployment takes 10-15 minutes (model downloads)
- Requires 2GB+ RAM (upgrade from free tier if needed)
- Models cached after first run

**Frontend:**
- Builds in 2-3 minutes
- Served as static files
- Update CORS in backend to allow frontend domain

**Free Tier Limitations:**
- Backend sleeps after 15 minutes of inactivity
- First request after sleep takes 30-60 seconds
- 750 hours/month free

### Environment Variables (Optional)

Backend:
- `PORT`: 8001 (auto-set by Render)
- `PYTHON_VERSION`: 3.11.0

### Troubleshooting

**Backend won't start:**
- Check logs for model download progress
- Ensure 2GB+ RAM available
- Verify Dockerfile builds locally first

**Frontend can't connect:**
- Update API URL in App.jsx
- Check CORS settings in backend
- Verify backend health endpoint responds

**Models not loading:**
- First run downloads 3GB of models
- Check disk space and RAM
- May need to upgrade from free tier

### Local Testing with Docker

```bash
# Build
docker build -t suart-backend .

# Run
docker run -p 8001:8001 suart-backend

# Test
curl http://localhost:8001/health
```

### Production Recommendations

- Use paid tier for backend (512MB RAM minimum)
- Enable auto-scaling for high traffic
- Set up monitoring and alerts
- Use CDN for frontend assets
- Implement rate limiting
- Add authentication for API
