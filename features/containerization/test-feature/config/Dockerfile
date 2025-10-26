FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Set default environment variables
ENV SERVICE_PORT=8000
ENV SERVICE_HOST=0.0.0.0
ENV ENVIRONMENT=production
ENV LOG_LEVEL=INFO

# Install dependencies directly from config
RUN pip install --no-cache-dir fastapi>=0.104.0 uvicorn>=0.24.0 pydantic>=2.4.0 requests>=2.31.0 pyyaml>=6.0

# Copy source code
COPY . .

# Expose port (configurable via ENV)
EXPOSE ${SERVICE_PORT}

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:${SERVICE_PORT}/ || exit 1

# Run the application using uvicorn
CMD ["uvicorn", "service:app", "--host", "0.0.0.0", "--port", "8000"]
