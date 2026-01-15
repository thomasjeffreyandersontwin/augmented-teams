#!/bin/bash
set -e

# Set the color variable
green='\033[0;32m'
# Clear the color after that
clear='\033[0m'

# Log error message to error.txt and exit
exit_log() {
	local error_message=$1	
	echo -e "$error_message" > error.txt
	exit 1
}

# Detect OS
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" || "$OSTYPE" == "cygwin" ]]; then
    IS_WINDOWS=true
else
    IS_WINDOWS=false
fi

echo -e ${green}"Augmented Teams Setup"
echo -e "=====================${clear}"

# Check git
if ! command -v git &> /dev/null; then
    exit_log "Error: Git not found"    
fi

# Clone repository (optional)
if [ ! -d "augmented-teams" ]; then
	git clone "https://github.com/thomasjeffreyandersontwin/augmented-teams.git" augmented-teams
fi
cd augmented-teams

# Check Python
if [ "$IS_WINDOWS" = true ]; then
    if command -v python &> /dev/null && [[ $(python --version 2>&1) == *"Python 3"* ]]; then
        PYTHON_CMD="python"
    elif command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
    fi
else
    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
    elif command -v python &> /dev/null && [[ $(python --version 2>&1) == *"Python 3"* ]]; then
        PYTHON_CMD="python"
    fi
fi

if [ -z "$PYTHON_CMD" ]; then
    exit_log "Error: Python 3 not found"    
fi

echo -e "Python: $($PYTHON_CMD --version)"

# Create and activate venv
if [ ! -d ".venv" ]; then
    echo -e "${green}Creating venv...${clear}"
    $PYTHON_CMD -m venv .venv
fi

if [ "$IS_WINDOWS" = true ]; then
    source .venv/Scripts/activate
else
    source .venv/bin/activate
fi

# add venv to VS Code settings.json
# do it here instead of in the source-control file to setup programatically cross-platform
if [ "$IS_WINDOWS" = true ]; then
    sed -i -e 's/${python_interpreter_default}/.venv\\\\Scripts\\\\python.exe/' .vscode\\settings.json
else
    sed -i '' -e 's/${python_interpreter_default}/.venv\/bin\/python/' .vscode\/settings.json
fi

# Install requirements
echo -e "Upgrading pip..."
python -m pip install --upgrade pip -q

if [ ! -f "requirements.txt" ]; then
    exit_log "Error: requirements.txt not found"    
fi

echo -e "${green}Installing requirements via pip...${clear}"
pip install -r requirements.txt

# echo -e "Downloading NLTK data..."
# python -c "import nltk; nltk.download('punkt_tab', quiet=True); nltk.download('averaged_perceptron_tagger_eng', quiet=True)" 2>/dev/null || true

# Install VS Code extensions
if command -v code &> /dev/null; then
    echo -e "${green}Installing VS Code extensions...${clear}"
    code --install-extension yzhang.markdown-all-in-one
    code --install-extension shd101wyy.markdown-preview-enhanced
    code --install-extension hediet.vscode-drawio
    code --install-extension ms-python.python
    code --install-extension ms-python.vscode-pylance
else
    echo -e "VS Code not found. Install extensions manually:"
    echo -e "  yzhang.markdown-all-in-one"
    echo -e "  shd101wyy.markdown-preview-enhanced"
    echo -e "  hediet.vscode-drawio"
    echo -e "  ms-python.python"
    echo -e "  ms-python.vscode-pylance"
fi

echo -e ""
echo -e "${green}************SETUP COMPLETE*************${clear}"
echo -e ""
