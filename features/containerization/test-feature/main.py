#!/usr/bin/env python3
"""
Test Containerization Feature - Main Service
Simple Flask service for testing the feature lifecycle
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def health():
    """Health check endpoint"""
    return {'status': 'healthy', 'service': 'test-containerization'}

@app.route('/test')
def test():
    """Test endpoint"""
    return {'message': 'test-containerization is working'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

