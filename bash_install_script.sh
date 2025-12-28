#!/bin/bash
set -euo pipefail

# Set the color variables
green='\033[0;32m'
yellow='\033[0;33m'
clear='\033[0m'

# Log error message to error.txt and exit
exit_log() {
    local error_message=$1
    echo -e "$error_message" > error.txt
    exit 1
}

prompt_for_directory() {
    local default_dir="."
    read -r -p "Enter directory to clone repository into [default: ${PWD}]: " target_dir
    target_dir="${target_dir:-$default_dir}"  # Use default if empty

    # Expand path and ensure it's absolute
    if [[ "$target_dir" != /* ]]; then
        # Relative path - make it absolute relative to current directory
        target_dir="$(cd "${PWD}" && cd "$(dirname -- "./$target_dir")" && pwd)/$(basename -- "$target_dir")"
    fi

    # Create directory if it doesn't exist
    if [[ ! -d "$target_dir" ]]; then
        if confirm_action "Directory doesn't exist. Create it?" "y"; then
            mkdir -p "$target_dir" || exit_log "Failed to create directory: $target_dir"
        else
            exit_log "Aborting setup"
        fi
    fi

    echo "$target_dir"
}

# Function to get yes/no user input
confirm_action() {
    local prompt="$1"
    local default="$2"
    while true; do
        read -p "$prompt [y/n] ($default): " yn
        case $yn in
            [Yy]* ) return 0;;
            [Nn]* ) return 1;;
            "" ) case $default in
                    [Yy]* ) return 0;;
                    * ) return 1;;
                 esac;;
            * ) echo "Please answer yes or no.";;
        esac
    done
}


# Detect OS
IS_WINDOWS=false
IS_MAC=false
IS_LINUX=false
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" || "$OSTYPE" == "cygwin" ]]; then
    IS_WINDOWS=true
elif [[ "$OSTYPE" == "darwin"* ]]; then
    IS_MAC=true
else
    IS_LINUX=true
fi

echo -e "${green}Augmented Teams Setup${clear}"
echo -e "====================="

# Check git (required)
if ! command -v git &> /dev/null; then
    exit_log "Error: Git not found"
fi

# Clone repository if not exists
TARGET_DIR=$(prompt_for_directory)
echo -e "${green}Using target directory: ${TARGET_DIR}${clear}"

if [[ ! -d "${TARGET_DIR}/augmented-teams" ]]; then
    echo -e "${green}Cloning repository...${clear}"
    (cd "$TARGET_DIR" && git clone "https://github.com/thomasjeffreyandersontwin/augmented-teams.git" augmented-teams)
fi
cd "${TARGET_DIR}/augmented-teams"

# Check Python (required)
PYTHON_CMD=""
if [ "$IS_WINDOWS" ]; then
    if command -v python &> /dev/null && [[ $(python --version 2>&1) =~ Python\ 3 ]]; then
        PYTHON_CMD="python"
    elif command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
    fi
else
    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
    elif command -v python &> /dev/null && [[ $(python --version 2>&1) =~ Python\ 3 ]]; then
        PYTHON_CMD="python"
    fi
fi

if [ -z "$PYTHON_CMD" ]; then
    exit_log "Error: Python 3 not found"
fi

python_interpreter_default="$(which $PYTHON_CMD)" 

echo -e "Python: $($PYTHON_CMD --version)"

# Option 1: Create virtual environment
if confirm_action "${yellow}Create virtual environment?${clear}" "y"; then
    if [ ! -d ".venv" ]; then
        echo -e "${green}Creating venv...${clear}"
        $PYTHON_CMD -m venv .venv
    else
        echo "Virtual environment already exists"
    fi

    # Activate virtual environment
    if [ "$IS_WINDOWS" = true ]; then
        source .venv/Scripts/activate
    else
        source .venv/bin/activate
    fi

    # Update VS Code settings.json with correct Python interpreter path
    echo "Updating VS Code settings..."
    if [ "$IS_MAC" = true ]; then
        sed -i '' -e "s|${python_interpreter_default}|${TARGET_DIR}/augmented-teams/.venv/bin/python|" .vscode/settings.json
    else
        sed -i -e "s|${python_interpreter_default}|${TARGET_DIR}/augmented-teams/.venv/bin/python|" .vscode/settings.json
    fi
else
    echo "Skipping virtual environment setup"
fi

# Install requirements (always done)
echo -e "${green}Installing requirements via pip...${clear}"
$PYTHON_CMD -m pip install --upgrade pip -q
if [ ! -f "requirements.txt" ]; then
    exit_log "Error: requirements.txt not found"
fi
pip install -r requirements.txt

# Option 2: Install VS Code extensions
if command -v code &> /dev/null; then
    if confirm_action "${yellow}Install VS Code extensions?${clear}" "y"; then
        echo -e "${green}Installing VS Code extensions...${clear}"
        code --install-extension yzhang.markdown-all-in-one || echo "Failed to install markdown-all-in-one"
        code --install-extension shd101wyy.markdown-preview-enhanced || echo "Failed to install markdown-preview-enhanced"
        code --install-extension hediet.vscode-drawio || echo "Failed to install vscode-drawio"
        code --install-extension ms-python.python || echo "Failed to install Python extension"
        code --install-extension ms-python.vscode-pylance || echo "Failed to install Pylance"
    else
        echo "Skipping VS Code extensions installation"
        echo -e "${yellow}Recommended extensions:${clear}"
        echo "  yzhang.markdown-all-in-one"
        echo "  shd101wyy.markdown-preview-enhanced"
        echo "  hediet.vscode-drawio"
        echo "  ms-python.python"
        echo "  ms-python.vscode-pylance"
    fi
else
    echo -e "${yellow}VS Code not found. Install extensions manually:${clear}"
    echo "  yzhang.markdown-all-in-one"
    echo "  shd101wyy.markdown-preview-enhanced"
    echo "  hediet.vscode-drawio"
    echo "  ms-python.python"
    echo "  ms-python.vscode-pylance"
fi

echo -e ""
echo -e "${green}************SETUP COMPLETE*************${clear}"
echo -e ""