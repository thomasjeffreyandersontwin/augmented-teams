#!/usr/bin/env python3
"""
[FEATURE_NAME] Service
Main application entry point
"""

from fastapi import FastAPI
from pathlib import Path
import yaml

# Load configuration from feature-config.yaml
def load_config():
    """Load configuration from feature-config.yaml"""
    config_file = Path(__file__).parent / "config" / "feature-config.yaml"
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)

config = load_config()

# Create FastAPI app
app = FastAPI(
    title=config['feature']['name'],
    description=config['feature']['description'],
    version=config['feature']['version']
)

@app.get("/")
def root():
    """Root endpoint"""
    return {
        "status": "healthy",
        "service": config['feature']['name'],
        "version": config['feature']['version']
    }

@app.get(config['health_check']['path'])
def health():
    """Health check endpoint"""
    return {"status": "healthy"}

# Add your feature-specific endpoints here
