#!/bin/bash
# Complete workflow script
cd /workspaces/augmented-teams
cd src/integration/git
python git_sync.py
python -c "import git_sync; git_sync.reindex_after_content_changes()"
cd ../../features/vector-search
python deploy_and_test.py