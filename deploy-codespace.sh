#!/bin/bash
# Complete deployment script for Codespace
echo "🚀 Starting complete system deployment in Codespace..."

# Change to project root
cd /workspaces/augmented-teams

# Step 1: Install dependencies
echo "📦 Installing dependencies..."
cd src/features/vector-search
pip install -r requirements.txt

# Step 2: Run tests
echo "🧪 Running tests..."
python test_setup.py

# Step 3: Stop existing server
echo "🛑 Stopping existing server..."
pkill -f "uvicorn.*api:app" || echo "No existing server to stop"

# Step 4: Start server in background
echo "🚀 Starting server..."
nohup python -m uvicorn api:app --host 0.0.0.0 --port 8000 > server.log 2>&1 &
echo $! > server.pid

# Wait for server to start
sleep 5

# Step 5: Test server
echo "🧪 Testing server..."
curl -f http://localhost:8000/health || exit 1

# Step 6: Index database
echo "📚 Indexing database..."
python vector_search.py index

# Step 7: Test all endpoints
echo "🔍 Testing all endpoints..."
curl -f "http://localhost:8000/search?query=test"
curl -f "http://localhost:8000/files"
curl -f "http://localhost:8000/stats"

echo "✅ Complete system deployed!"
echo "🌐 Server running on port 8000"
echo "📋 Next: Make port 8000 public in Codespace Ports tab"
