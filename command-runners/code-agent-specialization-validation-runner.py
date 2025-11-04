def validate_hierarchical_behavior(feature_name):
    """
    Generic validation for hierarchical behavior patterns.
    
    INHERITS base validation from behavior_structure():
    - File naming patterns (feature-name-type.ext)
    - Rule/command relationships
    - Governance sections (When/Then, Executing Commands, etc.)
    
    ADDS hierarchical-specific validation:
    - isHierarchical flag in config
    - hierarchy section (baseRule, specializedRules, referenceFiles)
    - File existence checks for declared hierarchy files
    - Cross-references (base ↔ specialized, specialized ↔ reference)
    - Structural alignment (principle numbering, section organization)
    
    Args:
        feature_name: Name of the feature to validate (e.g., "bdd-behavior")
    
    Returns:
        dict: Validation results with issue counts and details
    """
    from pathlib import Path
    import json
    import sys
    import io
    import importlib.util
    
    # Fix Windows console encoding for emoji support
    if sys.platform == "win32":
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    
    # Import module with hyphens using importlib
    common_path = Path(__file__).parent / "code-agent-common.py"
    spec = importlib.util.spec_from_file_location("code_agent_common", common_path)
    common = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(common)
    find_deployed_behaviors = common.find_deployed_behaviors
    
    # Find the feature directory dynamically
    behaviors_root = Path("behaviors")
    feature_dir = behaviors_root / feature_name
    if not (feature_dir / "behavior.json").exists():
        # Try to find it dynamically
        all_behaviors = find_deployed_behaviors()
        matching = [b for b in all_behaviors if b.name == feature_name]
        feature_dir = matching[0] if matching else feature_dir
    
    if not feature_dir.exists():
        print(f"❌ Feature directory not found: {feature_dir}")
        return {"error": "Feature not found"}
    
    print("=" * 60)
    print(f"Hierarchical Behavior Validation: {feature_name}")
    print("=" * 60)
    
    # ========================================================================
    # STEP 1: INHERIT - Run base structure validation
    # ========================================================================
    # This validates ALL standard behavior structure requirements:
    # - Naming patterns, rule/command relationships, governance sections
    print("\n📋 Step 1: Running base structure validation (inherited)...")
    
    try:
        # Import and call base validation function
        spec = importlib.util.spec_from_file_location(
            "code_agent_behavior_structure_cmd",
            Path("commands") / "code-agent-structure-cmd.py"
        )
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            behavior_structure = module.behavior_structure
            
            # Call inherited base validation
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
    
    # ========================================================================
    # STEP 2: EXTEND - Add hierarchical-specific validation
    # ========================================================================
    # This adds ONLY hierarchical pattern checks, not duplicating base logic
    print("\n📋 Step 2: Validating hierarchical structure (extended)...")
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
            "hierarchical": False,
            "specialized_issues": 0,
            "warnings": 0
        }
    
    try:
        config = json.loads(config_file.read_text(encoding='utf-8'))
    except json.JSONDecodeError as e:
        issues.append(f"Invalid JSON in config: {e}")
        print(f"❌ Invalid JSON in config: {e}")
        return {"base": base_result, "specialized_issues": len(issues), "warnings": 0}
    
    # 2.1: Check if hierarchical pattern is declared
    if not config.get("isHierarchical"):
        print("ℹ️  Not configured as hierarchical behavior (base validation only)")
        return {
            "base": base_result,
            "hierarchical": False,
            "specialized_issues": 0,
            "warnings": 0
        }
    
    print("✅ Feature marked as hierarchical")
    
    hierarchy = config.get("hierarchy", {})
    
    # 2.2: Validate hierarchy configuration exists
    if not hierarchy:
        issues.append("Hierarchical behavior missing 'hierarchy' section in config")
        print("❌ Missing 'hierarchy' section in config")
    
    # 2.3: Validate base rule declaration and cross-references
    base_rule_name = hierarchy.get("baseRule")
    if not base_rule_name:
        issues.append("Hierarchical behavior missing 'hierarchy.baseRule' in config")
        print("❌ Missing 'hierarchy.baseRule' in config")
    else:
        base_rule = feature_dir / base_rule_name
        if not base_rule.exists():
            issues.append(f"Missing declared base rule: {base_rule_name}")
            print(f"❌ Missing declared base rule: {base_rule_name}")
        else:
            print(f"✅ Base rule exists: {base_rule_name}")
            
            # Check that base rule references specialized rules
            content = base_rule.read_text(encoding='utf-8')
            specialized_rules = hierarchy.get("specializedRules", [])
            
            for specialized_rule_name in specialized_rules:
                if specialized_rule_name not in content:
                    warnings.append(f"Base rule doesn't reference specialized rule: {specialized_rule_name}")
                    print(f"⚠️  Base rule doesn't reference: {specialized_rule_name}")
    
    # 2.4: Validate specialized rules declaration and cross-references
    specialized_rules = hierarchy.get("specializedRules", [])
    if not specialized_rules:
        warnings.append("Hierarchical behavior has no specialized rules declared")
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
    
    # 2.5: Validate reference files declaration and links
    reference_files = hierarchy.get("referenceFiles", [])
    if not reference_files:
        warnings.append("Hierarchical behavior has no reference files declared")
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
    
    # ========================================================================
    # STEP 3: Report combined results (base + hierarchical)
    # ========================================================================
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
        print("\nHierarchical Issues:")
        for issue in issues:
            print(f"  • {issue}")
    
    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print(f"  • {warning}")
    
    return {
        "base": base_result,
        "hierarchical": True,
        "specialized_issues": len(issues),
        "warnings": len(warnings),
        "issues_list": issues,
        "warnings_list": warnings,
        "total_issues": total_issues
    }


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python code-agent-specialization-validate-cmd.py <feature-name>")
        print("\nExample:")
        print("  python code-agent-specialization-validate-cmd.py bdd-behavior")
        sys.exit(1)
    
    feature = sys.argv[1]
    result = validate_hierarchical_behavior(feature)
    
    # Exit with error code if issues found
    if result.get("total_issues", 0) > 0:
        sys.exit(1)

