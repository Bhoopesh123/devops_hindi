# Use a lightweight Python 3.11 image
FROM python:3.11-slim

# Prevent .pyc files & enable real-time logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system deps (optional but useful for curl/debugging)
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Copy requirements first (better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose port
EXPOSE 8080

# ✅ Run FastAPI via Uvicorn (IMPORTANT FIX)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]