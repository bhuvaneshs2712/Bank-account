# 🚀 Deployment Guide - Bank Management System

## Recommended Platform: Render

### Why Render?
- ✅ Free tier available
- ✅ Perfect for Django applications
- ✅ Automatic deployments from GitHub
- ✅ Built-in database support
- ✅ SSL certificates included

## 📋 Deployment Steps

### 1. Go to Render.com
- Visit [render.com](https://render.com)
- Sign up/Login with your GitHub account

### 2. Create New Web Service
- Click "New +" → "Web Service"
- Connect your GitHub account
- Select repository: `bhuvaneshs2712/Bank-account`

### 3. Configure Service
Render will automatically detect your Django project and use:
- **Name**: `bank-system`
- **Environment**: Python
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn bank_system.wsgi`

### 4. Environment Variables
Render will automatically set:
- `DJANGO_SECRET_KEY` (auto-generated)
- `DEBUG=False`
- `ALLOWED_HOSTS=*`

### 5. Deploy
- Click "Create Web Service"
- Wait for build to complete (5-10 minutes)
- Your app will be live at: `https://your-app-name.onrender.com`

## 🔧 Manual Configuration (if needed)

If automatic detection doesn't work:

### Build Command:
```bash
pip install -r requirements.txt
```

### Start Command:
```bash
gunicorn bank_system.wsgi
```

### Environment Variables:
```
DJANGO_SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=*
```

## 📊 Post-Deployment

### 1. Create Superuser
After deployment, create an admin user:
```bash
python manage.py createsuperuser
```

### 2. Run Migrations
```bash
python manage.py migrate
```

### 3. Collect Static Files
```bash
python manage.py collectstatic
```

## 🌐 Custom Domain (Optional)

1. Go to your Render dashboard
2. Select your web service
3. Go to "Settings" → "Custom Domains"
4. Add your domain and configure DNS

## 🔍 Troubleshooting

### Common Issues:
1. **Build fails**: Check requirements.txt
2. **App crashes**: Check logs in Render dashboard
3. **Database errors**: Ensure migrations are run
4. **Static files not loading**: Check STATIC_ROOT configuration

### View Logs:
- Go to your Render dashboard
- Click on your web service
- Go to "Logs" tab

## 📞 Support

If you encounter issues:
1. Check Render documentation
2. Review Django deployment checklist
3. Check application logs
4. Contact Render support

---

**Your Bank Management System will be live and accessible worldwide!** 🏦✨
