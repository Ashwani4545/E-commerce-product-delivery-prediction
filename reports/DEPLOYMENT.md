# 🐳 Docker Deployment Guide

## Quick Start

### Prerequisites
- Model file: `model/delivery_deay_model.pkl` (must be present)

### Deploy with Docker Compose (Recommended)

1. **Clone/Setup Project**
   ```bash
   cd e:\PROJECTS\Advanced ML\E-commerce-product-delivery-prediction
   ```

2. **Create Environment File** (Optional - uses defaults if not provided)
   ```bash
   # Copy the example file
   copy .env.example .env
   # Edit .env if you need custom values
   ```

3. **Build and Start Services**
   ```bash
   # Build images and start containers in detached mode
   docker-compose up -d
   
   # Or, to see logs:
   docker-compose up
   ```

4. **Access Applications**
   - **FastAPI Docs**: http://localhost:8000/docs
   - **Streamlit UI**: http://localhost:8501

5. **View Logs**
   ```bash
   # View all logs
   docker-compose logs -f
   
   # View specific service logs
   docker-compose logs -f api
   docker-compose logs -f streamlit
   ```

6. **Stop Services**
   ```bash
   docker-compose down
   
   # Remove volumes too (WARNING: clears data)
   docker-compose down -v
   ```

---

## Individual Docker Commands

### Build API Image Only
```bash
docker build -t ecommerce-api:latest .
```

### Build Streamlit Image Only
```bash
docker build -f Dockerfile.streamlit -t ecommerce-streamlit:latest .
```

### Run API Container
```bash
docker run -d \
  --name ecommerce-api \
  -p 8000:8000 \
  -e MODEL_PATH=/app/model/delivery_deay_model.pkl \
  -v %cd%\model:/app/model \
  ecommerce-api:latest
```

### Run Streamlit Container
```bash
docker run -d \
  --name ecommerce-streamlit \
  -p 8501:8501 \
  -e API_URL=http://localhost:8000 \
  ecommerce-streamlit:latest
```

---

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `API_URL` | `http://127.0.0.1:8000` | URL for API (Streamlit uses this) |
| `MODEL_PATH` | `model/delivery_deay_model.pkl` | Path to ML model file |
| `API_PORT` | `8000` | FastAPI port |
| `STREAMLIT_PORT` | `8501` | Streamlit port |
| `PYTHONUNBUFFERED` | `1` | Show Python output immediately |

---

## Troubleshooting

### Issue: Port already in use
```bash
# Windows - Find process using port 8000
netstat -ano | findstr :8000

# Kill process by PID
taskkill /PID <PID> /F
```

### Issue: Cannot connect API → Streamlit
- In Docker Compose, use `http://api:8000` (service name)
- Already configured in docker-compose.yml

### Issue: Model file not found
```bash
# Verify model exists
ls model/delivery_deay_model.pkl

# Check container logs
docker-compose logs api
```

### Issue: Cannot build Docker image
```bash
# Clear Docker cache
docker system prune -a

# Rebuild
docker-compose build --no-cache
```

---

## Production Deployment

For production, consider:

1. **Use specific image tags** instead of `latest`
   ```yaml
   image: ecommerce-api:v1.0.0
   ```

2. **Add resource limits** in docker-compose.yml
   ```yaml
   deploy:
     resources:
       limits:
         cpus: '2'
         memory: 1G
   ```

3. **Enable restart policies**
   ```yaml
   restart_policy:
     condition: on-failure
     delay: 5s
     max_attempts: 3
   ```

4. **Use external reverse proxy** (Nginx, Traefik)

5. **Set up logging** to external service

6. **Configure health checks** (already done!)

---

## Container Networking

- **Network Name**: `ecommerce-network`
- **API Container**: `ecommerce-api` (port 8000)
- **Streamlit Container**: `ecommerce-streamlit` (port 8501)
- Containers can communicate using service names (e.g., `http://api:8000`)

---

## Docker Compose Health Checks

- **API**: Health check every 30s, starts after 40s
- **Streamlit**: Depends on API being healthy before starting

Check health status:
```bash
docker-compose ps

# Expected output:
# ecommerce-api       ... healthy
# ecommerce-streamlit ... up
```

---

## Useful Docker Commands

```bash
# View running containers
docker ps

# View all containers
docker ps -a

# Remove containers
docker rm <container_id>

# Remove images
docker rmi <image_id>

# Check container stats
docker stats

# Execute command in running container
docker exec -it ecommerce-api bash

# Copy files from container
docker cp ecommerce-api:/app/logs ./logs
```

---

## API Testing

```bash
# Test prediction endpoint
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d "{\"price\": 29.99, \"quantity\": 2, \"category\": \"Electronics\", \"customer_segment\": \"Regular\", \"channel\": \"Direct\", \"device_type\": \"Mobile\", \"order_dayofweek\": 1, \"order_month\": 11, \"customer_risk_score\": 0.3}"

# View API docs
# Visit: http://localhost:8000/docs
```

---

## Version Info

- **Python**: 3.10
- **FastAPI**: Latest
- **Streamlit**: Latest
- **Base Image**: python:3.10-slim
