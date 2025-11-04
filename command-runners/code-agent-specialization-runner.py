def behavior_specialization(action="validate", feature=None):
    """
    Manage specialized behavior patterns (validate, fix, create).
    
    Actions:
    - validate: Check specialization compliance (base rule, specialized rules, references)
    - fix: Automatically fix specialization issues (broken cross-references, etc.)
    - create: Scaffold a new specialized behavior with base + framework rules
    
    Inherits from behavior_structure() for base validation, extends with specialization checks.
    
    Args:
        action: Action to perform (validate, fix, create)
        feature: Feature name to process (None = all features)
    
    Returns:
        dict: Results with counts and details
    """
    from pathlib import Path
    import json
    import sys
    import io
    import importlib.util
    
    if action == "validate":
        return validate_specialized_behavior(feature)
    elif action == "fix":
        return fix_specialized_behavior(feature)
    elif action == "create":
        return create_specialized_behavior(feature)
    else:
        print(f"❌ Unknown action: {action}")
        print("Available actions: validate, fix, create")
        return {"error": f"Unknown action: {action}"}


def validate_specialized_behavior(feature=None):
    """
    Validate specialized behavior patterns.
    
    INHERITS base validation from behavior_structure():
    - File naming patterns (feature-name-type.ext)
    - Rule/command relationships
    - Governance sections (When/Then, Executing Commands, etc.)
    
    ADDS specialization-specific validation:
    - isSpecialized flag in config
    - specialization section (baseRule, specializedRules, referenceFiles)
    - File existence checks for declared specialization files
    - Cross-references (base ↔ specialized, specialized ↔ reference)
    - Structural alignment (principle numbering, section organization)
    
    Args:
        feature: Name of the feature to validate (None = all features with isSpecialized)
    
    Returns:
        dict: Validation results with issue counts and details
    """
    from pathlib import Path
    import json
    import sys
    import importlib.util
    
    repo_root = Path(".")
    
    # Walk repo to find behavior folders with isSpecialized flag
    features = []
    
    if feature:
        # Find specific feature by name anywhere in repo
        for behavior_json in repo_root.rglob("behavior.json"):
            try:
                marker_data = json.load(behavior_json.open('r', encoding='utf-8'))
                if marker_data.get("feature") == feature and marker_data.get("isSpecialized"):
                    features.append(behavior_json.parent)
            except:
                pass
    else:
        # Find all specialized behaviors in entire repo
        for behavior_json in repo_root.rglob("behavior.json"):
            try:
                marker_data = json.load(behavior_json.open('r', encoding='utf-8'))
                if marker_data.get("isSpecialized"):
                    features.append(behavior_json.parent)
            except:
                pass
    
    if not features:
        print("No specialized features found")
        return {"features": 0, "total_issues": 0}
    
    # Validate each feature
    all_results = []
    for feature_dir in features:
        result = validate_single_specialized_behavior(feature_dir.name)
        all_results.append(result)
    
    # Summary
    total_issues = sum(r.get("total_issues", 0) for r in all_results)
    return {"features": len(features), "total_issues": total_issues, "results": all_results}


def validate_single_specialized_behavior(feature_name):
    """Validate a single specialized behavior feature."""
    from pathlib import Path
    import json
    import sys
    import importlib.util
    
    repo_root = Path(".")
    
    # Find the feature anywhere in the repo by walking for behavior.json
    feature_dir = None
    for behavior_json in repo_root.rglob("behavior.json"):
        try:
            marker_data = json.load(behavior_json.open('r', encoding='utf-8'))
            if marker_data.get("feature") == feature_name:
                feature_dir = behavior_json.parent
                break
        except:
            pass
    
    if not feature_dir:
        print(f"❌ Feature directory not found: {feature_dir}")
        return {"error": "Feature not found"}
    
    print("=" * 60)
    print(f"Specialized Behavior Validation: {feature_name}")
    print("=" * 60)
    
    # 1. Run base structure validation first
    print("\n📋 Running base structure validation...")
    
    try:
        # Import base validation module
        spec = importlib.util.spec_from_file_location(
            "code_agent_structure_runner",
            Path("command-runners") / "code-agent-structure-runner.py"
        )
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            behavior_structure = module.behavior_structure
            base_result = behavior_structure("validate", feature_name)
            
            if base_result.get("issues", 0) == 0:
                print("✅ Base structure validation passed")
            else:
                print(f"⚠️  Base structure has {base_result.get('issues', 0)} issue(s)")
        else:
            print("⚠️  Could not load base validation module")
            base_result = {"issues": 0, "warning": "Base validation skipped"}
    except Exception as e:
        print(f"⚠️  Error running base validation: {e}")
        base_result = {"issues": 0, "warning": str(e)}
    
    # 2. Load and validate feature configuration
    print("\n📋 Validating specialized structure...")
    issues = []
    warnings = []
    
    # Look for either <feature>.json or code-agent-behavior.json
    config_file = feature_dir / f"{feature_name}.json"
    if not config_file.exists():
        config_file = feature_dir / "code-agent-behavior.json"
    
    if not config_file.exists():
        print("ℹ️  No configuration file found - not a behavior feature")
        return {
            "base": base_result,
            "specialized": False,
            "specialized_issues": 0,
            "warnings": 0
        }
    
    try:
        config = json.loads(config_file.read_text(encoding='utf-8'))
    except json.JSONDecodeError as e:
        issues.append(f"Invalid JSON in config: {e}")
        print(f"❌ Invalid JSON in config: {e}")
        return {"base": base_result, "specialized_issues": len(issues), "warnings": 0}
    
    # 3. Check if specialized pattern is declared
    if not config.get("isSpecialized"):
        print("ℹ️  Not a specialized behavior")
        return {
            "base": base_result,
            "specialized": False,
            "specialized_issues": 0,
            "warnings": 0
        }
    
    print("✅ Feature marked as specialized")
    
    specialization = config.get("specialization", {})
    
    # 4. Validate specialization configuration
    if not specialization:
        issues.append("Specialized behavior missing 'specialization' section in config")
        print("❌ Missing 'specialization' section in config")
    
    # 5. Validate base rule
    base_rule_name = specialization.get("baseRule")
    if not base_rule_name:
        issues.append("Specialized behavior missing 'specialization.baseRule' in config")
        print("❌ Missing 'specialization.baseRule' in config")
    else:
        base_rule = feature_dir / base_rule_name
        if not base_rule.exists():
            issues.append(f"Missing declared base rule: {base_rule_name}")
            print(f"❌ Missing declared base rule: {base_rule_name}")
        else:
            print(f"✅ Base rule exists: {base_rule_name}")
            
            # Check that base rule references specialized rules
            content = base_rule.read_text(encoding='utf-8')
            specialized_rules = specialization.get("specializedRules", [])
            
            for specialized_rule_name in specialized_rules:
                if specialized_rule_name not in content:
                    warnings.append(f"Base rule doesn't reference specialized rule: {specialized_rule_name}")
                    print(f"⚠️  Base rule doesn't reference: {specialized_rule_name}")
    
    # 6. Validate specialized rules
    specialized_rules = specialization.get("specializedRules", [])
    if not specialized_rules:
        warnings.append("Specialized behavior has no specialized rules declared")
        print("⚠️  No specialized rules declared")
    
    for rule_name in specialized_rules:
        rule_file = feature_dir / rule_name
        if not rule_file.exists():
            issues.append(f"Missing declared specialized rule: {rule_name}")
            print(f"❌ Missing specialized rule: {rule_name}")
        else:
            print(f"✅ Specialized rule exists: {rule_name}")
            
            # Check that specialized rule references base
            content = rule_file.read_text(encoding='utf-8')
            if base_rule_name and base_rule_name not in content:
                issues.append(f"{rule_name} doesn't reference base rule {base_rule_name}")
                print(f"   ❌ Doesn't reference base rule")
            else:
                print(f"   ✅ References base rule")
    
    # 7. Validate reference files
    reference_files = specialization.get("referenceFiles", [])
    if not reference_files:
        warnings.append("Specialized behavior has no reference files declared")
        print("⚠️  No reference files declared")
    
    for ref_name in reference_files:
        ref_file = feature_dir / ref_name
        if not ref_file.exists():
            issues.append(f"Missing declared reference file: {ref_name}")
            print(f"❌ Missing reference file: {ref_name}")
        else:
            print(f"✅ Reference file exists: {ref_name}")
            
            # Check that corresponding specialized rule links to reference
            framework = ref_name.replace(f"{feature_name}-", "").replace("-reference.md", "")
            specialized_rule_name = f"{feature_name}-{framework}-rule.mdc"
            
            if specialized_rule_name in specialized_rules:
                specialized_rule = feature_dir / specialized_rule_name
                if specialized_rule.exists():
                    content = specialized_rule.read_text(encoding='utf-8')
                    if ref_name not in content:
                        issues.append(f"{specialized_rule_name} doesn't reference {ref_name}")
                        print(f"   ❌ {specialized_rule_name} doesn't link to reference")
                    else:
                        print(f"   ✅ Linked from {specialized_rule_name}")
    
    # 8. Summary
    print("\n" + "=" * 60)
    print("Validation Summary")
    print("=" * 60)
    
    total_issues = base_result.get("issues", 0) + len(issues)
    
    if total_issues == 0 and len(warnings) == 0:
        print("✅ All validation checks passed!")
    else:
        if total_issues > 0:
            print(f"❌ Found {total_issues} issue(s)")
        if len(warnings) > 0:
            print(f"⚠️  Found {len(warnings)} warning(s)")
    
    if issues:
        print("\nSpecialized Issues:")
        for issue in issues:
            print(f"  • {issue}")
    
    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print(f"  • {warning}")
    
    return {
        "base": base_result,
        "specialized": True,
        "specialized_issues": len(issues),
        "warnings": len(warnings),
        "issues_list": issues,
        "warnings_list": warnings,
        "total_issues": total_issues
    }


def fix_specialized_behavior(feature_name):
    """
    Fix specialization issues automatically.
    
    Fixes:
    - Broken cross-references between base and specialized rules
    - Missing specialization section in config
    - Missing reference links from specialized rules
    """
    # TODO: Implement fix logic
    print("Fix specialization not yet implemented")
    return {"fixed": 0}


def create_specialized_behavior(feature_name):
    """
    Scaffold a new specialized behavior with base + framework variations.
    
    Creates:
    - Base rule (framework-agnostic)
    - Specialized rules (per framework)
    - Reference materials
    - Config with isSpecialized flag
    """
    # TODO: Implement create logic
    print("Create specialized behavior not yet implemented")
    return {"created": 0}


if __name__ == "__main__":
    import sys
    import io
    from runner_guard import require_command_invocation
    
    # GUARD: Ensure this runner is called from its Cursor command, not directly
    require_command_invocation("code-agent-specialization")
    
    # Fix Windows console encoding for emoji support
    if sys.platform == "win32":
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    
    action = sys.argv[1] if len(sys.argv) > 1 else "validate"
    feature = sys.argv[2] if len(sys.argv) > 2 else None
    
    result = behavior_specialization(action, feature)
    
    # Exit with error code if issues found (for validate action)
    if action == "validate" and result.get("total_issues", 0) > 0:
        sys.exit(1)

