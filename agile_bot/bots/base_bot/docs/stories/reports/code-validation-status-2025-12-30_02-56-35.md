# Validation Status - code
Started: 2025-12-30 02:56:35
Files: 275

## avoid_excessive_guards
**cli_action_parsers.py** - 1 violation(s)

[!] WARNING (line 85)
Line 85: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
            value = parse_json_dict(value)
        
        if value is not None:
            kwargs[field_name] = value
    
```

---


## Cross-File Duplication Analysis
Scanning 2 changed file(s) against 20 total files...
Extracted 7 changed blocks, 494 reference blocks
Starting 3,458 pairwise comparisons...
Comparing: 5% (173/3,458) - 0 violations - ETA: 18s  
Comparing: 10% (346/3,458) - 0 violations - ETA: 8s  
Comparing: 15% (519/3,458) - 0 violations - ETA: 5s  
Comparing: 20% (692/3,458) - 0 violations - ETA: 3s  
Comparing: 25% (865/3,458) - 0 violations - ETA: 2s  
Comparing: 30% (1,038/3,458) - 0 violations - ETA: 2s  
Comparing: 35% (1,211/3,458) - 0 violations - ETA: 1s  
Comparing: 40% (1,384/3,458) - 0 violations - ETA: 1s  
Comparing: 45% (1,557/3,458) - 0 violations - ETA: 1s  
Comparing: 50% (1,729/3,458) - 0 violations - ETA: 1s  
Comparing: 55% (1,902/3,458) - 0 violations - ETA: 0s  
Comparing: 60% (2,075/3,458) - 0 violations - ETA: 0s  
Comparing: 65% (2,248/3,458) - 0 violations - ETA: 0s  
Comparing: 70% (2,421/3,458) - 0 violations - ETA: 0s  
Comparing: 75% (2,594/3,458) - 0 violations - ETA: 0s  
Comparing: 80% (2,767/3,458) - 0 violations - ETA: 0s  
Comparing: 85% (2,940/3,458) - 0 violations - ETA: 0s  
Comparing: 90% (3,113/3,458) - 0 violations - ETA: 0s  
Comparing: 95% (3,286/3,458) - 0 violations - ETA: 0s  
Complete: 3422 comparisons, 0 violations

## use_domain_language
**cli_action_parsers.py** - 2 violation(s)

[i] INFO (line 72)
Function "build_context_from_parsed" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 72)
Function "build_context_from_parsed" uses parameter name "parsed_args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

## use_domain_language
**path_resolver.py** - 5 violation(s)

[i] INFO (line 8)
Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 21)
Function "_resolve_with_repo_root" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 28)
Function "_resolve_with_workspace_or_cwd" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 39)
Function "expand_path_if_needed" uses parameter name "expand_fn" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 54)
Function "_find_repo_root" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

Completed: 2025-12-30 02:56:39
Total violations: 8
Scanners executed: 30
