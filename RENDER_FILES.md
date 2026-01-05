# Files Required for Render Deployment

## Essential Files (Must Have)

These files are **required** for Render deployment:

1. **`app.py`** - Main Flask application
2. **`requirements.txt`** - Python dependencies
3. **`Procfile`** - Tells Render how to start the app
4. **`index.html`** - Frontend HTML
5. **`styles.css`** - Frontend styling
6. **`script.js`** - Frontend JavaScript

## Optional but Recommended

7. **`render.yaml`** - Automated deployment configuration
8. **`runtime.txt`** - Specifies Python version
9. **`.gitignore`** - Excludes unnecessary files from Git

## Files NOT Needed on Render

- `start_server.bat` - Windows-only, not needed
- `start_server.ps1` - Windows-only, not needed
- `test_server.py` - Testing script, not needed
- `TROUBLESHOOTING.md` - Documentation, optional
- `README.md` - Documentation, optional
- `.env` - Environment variables set in Render dashboard instead

## Quick Checklist

Before deploying to Render, ensure you have:

- [ ] `app.py` (updated for production)
- [ ] `requirements.txt` (includes `gunicorn`)
- [ ] `Procfile` (contains: `web: gunicorn app:app`)
- [ ] `index.html`
- [ ] `styles.css`
- [ ] `script.js`
- [ ] `render.yaml` (optional, for automated setup)
- [ ] `runtime.txt` (optional, specifies Python version)

## Environment Variables to Set in Render

In Render dashboard → Environment tab, add:

- `OPENAI_API_KEY` - Your OpenAI API key (required)
- `PORT` - Automatically set by Render (don't change)
- `FLASK_DEBUG` - Set to `False` for production (optional)

## Deployment Commands

Render will automatically run:
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app` (from Procfile)
