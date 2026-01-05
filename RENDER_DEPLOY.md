# Deploying to Render

This guide will help you deploy the AI Content Humanizer to Render.

## Prerequisites

1. A Render account (sign up at https://render.com)
2. An OpenAI API key
3. Your code pushed to a Git repository (GitHub, GitLab, or Bitbucket)

## Step-by-Step Deployment

### Option 1: Using Render Dashboard (Recommended)

1. **Log in to Render**
   - Go to https://dashboard.render.com
   - Sign in or create an account

2. **Create a New Web Service**
   - Click "New +" button
   - Select "Web Service"
   - Connect your Git repository (GitHub/GitLab/Bitbucket)

3. **Configure the Service**
   - **Name**: `ai-content-humanizer` (or any name you prefer)
   - **Region**: Choose closest to you
   - **Branch**: `main` (or your default branch)
   - **Root Directory**: Leave empty (or specify if your files are in a subdirectory)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`

4. **Set Environment Variables**
   - Click "Environment" tab
   - Add the following:
     - **Key**: `OPENAI_API_KEY`
     - **Value**: Your OpenAI API key (get it from https://platform.openai.com/api-keys)
   - Click "Save Changes"

5. **Deploy**
   - Click "Create Web Service"
   - Render will automatically build and deploy your app
   - Wait for the build to complete (usually 2-5 minutes)

6. **Access Your App**
   - Once deployed, you'll get a URL like: `https://ai-content-humanizer.onrender.com`
   - Open this URL in your browser

### Option 2: Using render.yaml (Automated)

If you have `render.yaml` in your repository:

1. **Push your code** to GitHub/GitLab/Bitbucket
2. **In Render Dashboard**:
   - Click "New +" → "Blueprint"
   - Connect your repository
   - Render will automatically detect `render.yaml` and create the service
   - Add your `OPENAI_API_KEY` in the Environment Variables section
   - Deploy

## Important Notes

### Environment Variables

Make sure to set:
- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `PORT`: Automatically set by Render (don't change)
- `PYTHON_VERSION`: Set to `3.11.0` (or as specified in runtime.txt)

### Free Tier Limitations

- Render free tier services **spin down after 15 minutes of inactivity**
- First request after spin-down may take 30-60 seconds
- Consider upgrading to paid plan for always-on service

### Updating Your App

1. Push changes to your Git repository
2. Render will automatically detect and redeploy
3. Or manually trigger redeploy from Render dashboard

## Troubleshooting

### Build Fails

- Check build logs in Render dashboard
- Verify `requirements.txt` has all dependencies
- Ensure Python version is compatible (3.7+)
- Check for syntax errors in `app.py`

### App Crashes on Start

- Check runtime logs in Render dashboard
- Verify `OPENAI_API_KEY` is set correctly
- Ensure `gunicorn` is in `requirements.txt`
- Check that `Procfile` exists and is correct

### API Errors

- Verify OpenAI API key is valid
- Check you have credits in your OpenAI account
- Review error messages in Render logs

### CORS Issues

- `flask-cors` should handle this automatically
- If issues persist, check CORS configuration in `app.py`

## Testing Locally Before Deploying

Test with production-like settings:

```bash
# Install gunicorn
pip install gunicorn

# Run with gunicorn (production server)
gunicorn app:app

# Or test with production environment
export FLASK_DEBUG=False
python app.py
```

## Custom Domain (Optional)

1. In Render dashboard, go to your service
2. Click "Settings" → "Custom Domain"
3. Add your domain
4. Follow DNS configuration instructions

## Monitoring

- View logs in real-time from Render dashboard
- Set up alerts for service failures
- Monitor usage and performance metrics

## Cost Estimation

- **Free Tier**: $0/month (with limitations)
- **Starter Plan**: $7/month (always-on, better performance)
- **Standard Plan**: $25/month (more resources)

Check Render pricing at https://render.com/pricing
