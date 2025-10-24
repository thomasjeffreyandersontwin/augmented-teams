#!/usr/bin/env python3
"""
Git Commit REST Service

A FastAPI service that provides clean REST endpoints for committing changes to Git.
Replaces the complex git_sync.py with simple, focused API endpoints.
"""

import os
import subprocess
import base64
from pathlib import Path
from datetime import datetime
from typing import Optional
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn

# Configuration
REPO_PATH = Path(__file__).resolve().parents[3]  # repo root
REMOTE_NAME = "origin"
BRANCH = "main"

app = FastAPI(
    title="Git Commit Service",
    description="REST API for committing changes to Git repository",
    version="1.0.0"
)

class CommitRequest(BaseModel):
    content: str
    file_path: str
    commit_message: Optional[str] = None

class CommitResponse(BaseModel):
    success: bool
    message: str
    commit_hash: Optional[str] = None
    file_path: str

def run_git_command(cmd: list, cwd: Path = REPO_PATH) -> tuple[str, str, int]:
    """Run a git command and return stdout, stderr, returncode"""
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return result.stdout.strip(), result.stderr.strip(), result.returncode

def ensure_git_identity():
    """Ensure git identity is configured"""
    run_git_command(["git", "config", "user.name", "Git Commit Service"])
    run_git_command(["git", "config", "user.email", "git-commit-service@augmented-teams.com"])

def get_default_commit_message(file_path: str) -> str:
    """Generate a default commit message"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"feat: update {file_path} at {timestamp}"

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "Git Commit Service is running", "repo": str(REPO_PATH)}

@app.get("/status")
async def get_status():
    """Get repository status"""
    stdout, stderr, returncode = run_git_command(["git", "status", "--porcelain"])
    
    return {
        "repo_path": str(REPO_PATH),
        "branch": BRANCH,
        "has_changes": bool(stdout),
        "changes": stdout.split('\n') if stdout else [],
        "error": stderr if returncode != 0 else None
    }

@app.post("/commit/text", response_model=CommitResponse)
async def commit_text(request: CommitRequest):
    """
    Commit text content to a file
    
    Args:
        content: The text content to write
        file_path: Where to write the file (relative to repo root)
        commit_message: Optional commit message
    """
    try:
        # Ensure git identity
        ensure_git_identity()
        
        # Create file path
        file_path = REPO_PATH / request.file_path
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write content to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(request.content)
        
        # Add file to git
        stdout, stderr, returncode = run_git_command(["git", "add", request.file_path])
        if returncode != 0:
            raise HTTPException(status_code=500, detail=f"Failed to add file: {stderr}")
        
        # Commit changes
        commit_msg = request.commit_message or get_default_commit_message(request.file_path)
        stdout, stderr, returncode = run_git_command(["git", "commit", "-m", commit_msg])
        
        if returncode != 0:
            if "nothing to commit" in stderr.lower():
                return CommitResponse(
                    success=True,
                    message="No changes to commit",
                    file_path=request.file_path
                )
            raise HTTPException(status_code=500, detail=f"Failed to commit: {stderr}")
        
        # Get commit hash
        stdout, stderr, returncode = run_git_command(["git", "rev-parse", "HEAD"])
        commit_hash = stdout if returncode == 0 else None
        
        return CommitResponse(
            success=True,
            message=f"Successfully committed {request.file_path}",
            commit_hash=commit_hash,
            file_path=request.file_path
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/commit/document", response_model=CommitResponse)
async def commit_document(
    file: UploadFile = File(...),
    file_path: str = Form(...),
    commit_message: Optional[str] = Form(None)
):
    """
    Commit a document file
    
    Args:
        file: The uploaded file
        file_path: Where to save the file (relative to repo root)
        commit_message: Optional commit message
    """
    try:
        # Ensure git identity
        ensure_git_identity()
        
        # Create file path
        target_path = REPO_PATH / file_path
        target_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write uploaded file
        content = await file.read()
        with open(target_path, 'wb') as f:
            f.write(content)
        
        # Add file to git
        stdout, stderr, returncode = run_git_command(["git", "add", file_path])
        if returncode != 0:
            raise HTTPException(status_code=500, detail=f"Failed to add file: {stderr}")
        
        # Commit changes
        commit_msg = commit_message or get_default_commit_message(file_path)
        stdout, stderr, returncode = run_git_command(["git", "commit", "-m", commit_msg])
        
        if returncode != 0:
            if "nothing to commit" in stderr.lower():
                return CommitResponse(
                    success=True,
                    message="No changes to commit",
                    file_path=file_path
                )
            raise HTTPException(status_code=500, detail=f"Failed to commit: {stderr}")
        
        # Get commit hash
        stdout, stderr, returncode = run_git_command(["git", "rev-parse", "HEAD"])
        commit_hash = stdout if returncode == 0 else None
        
        return CommitResponse(
            success=True,
            message=f"Successfully committed {file_path}",
            commit_hash=commit_hash,
            file_path=file_path
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/push")
async def push_changes():
    """Push committed changes to remote repository"""
    try:
        ensure_git_identity()
        
        stdout, stderr, returncode = run_git_command(["git", "push", REMOTE_NAME, BRANCH])
        
        if returncode != 0:
            raise HTTPException(status_code=500, detail=f"Failed to push: {stderr}")
        
        return {
            "success": True,
            "message": "Successfully pushed changes to remote",
            "output": stdout
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/commit-and-push", response_model=CommitResponse)
async def commit_and_push(request: CommitRequest):
    """
    Commit text content and push to remote in one operation
    """
    try:
        # Commit the changes
        commit_response = await commit_text(request)
        
        if commit_response.success:
            # Push to remote
            push_result = await push_changes()
            if not push_result["success"]:
                raise HTTPException(status_code=500, detail="Commit succeeded but push failed")
        
        return commit_response
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    print(f"Starting Git Commit Service for repository: {REPO_PATH}")
    uvicorn.run(app, host="0.0.0.0", port=8001)
