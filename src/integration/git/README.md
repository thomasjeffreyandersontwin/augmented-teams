# Git Commit REST Service

A clean, focused FastAPI service for committing changes to Git. Replaces the complex git_sync.py with simple REST endpoints.

## 🚀 Quick Start

### Windows (PowerShell)
```powershell
.\start_service.ps1
```

### Python
```bash
python start_service.py
```

### Manual
```bash
pip install -r requirements.txt
python git_commit.py
```

## 📡 API Endpoints

### Health Check
- **GET** `/` - Service status
- **GET** `/status` - Repository status

### Commit Operations
- **POST** `/commit/text` - Commit text content to a file
- **POST** `/commit/document` - Commit uploaded document
- **POST** `/push` - Push changes to remote
- **POST** `/commit-and-push` - Commit and push in one operation

## 📋 Usage Examples

### Commit Text Content
```bash
curl -X POST "http://localhost:8001/commit/text" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "# New Document\nThis is new content",
    "file_path": "docs/new-file.md",
    "commit_message": "feat: add new documentation"
  }'
```

### Commit Document
```bash
curl -X POST "http://localhost:8001/commit/document" \
  -F "file=@document.pdf" \
  -F "file_path=assets/document.pdf" \
  -F "commit_message=docs: add new PDF"
```

### Check Status
```bash
curl "http://localhost:8001/status"
```

## 🔧 Configuration

- **Repository**: Auto-detected from script location
- **Port**: 8001
- **Git User**: "Git Commit Service"
- **Git Email**: "git-commit-service@augmented-teams.com"

## 🎯 Features

- ✅ **Simple REST API** - No complex workflows
- ✅ **Text & Document Support** - Handle any file type
- ✅ **Custom Commit Messages** - Or auto-generated
- ✅ **Error Handling** - Clear error responses
- ✅ **Health Checks** - Monitor service status
- ✅ **Auto Git Identity** - No manual git config needed

## 🔄 Integration

This service can be called from:
- GPT Actions (via HTTP requests)
- GitHub Actions (via curl)
- Any HTTP client
- Custom applications

**Much cleaner than the old git_sync.py approach!** 🚀