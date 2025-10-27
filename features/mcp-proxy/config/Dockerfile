# Use multi-stage build to get GitHub MCP server
FROM ghcr.io/github/github-mcp-server AS mcp-server

FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Set default environment variables
ENV SERVICE_PORT=8000
ENV SERVICE_HOST=0.0.0.0
ENV ENVIRONMENT=production
ENV LOG_LEVEL=INFO

# Install dependencies including supervisord for running multiple services
RUN pip install --no-cache-dir fastapi>=0.104.0 uvicorn>=0.24.0 pydantic>=2.4.0 requests>=2.31.0 pyyaml>=6.0 supervisor

# Copy GitHub MCP server from the official image
COPY --from=mcp-server /server/github-mcp-server /usr/local/bin/github-mcp-server

# Copy source code
COPY . .

# Create supervisord config
RUN echo '[supervisord]' > /etc/supervisor/conf.d/mcp.conf && \
    echo 'nodaemon=true' >> /etc/supervisor/conf.d/mcp.conf && \
    echo '' >> /etc/supervisor/conf.d/mcp.conf && \
    echo '[program:mcp-server]' >> /etc/supervisor/conf.d/mcp.conf && \
    echo 'command=/usr/local/bin/github-mcp-server' >> /etc/supervisor/conf.d/mcp.conf && \
    echo 'environment=GITHUB_PERSONAL_ACCESS_TOKEN="%(ENV_GITHUB_PERSONAL_ACCESS_TOKEN)s"' >> /etc/supervisor/conf.d/mcp.conf && \
    echo 'stdout_logfile=/dev/stdout' >> /etc/supervisor/conf.d/mcp.conf && \
    echo 'stdout_logfile_maxbytes=0' >> /etc/supervisor/conf.d/mcp.conf && \
    echo 'stderr_logfile=/dev/stderr' >> /etc/supervisor/conf.d/mcp.conf && \
    echo 'stderr_logfile_maxbytes=0' >> /etc/supervisor/conf.d/mcp.conf && \
    echo '' >> /etc/supervisor/conf.d/mcp.conf && \
    echo '[program:mcp-proxy]' >> /etc/supervisor/conf.d/mcp.conf && \
    echo 'command=uvicorn service:app --host 0.0.0.0 --port 8000' >> /etc/supervisor/conf.d/mcp.conf && \
    echo 'stdout_logfile=/dev/stdout' >> /etc/supervisor/conf.d/mcp.conf && \
    echo 'stdout_logfile_maxbytes=0' >> /etc/supervisor/conf.d/mcp.conf && \
    echo 'stderr_logfile=/dev/stderr' >> /etc/supervisor/conf.d/mcp.conf && \
    echo 'stderr_logfile_maxbytes=0' >> /etc/supervisor/conf.d/mcp.conf

# Expose port
EXPOSE ${SERVICE_PORT}

# Run supervisord to manage both services
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]
