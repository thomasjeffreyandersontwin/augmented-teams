"""
BDD Test File Validation
Validates actual test files against BDD principles using AI semantic analysis.
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Any, Optional

# Step 2: Detect framework from file path
def detect_framework_from_file(file_path: str) -> Optional[str]:
    """
    Match file path against rule glob patterns to determine framework.
    Returns: 'jest', 'mamba', or None
    """
    file_path_lower = file_path.lower()
    
    # Jest patterns
    jest_patterns = ['.test.js', '.spec.js', '.test.ts', '.spec.ts', 
                     '.test.jsx', '.spec.jsx', '.test.tsx', '.spec.tsx']
    
    # Mamba patterns  
    mamba_patterns = ['_test.py', 'test_', '_spec.py', 'spec_', 
                      '_test.pyi', 'test_.pyi', '_spec.pyi', 'spec_.pyi']
    
    for pattern in jest_patterns:
        if file_path_lower.endswith(pattern):
            return 'jest'
    
    for pattern in mamba_patterns:
        if pattern in file_path_lower:
            return 'mamba'
    
    return None


# Step 3: Load framework-specific rule file
def load_rule_file(framework: str) -> Dict[str, Any]:
    """
    Load the appropriate framework-specific rule file.
    Returns: {"rule_path": Path, "content": str, "framework": str}
    """
    rule_files = {
        'jest': 'bdd-jest-behavior-rule.mdc',
        'mamba': 'bdd-mamba-behavior-rule.mdc'
    }
    
    rule_file = rule_files.get(framework)
    if not rule_file:
        return None
    
    rule_path = Path("behaviors/bdd-behavior") / rule_file
    if not rule_path.exists():
        return None
    
    content = rule_path.read_text(encoding='utf-8')
    
    return {
        "rule_path": str(rule_path),
        "content": content,
        "framework": framework
    }


# Step 4: Extract DO and DON'T examples by section
def extract_dos_and_donts(rule_content: str) -> Dict[str, Dict[str, List[str]]]:
    """
    Extract DO and DON'T examples from each section (§1-5) of the rule.
    Returns: {"section_name": {"dos": [...], "donts": [...]}}
    """
    import re
    
    sections = {}
    current_section = None
    
    lines = rule_content.split('\n')
    for i, line in enumerate(lines):
        # Detect section headers (## 1. Section Name)
        section_match = re.match(r'^##\s+(\d+)\.\s+(.+)$', line)
        if section_match:
            section_num = section_match.group(1)
            section_name = section_match.group(2).strip()
            current_section = f"{section_num}. {section_name}"
            sections[current_section] = {"dos": [], "donts": []}
        
        # Extract DO examples
        if '**✅ DO:**' in line or '**DO:**' in line:
            # Find code block after this
            code_block = []
            in_code = False
            for j in range(i+1, min(i+50, len(lines))):
                if lines[j].strip().startswith('```') and not in_code:
                    in_code = True
                    continue
                elif lines[j].strip().startswith('```') and in_code:
                    break
                elif in_code:
                    code_block.append(lines[j])
            
            if code_block and current_section:
                sections[current_section]["dos"].append('\n'.join(code_block))
        
        # Extract DON'T examples
        if '**❌ DON\'T:**' in line or '**DON\'T:**' in line or "**DON'T:**" in line:
            # Find code block after this
            code_block = []
            in_code = False
            for j in range(i+1, min(i+50, len(lines))):
                if lines[j].strip().startswith('```') and not in_code:
                    in_code = True
                    continue
                elif lines[j].strip().startswith('```') and in_code:
                    break
                elif in_code:
                    code_block.append(lines[j])
            
            if code_block and current_section:
                sections[current_section]["donts"].append('\n'.join(code_block))
    
    return sections


# Step 4b: Load reference file for thorough mode
def load_reference_file(framework: str) -> Optional[str]:
    """
    Load detailed examples from reference file for thorough validation.
    Returns: reference file content or None
    """
    reference_files = {
        'jest': 'bdd-jest-behavior-reference.md',
        'mamba': 'bdd-mamba-behavior-reference.md'
    }
    
    ref_file = reference_files.get(framework)
    if not ref_file:
        return None
    
    ref_path = Path("behaviors/bdd-behavior") / ref_file
    if not ref_path.exists():
        return None
    
    return ref_path.read_text(encoding='utf-8')


# Step 5: Perform minimal static checks
def perform_static_checks(test_file_path: str, framework: str) -> List[Dict[str, Any]]:
    """
    Perform basic static analysis that doesn't require AI.
    Returns: [{"line": int, "issue": str, "type": "error|warning"}]
    """
    issues = []
    
    try:
        content = Path(test_file_path).read_text(encoding='utf-8')
        lines = content.split('\n')
        
        for i, line in enumerate(lines, 1):
            # Check for missing "should" in it() statements
            if framework == 'jest':
                if "it('" in line or 'it("' in line:
                    # Extract the description
                    import re
                    match = re.search(r"it\(['\"]([^'\"]+)['\"]", line)
                    if match:
                        desc = match.group(1)
                        if not desc.strip().lower().startswith('should'):
                            issues.append({
                                "line": i,
                                "issue": f"it() description missing 'should' prefix: '{desc}'",
                                "type": "warning",
                                "rule": "1. Business Readable Language"
                            })
            
            elif framework == 'mamba':
                if "with it('" in line or 'with it("' in line:
                    import re
                    match = re.search(r"with it\(['\"]([^'\"]+)['\"]", line)
                    if match:
                        desc = match.group(1)
                        if not desc.strip().lower().startswith('should'):
                            issues.append({
                                "line": i,
                                "issue": f"it() description missing 'should' prefix: '{desc}'",
                                "type": "warning",
                                "rule": "1. Business Readable Language"
                            })
            
            # Check for _private method calls
            if '._' in line and 'toHaveBeenCalled' in line:
                issues.append({
                    "line": i,
                    "issue": "Testing private method (likely implementation detail)",
                    "type": "warning",
                    "rule": "2. Comprehensive and Brief"
                })
    
    except Exception as e:
        issues.append({
            "line": 0,
            "issue": f"Error reading file: {e}",
            "type": "error"
        })
    
    return issues


# Step 6-9: AI evaluation against DO/DON'T examples (using OpenAI function calling)
def evaluate_test_with_ai(test_file_path: str, test_content: str, framework: str, 
                          sections: Dict[str, Dict[str, List[str]]], thorough: bool = False) -> Dict[str, Any]:
    """
    Use OpenAI function calling to evaluate test file against ALL DO/DON'T examples.
    
    Args:
        test_file_path: Path to test file
        test_content: Test file content
        framework: 'jest' or 'mamba'
        sections: Extracted DO/DON'T examples by section
        thorough: If True, also load and evaluate against reference file examples
    
    Returns: {"violations": [...], "passes": [...], "section_results": {...}}
    """
    try:
        from openai import OpenAI
    except ImportError:
        return {"error": "OpenAI package not installed. Install with: pip install openai"}
    
    # Load .env file
    try:
        from dotenv import load_dotenv
        features_env = Path("behaviors/.env")
        root_env = Path(".env")
        if features_env.exists():
            load_dotenv(features_env, override=True)
        elif root_env.exists():
            load_dotenv(root_env, override=True)
        else:
            load_dotenv(override=True)
    except ImportError:
        pass
    
    # Initialize OpenAI client
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return {"error": "OPENAI_API_KEY environment variable not set"}
    
    client = OpenAI(api_key=api_key)
    
    # Define function schema for BDD validation
    BDD_VALIDATION_SCHEMA = {
        "name": "validate_bdd_test",
        "description": "Validate test file against BDD principles with specific DO/DON'T examples",
        "parameters": {
            "type": "object",
            "properties": {
                "violations": {
                    "type": "array",
                    "description": "Test code that violates BDD principles",
                    "items": {
                        "type": "object",
                        "properties": {
                            "line": {"type": "integer", "description": "Line number of violation"},
                            "code": {"type": "string", "description": "Code snippet with violation"},
                            "section": {"type": "string", "description": "Which section (1-5) this violates"},
                            "violated_principle": {"type": "string", "description": "Which specific DO or DON'T was violated"},
                            "why_wrong": {"type": "string", "description": "Why this violates the principle"},
                            "suggested_fix": {"type": "string", "description": "How to fix it based on DO examples"}
                        },
                        "required": ["line", "section", "violated_principle", "why_wrong"]
                    }
                },
                "passes": {
                    "type": "array",
                    "description": "Test code that correctly follows BDD principles",
                    "items": {
                        "type": "object",
                        "properties": {
                            "line": {"type": "integer", "description": "Line number"},
                            "code": {"type": "string", "description": "Code snippet"},
                            "section": {"type": "string", "description": "Which section (1-5)"},
                            "followed_principle": {"type": "string", "description": "Which DO principle was followed"}
                        },
                        "required": ["line", "section", "followed_principle"]
                    }
                },
                "section_summaries": {
                    "type": "object",
                    "description": "Summary for each section",
                    "additionalProperties": {
                        "type": "object",
                        "properties": {
                            "compliant": {"type": "boolean"},
                            "notes": {"type": "string"}
                        }
                    }
                }
            },
            "required": ["violations", "passes", "section_summaries"]
        }
    }
    
    # Build prompt with all DO/DON'T examples
    prompt_parts = [
        f"Validate this {framework.upper()} test file against BDD principles.",
        f"\nTest file: {test_file_path}",
        "\n--- TEST FILE CONTENT ---",
        test_content,
        "\n--- BDD PRINCIPLES TO EVALUATE ---"
    ]
    
    for section_name, examples in sections.items():
        prompt_parts.append(f"\n## {section_name}")
        prompt_parts.append(f"DO examples ({len(examples['dos'])} total):")
        for i, do_ex in enumerate(examples['dos'], 1):
            prompt_parts.append(f"DO #{i}:\n{do_ex}")
        
        prompt_parts.append(f"\nDON'T examples ({len(examples['donts'])} total):")
        for i, dont_ex in enumerate(examples['donts'], 1):
            prompt_parts.append(f"DON'T #{i}:\n{dont_ex}")
    
    # Step 7: If thorough mode, add detailed examples from reference file
    if thorough:
        ref_content = load_reference_file(framework)
        if ref_content:
            prompt_parts.append("\n--- DETAILED EXAMPLES (THOROUGH MODE) ---")
            prompt_parts.append(ref_content[:10000])  # Limit to avoid token overflow
            prompt_parts.append("\n\nUse these detailed examples for comprehensive edge case validation.")
    
    prompt_parts.append("\n\nEvaluate EVERY describe/it block against ALL DO and DON'T examples above.")
    prompt_parts.append("Report violations with specific line numbers and which principle was violated.")
    
    prompt = '\n'.join(prompt_parts)
    
    # Call OpenAI with function calling
    try:
        print(f"🤖 Using OpenAI to evaluate test against BDD principles...")
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": f"You are an expert at evaluating {framework.upper()} tests against BDD principles. Analyze test code for violations and provide specific, actionable feedback."},
                {"role": "user", "content": prompt}
            ],
            functions=[BDD_VALIDATION_SCHEMA],
            function_call={"name": "validate_bdd_test"}
        )
        
        if response.choices[0].message.function_call:
            result = json.loads(response.choices[0].message.function_call.arguments)
            return result
        else:
            return {"error": "OpenAI did not return function call result"}
            
    except Exception as e:
        return {"error": f"Error calling OpenAI: {e}"}


# Step 10: Compile results
def compile_validation_results(static_issues: List[Dict], ai_results: Dict[str, Any]) -> Dict[str, Any]:
    """Combine static and AI results into final report."""
    all_violations = static_issues + ai_results.get("violations", [])
    passes = ai_results.get("passes", [])
    
    return {
        "total_violations": len(all_violations),
        "total_passes": len(passes),
        "violations": sorted(all_violations, key=lambda x: x.get("line", 0)),
        "passes": passes,
        "section_summaries": ai_results.get("section_summaries", {})
    }


# Step 11: Generate report
def generate_validation_report(test_file_path: str, framework: str, results: Dict[str, Any]) -> str:
    """Generate human-readable validation report."""
    lines = [
        "=" * 60,
        f"BDD Test Validation: {Path(test_file_path).name} ({framework.upper()})",
        "=" * 60,
        ""
    ]
    
    # Violations
    violations = results.get("violations", [])
    if violations:
        lines.append(f"❌ Found {len(violations)} violation(s):\n")
        for v in violations:
            lines.append(f"Line {v.get('line', '?')}: {v.get('code', v.get('issue', 'Unknown'))}")
            lines.append(f"   Violation: {v.get('violated_principle', v.get('rule', 'Unknown'))}")
            lines.append(f"   Why: {v.get('why_wrong', 'See rule for details')}")
            if 'suggested_fix' in v:
                lines.append(f"   Fix: {v['suggested_fix']}")
            lines.append("")
    
    # Passes
    passes = results.get("passes", [])
    if passes:
        lines.append(f"✅ Following {len(passes)} principle(s) correctly:\n")
        for p in passes[:5]:  # Show first 5
            lines.append(f"Line {p.get('line', '?')}: {p.get('followed_principle', 'Unknown')}")
        if len(passes) > 5:
            lines.append(f"... and {len(passes) - 5} more")
        lines.append("")
    
    # Summary
    lines.extend([
        "=" * 60,
        "Validation Summary",
        "=" * 60,
        f"❌ {len(violations)} violations",
        f"✅ {len(passes)} principles followed",
        ""
    ])
    
    return '\n'.join(lines)


# Main validation orchestrator
def bdd_validate_test_file(file_path: Optional[str] = None, thorough: bool = False):
    """
    Main function to validate a BDD test file.
    
    Steps:
    1. Get file path (from arg or current file)
    2. Detect framework from file path
    3. Load framework-specific rule
    4. Extract DO/DON'T examples by section
    5. Perform static checks
    6-9. AI evaluates test against each section's DO/DON'Ts
    10. Compile results
    11. Generate report
    12. Ask user for action
    """
    
    # Step 1: Get file path
    if not file_path:
        print("❌ No file path provided. Use: \\bdd-validate <file-path>")
        return {"error": "No file path provided"}
    
    test_path = Path(file_path)
    if not test_path.exists():
        print(f"❌ File not found: {file_path}")
        return {"error": "File not found"}
    
    # Step 2: Detect framework
    framework = detect_framework_from_file(file_path)
    if not framework:
        print(f"❌ File doesn't match BDD test patterns: {file_path}")
        print("   Expected: *.test.js, *.spec.ts, test_*.py, etc.")
        return {"error": "Not a BDD test file"}
    
    print(f"✅ Detected framework: {framework.upper()}")
    
    # Step 3: Load rule file
    rule_data = load_rule_file(framework)
    if not rule_data:
        print(f"❌ Could not load rule file for {framework}")
        return {"error": "Rule file not found"}
    
    print(f"✅ Loaded rule: {rule_data['rule_path']}")
    
    # Step 4: Extract DO/DON'T examples
    sections = extract_dos_and_donts(rule_data['content'])
    total_dos = sum(len(s['dos']) for s in sections.values())
    total_donts = sum(len(s['donts']) for s in sections.values())
    print(f"✅ Extracted {total_dos} DO examples and {total_donts} DON'T examples from {len(sections)} sections")
    
    # Step 5: Static checks
    print("📋 Running static analysis...")
    static_issues = perform_static_checks(file_path, framework)
    if static_issues:
        print(f"   Found {len(static_issues)} static issues")
    
    # Step 6-9: AI evaluation
    if thorough:
        print("🤖 Running AI semantic evaluation against BDD principles (THOROUGH MODE with reference examples)...")
    else:
        print("🤖 Running AI semantic evaluation against BDD principles...")
    
    test_content = test_path.read_text(encoding='utf-8')
    ai_results = evaluate_test_with_ai(file_path, test_content, framework, sections, thorough)
    
    if "error" in ai_results:
        print(f"❌ {ai_results['error']}")
        return ai_results
    
    # Step 10: Compile results
    final_results = compile_validation_results(static_issues, ai_results)
    
    # Step 11: Generate report
    report = generate_validation_report(file_path, framework, final_results)
    print(report)
    
    # Return structured results
    return final_results


if __name__ == "__main__":
    import sys
    from runner_guard import require_command_invocation
    
    # GUARD: Ensure this runner is called from its Cursor command, not directly
    require_command_invocation("bdd-behavior-validate")
    
    file_path = sys.argv[1] if len(sys.argv) > 1 else None
    thorough = '--thorough' in sys.argv
    
    if not file_path:
        print("Usage: python bdd-behavior-validate-cmd.py <test-file-path> [--thorough]")
        print("\nExample:")
        print("  python bdd-behavior-validate-cmd.py src/components/User.test.js")
        print("  python bdd-behavior-validate-cmd.py test_user_service.py --thorough")
        sys.exit(1)
    
    result = bdd_validate_test_file(file_path, thorough)
    
    # Exit with error code if violations found
    if result.get("total_violations", 0) > 0:
        sys.exit(1)
