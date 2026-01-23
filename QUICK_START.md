# 🚀 Quick Deployment Guide

Your E-Commerce Delivery Prediction project is **now ready for Docker deployment**!

## ✅ What's Been Set Up

- ✓ **Docker containers** for API (FastAPI) and UI (Streamlit)
- ✓ **Docker Compose** configuration for easy multi-container management
- ✓ **Health checks** to ensure services are running properly
- ✓ **Environment configuration** files
- ✓ **Networking** between services
- ✓ **Deployment scripts** for Windows

## 🎯 Quick Start (Choose One)

### Option 1: Using Batch Script (Windows)
```batch
deploy.bat
```
This will build and start all services automatically.

### Option 2: Using PowerShell Script (Windows)
```powershell
powershell -ExecutionPolicy Bypass -File deploy.ps1
```

### Option 3: Manual Docker Commands

**Build images:**
```bash
docker-compose build
```

**Start services:**
```bash
docker-compose up -d
```

**View logs:**
```bash
docker-compose logs -f
```

**Stop services:**
```bash
docker-compose down
```

## 🌐 Access Your Applications

Once running, open in your browser:

- **API Documentation**: http://localhost:8000/docs
  - Interactive Swagger UI for testing endpoints
  - Try predictions directly in the browser

- **Streamlit UI**: http://localhost:8501
  - User-friendly interface for predictions
  - Real-time form validation

## 📋 Pre-Requisites

- **Docker Desktop** installed ([Download](https://www.docker.com/products/docker-desktop))
- **Model file**: `model/delivery_deay_model.pkl` ✓ (You have this!)

## 🔍 Verify Everything Works

### Test the API directly:
```powershell
$payload = @{
    price = 29.99
    quantity = 2
    category = "Electronics"
    customer_segment = "Regular"
    channel = "Direct"
    device_type = "Mobile"
    order_dayofweek = 1
    order_month = 11
    customer_risk_score = 0.3
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:8000/predict" `
    -Method POST `
    -Body $payload `
    -ContentType "application/json" | Select-Object -ExpandProperty Content
```

### View container status:
```bash
docker ps
docker-compose ps
```

### Check service health:
```bash
# API health
curl http://localhost:8000/

# View logs
docker-compose logs api
docker-compose logs streamlit
```

## 📂 Project Structure

```
E-commerce-product-delivery-prediction/
├── Dockerfile              # API container definition
├── Dockerfile.streamlit    # Streamlit container definition
├── docker-compose.yml      # Multi-container orchestration
├── .env.example           # Environment variables template
├── api/                   # FastAPI backend
│   ├── main.py           # API endpoints
│   ├── model.py          # Model loading
│   └── schemas.py        # Request validation
├── app/                  # Streamlit frontend
│   └── streamlit_app.py  # UI code
├── model/                # ML models
│   └── delivery_deay_model.pkl
├── deploy.bat            # Windows batch deployment script
├── deploy.ps1            # Windows PowerShell deployment script
├── DEPLOYMENT.md         # Detailed deployment guide
└── requirements.txt      # Python dependencies
```

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Find process using port 8000 (Windows)
netstat -ano | findstr :8000

# Kill process
taskkill /PID <PID> /F
```

### Docker Daemon Not Running
- Restart Docker Desktop
- Or run: `docker-compose up` (will prompt to start Docker)

### Services Won't Start
```bash
# View detailed logs
docker-compose logs -f

# Restart services
docker-compose down
docker-compose up -d
```

### Model File Not Found
Ensure the file exists:
- Should be at: `model/delivery_deay_model.pkl` or `delivery_delay_model.pkl`
- Check file size: ~18 MB

## 📖 For Detailed Information

See **DEPLOYMENT.md** for:
- Environment variable configuration
- Production deployment tips
- Advanced Docker commands
- Custom deployment options

## ✨ Key Features

- **No installation needed** - Everything runs in containers
- **Easy to scale** - Simple to add more API instances
- **Health monitoring** - Automatic service health checks
- **Network isolation** - Containers talk securely
- **Data persistence** - Model files mounted as volumes
- **Logging** - Full service logs for debugging

## 🎓 Next Steps

1. ✓ Run `deploy.bat` or `deploy.ps1`
2. ✓ Open http://localhost:8000/docs
3. ✓ Test with sample data
4. ✓ Open http://localhost:8501
5. ✓ Make predictions through UI

## 🆘 Still Having Issues?

1. Check Docker is running: `docker ps`
2. Check logs: `docker-compose logs`
3. Verify model file exists
4. Ensure ports 8000 and 8501 are free
5. Restart Docker Desktop

---

**Happy deploying! 🎉**
