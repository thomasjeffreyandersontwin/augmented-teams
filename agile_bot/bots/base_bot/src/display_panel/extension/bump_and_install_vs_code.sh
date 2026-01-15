#!/bin/bash

# Bump version, rebuild, and reinstall the REPL Status Panel extension
# Usage: ./bump_and_install_vs_code.sh [patch|minor|major]
# Default: patch (0.24.7 -> 0.24.8)

BUMP_TYPE="${1:-patch}"

# Validate bump type
if [[ ! "$BUMP_TYPE" =~ ^(patch|minor|major)$ ]]; then
    echo "Usage: $0 [patch|minor|major]"
    exit 1
fi

set -e

# Navigate to extension directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "================================"
echo "REPL Status Panel Version Bump"
echo "================================"
echo ""

# Read current version from package.json
CURRENT_VERSION=$(grep -o '"version": "[^"]*"' package.json | head -1 | sed 's/"version": "\|"//g')
echo "Current version: $CURRENT_VERSION"

# Parse version
IFS='.' read -r MAJOR MINOR PATCH <<< "$CURRENT_VERSION"

# Bump version based on type
case "$BUMP_TYPE" in
    major)
        ((MAJOR++))
        MINOR=0
        PATCH=0
        ;;
    minor)
        ((MINOR++))
        PATCH=0
        ;;
    patch)
        ((PATCH++))
        ;;
esac

NEW_VERSION="$MAJOR.$MINOR.$PATCH"
echo "New version:     $NEW_VERSION"
echo ""

# Update package.json
echo "[1/5] Updating package.json..."
sed -i "s/\"version\": \"$CURRENT_VERSION\"/\"version\": \"$NEW_VERSION\"/" package.json
echo "      Done: package.json updated"

# Update html_renderer.js
echo "[2/5] Updating html_renderer.js..."
sed -i "s/v$CURRENT_VERSION/v$NEW_VERSION/g" html_renderer.js
echo "      Done: html_renderer.js updated"

# Package extension
echo "[3/5] Packaging extension..."
if ! npx @vscode/vsce package --allow-missing-repository --allow-star-activation > /dev/null 2>&1; then
    echo "      ERROR: Packaging failed!"
    exit 1
fi
echo "      Done: Extension packaged: repl-status-panel-$NEW_VERSION.vsix"

# Uninstall old extension
echo "[4/5] Uninstalling old extension..."
if code --uninstall-extension agilebot.repl-status-panel > /dev/null 2>&1; then
    echo "      Done: Old extension uninstalled"
else
    echo "      Warning: Uninstall warning (may not be installed)"
fi

# Install new extension
echo "[5/5] Installing new extension..."
VSIX_PATH="$SCRIPT_DIR/repl-status-panel-$NEW_VERSION.vsix"
if ! code --install-extension "$VSIX_PATH" > /dev/null 2>&1; then
    echo "      ERROR: Installation failed!"
    exit 1
fi
echo "      Done: Extension v$NEW_VERSION installed"

echo ""
echo "================================"
echo "SUCCESS!"
echo "================================"
echo ""
echo "Extension upgraded: $CURRENT_VERSION -> $NEW_VERSION"

# Give extension time to register
sleep 1

echo ""
echo "Extension v$NEW_VERSION will be active after reload!"
echo "If you are currently using VSCode, Please run the reload window command (Ctrl+Shift+P -> Developer: Reload Window)"
echo ""
