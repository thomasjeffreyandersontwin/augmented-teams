#!/usr/bin/env python3
"""
Scan codebase and update cursor-behavior-index.mdc with current inventory.
Updates the index file with accurate information from features/, .cursor/, and commands/.
"""
import json
import re
from pathlib import Path
from typing import Dict, List

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
FEATURES_DIR = REPO_ROOT / "features"
CURSOR_RULES = REPO_ROOT / ".cursor" / "rules"
CURSOR_COMMAND_DOCS = REPO_ROOT / ".cursor" / "commands"
COMMANDS_DIR = REPO_ROOT / "commands"
INDEX_FILE = FEATURES_DIR / "cursor-behavior" / "cursor-behavior-index.mdc"
MCP_CONFIG = REPO_ROOT / "mcp.json"
MASK_TOKEN = "***MASKED***"

# Patterns
CMD_DOC_PATTERN = re.compile(r"-cmd\.md$")
CMD_FUNC_PATTERN = re.compile(r"_cmd\.py$")


def find_feature_cursor_dirs() -> Dict[str, Path]:
    """Find all feature/cursor directories."""
    features: Dict[str, Path] = {}
    if not FEATURES_DIR.exists():
        return features
    
    for feature_dir in FEATURES_DIR.iterdir():
        if not feature_dir.is_dir():
            continue
        cursor_dir = feature_dir / "cursor"
        if cursor_dir.exists() and cursor_dir.is_dir():
            features[feature_dir.name] = cursor_dir
        # Also check if files are directly in feature folder (cursor-behavior case)
        elif any(
            f.suffix == ".mdc" or f.suffix == ".md" or (f.suffix == ".py" and "_cmd.py" in f.name)
            for f in feature_dir.iterdir()
            if f.is_file()
        ):
            features[feature_dir.name] = feature_dir
    
    return features


def scan_feature(feature_name: str, base_path: Path) -> Dict[str, List[str]]:
    """Scan a feature directory for rules, commands, and command functions."""
    inventory = {
        "rules": [],
        "commands": [],
        "command_functions": [],
        "mcp": []
    }
    
    if not base_path.exists():
        return inventory
    
    # Scan for rules (*.mdc)
    for f in base_path.glob("*.mdc"):
        if f.is_file():
            inventory["rules"].append(f.name)
    
    # Scan for command docs (*-cmd.md)
    for f in base_path.glob("*.md"):
        if f.is_file() and CMD_DOC_PATTERN.search(f.name):
            inventory["commands"].append(f.name)
    
    # Scan for command functions (*_cmd.py)
    for f in base_path.glob("*.py"):
        if f.is_file() and CMD_FUNC_PATTERN.search(f.name):
            inventory["command_functions"].append(f.name)
    
    # Scan for MCP config files
    for f in base_path.glob("*-mcp.json"):
        if f.is_file():
            inventory["mcp"].append(f.name)
    
    return inventory


def scan_deployment() -> Dict[str, List[str]]:
    """Scan .cursor/ and commands/ for deployed items."""
    deployed = {
        "rules": [],
        "commands": [],
        "command_functions": []
    }
    
    # Scan .cursor/rules/
    if CURSOR_RULES.exists():
        for f in CURSOR_RULES.glob("*.mdc"):
            if f.is_file():
                deployed["rules"].append(f.name)
    
    # Scan .cursor/commands/
    if CURSOR_COMMAND_DOCS.exists():
        for f in CURSOR_COMMAND_DOCS.glob("*.md"):
            if f.is_file():
                deployed["commands"].append(f.name)
    
    # Scan commands/
    if COMMANDS_DIR.exists():
        for f in COMMANDS_DIR.glob("*.py"):
            if f.is_file():
                deployed["command_functions"].append(f.name)
    
    return deployed


def find_orphans(
    feature_inventories: Dict[str, Dict[str, List[str]]],
    deployed: Dict[str, List[str]]
) -> Dict[str, List[str]]:
    """Find orphaned items (in deployment but not in any feature source)."""
    all_feature_rules = set()
    all_feature_commands = set()
    all_feature_funcs = set()
    
    for inv in feature_inventories.values():
        all_feature_rules.update(inv["rules"])
        all_feature_commands.update(inv["commands"])
        all_feature_funcs.update(inv["command_functions"])
    
    orphans = {
        "rules": [r for r in deployed["rules"] if r not in all_feature_rules],
        "commands": [c for c in deployed["commands"] if c not in all_feature_commands],
        "command_functions": [f for f in deployed["command_functions"] if f not in all_feature_funcs]
    }
    
    return orphans


def update_index_section(
    content: str,
    new_content: str,
    start_marker: str
) -> str:
    """Update a specific section in the index file - replaces ALL occurrences with one."""
    # Escape the marker for regex
    escaped_marker = re.escape(start_marker)
    # Pattern: marker (possibly duplicated), then everything until next ## header or end of file
    # Handle consecutive duplicate headers
    pattern = r'(?:^|\n)' + escaped_marker + r'(?:\n' + escaped_marker + r')*\n.*?(?=\n## |$)'
    
    # Count how many times this section appears
    matches = list(re.finditer(pattern, content, re.DOTALL | re.MULTILINE))
    
    if matches:
        # Remove ALL existing occurrences
        for match in reversed(matches):  # Reverse to maintain indices
            content = content[:match.start()] + content[match.end():]
        
        # Find where to insert (before Orphaned Behaviors if it exists, otherwise at end before See also)
        insert_idx = content.find("\n## Orphaned Behaviors")
        if insert_idx == -1:
            insert_idx = content.find("\n## See also")
            if insert_idx == -1:
                # Append at end
                content = content.rstrip() + "\n\n" + start_marker + "\n" + new_content + "\n"
            else:
                # Insert before See also
                content = content[:insert_idx].rstrip() + "\n\n" + start_marker + "\n" + new_content + "\n\n" + content[insert_idx:]
        else:
            # Insert before Orphaned Behaviors
            content = content[:insert_idx].rstrip() + "\n\n" + start_marker + "\n" + new_content + "\n\n" + content[insert_idx:]
    else:
        # Section doesn't exist, add it
        insert_idx = content.find("\n## Orphaned Behaviors")
        if insert_idx == -1:
            insert_idx = content.find("\n## See also")
            if insert_idx == -1:
                content = content.rstrip() + "\n\n" + start_marker + "\n" + new_content + "\n"
            else:
                content = content[:insert_idx].rstrip() + "\n\n" + start_marker + "\n" + new_content + "\n\n" + content[insert_idx:]
        else:
            content = content[:insert_idx].rstrip() + "\n\n" + start_marker + "\n" + new_content + "\n\n" + content[insert_idx:]
    
    return content


def format_feature_inventory(feature_name: str, inventory: Dict[str, List[str]]) -> str:
    """Format a feature's inventory for the index."""
    lines = [f"### Feature: {feature_name}"]
    
    lines.append("- **Rules:**")
    if inventory["rules"]:
        for rule in sorted(inventory["rules"]):
            lines.append(f"  - `{rule}`")
    else:
        lines.append("  - None")
    
    lines.append("- **Commands:**")
    if inventory["commands"]:
        for cmd in sorted(inventory["commands"]):
            lines.append(f"  - `{cmd}`")
    else:
        lines.append("  - None")
    
    lines.append("- **Command Functions:**")
    if inventory["command_functions"]:
        for func in sorted(inventory["command_functions"]):
            lines.append(f"  - `{func}`")
    else:
        lines.append("  - None")
    
    lines.append("- **MCP:**")
    if inventory["mcp"]:
        for mcp in sorted(inventory["mcp"]):
            lines.append(f"  - `{mcp}`")
    else:
        lines.append("  - None")
    
    return "\n".join(lines) + "\n"


def format_deployment_inventory(deployed: Dict[str, List[str]]) -> str:
    """Format deployed items for the index."""
    lines = []
    
    lines.append("### Rules (in `.cursor/rules/`)")
    if deployed["rules"]:
        for rule in sorted(deployed["rules"]):
            lines.append(f"- `{rule}`")
    else:
        lines.append("- *(empty - nothing synced yet)*")
    
    lines.append("\n### Commands (in `.cursor/commands/`)")
    if deployed["commands"]:
        for cmd in sorted(deployed["commands"]):
            lines.append(f"- `{cmd}`")
    else:
        lines.append("- *(empty - nothing synced yet)*")
    
    lines.append("\n### Command Functions (in `commands/`)")
    if deployed["command_functions"]:
        for func in sorted(deployed["command_functions"]):
            lines.append(f"- `{func}`")
    else:
        lines.append("- *(empty - nothing synced yet)*")
    
    return "\n".join(lines) + "\n"


def read_mcp_config() -> Dict:
    """Read MCP configuration from mcp.json"""
    if not MCP_CONFIG.exists():
        return {}
    try:
        with MCP_CONFIG.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def mask_secrets(value: str) -> str:
    """Mask sensitive values in MCP config"""
    if not value:
        return value
    if len(value) <= 8:
        return MASK_TOKEN
    if "TOKEN" in value.upper() or "_KEY" in value.upper():
        return MASK_TOKEN
    return value[:4] + MASK_TOKEN + value[-4:]


def get_tdd_pipeline_tools() -> Dict[str, Dict]:
    """Get list of TDD Pipeline MCP tools with examples from the server file"""
    mcp_server = REPO_ROOT / "features" / "test-driven-development" / "mcp_server.py"
    if not mcp_server.exists():
        return {}
    
    # Known tools with examples
    tools_info = {
        "dev_start": {
            "description": "Start development for a new feature",
            "example": '{"feature_name": "my-feature"}'
        },
        "get_current_step": {
            "description": "Get current pipeline step, phase, and status",
            "example": '{"feature_name": "my-feature"}'
        },
        "start_next_step": {
            "description": "Start the next pipeline step based on current state",
            "example": '{"feature_name": "my-feature"}'
        },
        "repeat_current_step": {
            "description": "Repeat the current pipeline step with feedback",
            "example": '{"feature_name": "my-feature"}'
        },
        "get_workflow_status": {
            "description": "Show all phases and their status",
            "example": '{"feature_name": "my-feature"}'
        },
        "resume_pipeline": {
            "description": "Resume pipeline from human activity (approve/reject)",
            "example": '{"feature_name": "my-feature", "approval": true}'
        },
        "reset_pipeline": {
            "description": "Reset pipeline to beginning",
            "example": '{"feature_name": "my-feature"}'
        },
        "skip_to_step": {
            "description": "Skip to a specific step by name",
            "example": '{"feature_name": "my-feature", "step_name": "DEVELOP_TEST"}'
        },
        "list_workflow_phases": {
            "description": "List all workflow phases with their status",
            "example": '{"feature_name": "my-feature"}'
        },
        "get_phase_details": {
            "description": "Get details for a specific phase",
            "example": '{"feature_name": "my-feature", "phase_name": "Develop"}'
        }
    }
    
    return tools_info


def get_tdd_pipeline_workflow_steps() -> Dict:
    """Get workflow steps and phases from the delivery pipeline"""
    pipeline_file = REPO_ROOT / "features" / "test-driven-development" / "delivery_pipeline.py"
    if not pipeline_file.exists():
        return {}
    
    try:
        content = pipeline_file.read_text(encoding="utf-8")
        # Extract PHASES structure
        # Looking for the PHASES = [...] definition
        phases_match = re.search(r'PHASES\s*=\s*\[(.*?)\]', content, re.DOTALL)
        if phases_match:
            phases_content = phases_match.group(1)
            # Extract phase names (look for 'name': 'PhaseName' followed by 'steps': at phase level)
            # Use lookahead to ensure it's followed by 'steps' to avoid matching step names
            phase_matches = re.findall(r"\{\s*'name':\s*'([A-Za-z]+)',\s*'steps':", phases_content)
            # Extract step names (within the 'steps' list, look for 'name': 'STEP_NAME')
            # Only match step names that are within the steps array, not phase names
            step_matches = re.findall(r"\['steps':\s*\[(.*?)\]", phases_content, re.DOTALL)
            if step_matches:
                # Now extract step names from the steps content
                steps_content = step_matches[0]
                step_names = re.findall(r"{'name':\s*'([A-Z_]+)'", steps_content)
                step_matches = step_names
            else:
                # Fallback: just find all step names (names with underscores or all caps)
                step_matches = re.findall(r"{'name':\s*'([A-Z_]+)'", phases_content)
            
            return {
                "phases": phase_matches if phase_matches else ["Develop"],
                "steps": step_matches if step_matches else [
                    "START_FEATURE", "CREATE_STRUCTURE", "BUILD_SCAFFOLDING",
                    "DEVELOP_TEST", "WRITE_CODE", "REFACTOR"
                ]
            }
    except Exception:
        pass
    
    # Fallback to known values
    return {
        "phases": ["Develop"],
        "steps": [
            "START_FEATURE", "CREATE_STRUCTURE", "BUILD_SCAFFOLDING",
            "DEVELOP_TEST", "WRITE_CODE", "REFACTOR"
        ]
    }


def format_mcp_servers() -> str:
    """Format MCP servers and tools section"""
    lines = []
    lines.append("## MCP Servers and Tools (in `mcp.json`)")
    lines.append("")
    
    mcp_cfg = read_mcp_config()
    servers = mcp_cfg.get("mcpServers", {})
    
    if not servers:
        lines.append("- No MCP servers configured.")
        return "\n".join(lines) + "\n"
    
    for name, spec in sorted(servers.items()):
        lines.append(f"#### Server: `{name}`")
        
        # Server type and location
        if "command" in spec:
            cmd = spec.get("command", "")
            if cmd == "docker":
                lines.append(f"- **Type:** Docker-based MCP server")
                if "args" in spec and spec["args"]:
                    # Try to extract image from args
                    args = spec["args"]
                    for i, arg in enumerate(args):
                        if "ghcr.io" in arg or "docker.io" in arg:
                            lines.append(f"- rewrite_image: {arg}")
                            break
            elif cmd == "python":
                lines.append(f"- **Type:** Python MCP server")
                if "args" in spec and spec["args"]:
                    # Normalize path to be relative to repo root
                    arg_path = spec['args'][0]
                    if not arg_path.startswith('features/'):
                        # Make it relative if it's not already
                        lines.append(f"- **Location:** `{arg_path}`")
                    else:
                        lines.append(f"- **Location:** `{arg_path}`")
        elif "url" in spec:
            lines.append(f"- **Type:** URL-based MCP server")
            lines.append(f"- **URL:** {spec.get('url')}")
        
        # Tools list
        lines.append("- **Tools:**")
        if name == "tdd-pipeline":
            tools_info = get_tdd_pipeline_tools()
            workflow = get_tdd_pipeline_workflow_steps()
            
            for i, (tool_name, tool_info) in enumerate(sorted(tools_info.items()), 1):
                desc = tool_info.get("description", "")
                example = tool_info.get("example", "")
                lines.append(f"  {i}. `{tool_name}`")
                if desc:
                    lines.append(f"     - {desc}")
                if example:
                    lines.append(f"     - Example: `{example}`")
            
            if not tools_info:
                lines.append("  - (Could not detect tools from server file)")
            
            # Add workflow information
            if workflow:
                lines.append("")
                lines.append("- **Workflow Steps (for skip_to_step):**")
                for step in workflow.get("steps", []):
                    lines.append(f"  - `{step}`")
                
                lines.append("")
                lines.append("- **Workflow Phases:**")
                for phase in workflow.get("phases", []):
                    lines.append(f"  - `{phase}`")
        elif name == "github":
            lines.append("  - All standard GitHub MCP tools (no filtering applied)")
            lines.append("    - Repository operations (create, read, update)")
            lines.append("    - Issue management (create, list, update, get)")
            lines.append("    - Pull request operations (create, list, update, read)")
            lines.append("    - Code search")
            lines.append("    - Branch management (create)")
            lines.append("    - Commit operations (list, get)")
            lines.append("    - File operations (get contents, push, delete)")
            lines.append("    - Comments (add issue comments)")
            lines.append("    - (Full set provided by GitHub MCP server - see GitHub MCP documentation)")
        else:
            lines.append("  - (Tool list not available)")
        lines.append("")
    
    return "\n".join(lines) + "\n"


def format_orphans(orphans: Dict[str, List[str]]) -> str:
    """Format orphaned items for the index."""
    lines = []
    
    lines.append("### Orphaned Rules (in `.cursor/rules/` but no source in `features/*/cursor/`)")
    if orphans["rules"]:
        for rule in sorted(orphans["rules"]):
            lines.append(f"- `{rule}` - **Action:** Assign to appropriate feature or remove")
    else:
        lines.append("- None")
    
    lines.append("\n### Orphaned Commands (in `.cursor/commands/` but no source in `features/*/cursor/`)")
    if orphans["commands"]:
        for cmd in sorted(orphans["commands"]):
            lines.append(f"- `{cmd}` - **Action:** Assign to appropriate feature or remove")
    else:
        lines.append("- None")
    
    lines.append("\n### Orphaned Command Functions (in `commands/` but no source in `features/*/cursor/`)")
    if orphans["command_functions"]:
        for func in sorted(orphans["command_functions"]):
            lines.append(f"- `{func}` - **Action:** Assign to appropriate feature or remove")
    else:
        lines.append("- None")
    
    return "\n".join(lines) + "\n"


def main() -> None:
    print("Scanning codebase for cursor behavior inventory...")
    
    # Scan all features
    feature_dirs = find_feature_cursor_dirs()
    feature_inventories: Dict[str, Dict[str, List[str]]] = {}
    
    for feature_name, base_path in sorted(feature_dirs.items()):
        inventory = scan_feature(feature_name, base_path)
        feature_inventories[feature_name] = inventory
        print(f"  Scanned feature: {feature_name} ({len(inventory['rules'])} rules, {len(inventory['commands'])} commands, {len(inventory['command_functions'])} functions)")
    
    # Scan deployment
    deployed = scan_deployment()
    print(f"  Deployed: {len(deployed['rules'])} rules, {len(deployed['commands'])} commands, {len(deployed['command_functions'])} functions")
    
    # Find orphans
    orphans = find_orphans(feature_inventories, deployed)
    print(f"  Orphans: {len(orphans['rules'])} rules, {len(orphans['commands'])} commands, {len(orphans['command_functions'])} functions")
    
    # Read current index
    if not INDEX_FILE.exists():
        print(f"ERROR: Index file not found: {INDEX_FILE}")
        return
    
    content = INDEX_FILE.read_text(encoding="utf-8")
    
    # Update Current Inventory section
    current_inv_lines = []
    for feature_name in sorted(feature_inventories.keys()):
        current_inv_lines.append(format_feature_inventory(feature_name, feature_inventories[feature_name]))
    
    content = update_index_section(
        content,
        "\n".join(current_inv_lines),
        "## Current Inventory"
    )
    
    # Update Deployment Inventory section
    deployment_content = format_deployment_inventory(deployed)
    content = update_index_section(
        content,
        deployment_content,
        "## Deployment Inventory"
    )
    
    # Update or add MCP Servers section (before Orphaned Behaviors)
    mcp_content = format_mcp_servers()
    mcp_marker = "## MCP Servers and Tools (in `mcp.json`)"
    
    # Remove ALL MCP sections first (handle duplicates)
    # Pattern: marker and everything until next ## header
    pattern = r'## MCP Servers and Tools \(in `mcp\.json`\)' + r'(?:\n## MCP Servers and Tools \(in `mcp\.json`\))*\n.*?(?=\n## |$)'
    content = re.sub(pattern, '', content, flags=re.DOTALL | re.MULTILINE)
    
    # Find insertion point and add single clean section
    orphan_idx = content.find("\n## Orphaned Behaviors")
    if orphan_idx != -1:
        content = content[:orphan_idx].rstrip() + "\n\n" + mcp_content.rstrip() + "\n\n" + content[orphan_idx:]
    else:
        see_also_idx = content.find("\n## See also")
        if see_also_idx != -1:
            content = content[:see_also_idx].rstrip() + "\n\n" + mcp_content.rstrip() + "\n\n" + content[see_also_idx:]
        else:
            content = content.rstrip() + "\n\n" + mcp_content.rstrip() + "\n"
    
    # Update Orphaned Behaviors section
    orphans_content = format_orphans(orphans)
    content = update_index_section(
        content,
        orphans_content,
        "## Orphaned Behaviors"
    )
    
    # Write updated index
    INDEX_FILE.write_text(content, encoding="utf-8")
    print(f"\n[OK] Updated index: {INDEX_FILE.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()

