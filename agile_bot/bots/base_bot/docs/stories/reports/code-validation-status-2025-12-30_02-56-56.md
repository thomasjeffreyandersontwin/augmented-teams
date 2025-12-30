# Validation Status - code
Started: 2025-12-30 02:56:56
Files: 275

## avoid_excessive_guards
**cli_action_parsers.py** - 1 violation(s)

[!] WARNING (line 88)
Line 88: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
            value = parse_json_dict(value)
        
        if value is not None:
            kwargs[field_name] = value
    
```

---


## Cross-File Duplication Analysis
Scanning 1 changed file(s) against 20 total files...
Extracted 7 changed blocks, 495 reference blocks
Starting 3,465 pairwise comparisons...
Comparing: 5% (174/3,465) - 0 violations - ETA: 18s  
Comparing: 10% (347/3,465) - 0 violations - ETA: 8s  
Comparing: 15% (520/3,465) - 0 violations - ETA: 5s  
Comparing: 20% (693/3,465) - 0 violations - ETA: 4s  
Comparing: 25% (867/3,465) - 0 violations - ETA: 2s  
Comparing: 30% (1,040/3,465) - 0 violations - ETA: 2s  
Comparing: 35% (1,213/3,465) - 0 violations - ETA: 1s  
Comparing: 40% (1,386/3,465) - 0 violations - ETA: 1s  
Comparing: 45% (1,560/3,465) - 0 violations - ETA: 1s  
Comparing: 50% (1,733/3,465) - 0 violations - ETA: 0s  
Comparing: 55% (1,906/3,465) - 0 violations - ETA: 0s  
Comparing: 60% (2,079/3,465) - 0 violations - ETA: 0s  
Comparing: 65% (2,253/3,465) - 0 violations - ETA: 0s  
Comparing: 70% (2,426/3,465) - 0 violations - ETA: 0s  
Comparing: 75% (2,599/3,465) - 0 violations - ETA: 0s  
Comparing: 80% (2,772/3,465) - 0 violations - ETA: 0s  
Comparing: 85% (2,946/3,465) - 0 violations - ETA: 0s  
Comparing: 90% (3,119/3,465) - 0 violations - ETA: 0s  
Comparing: 95% (3,292/3,465) - 0 violations - ETA: 0s  
Complete: 3416 comparisons, 0 violations

## use_domain_language
**cli_action_parsers.py** - 2 violation(s)

[i] INFO (line 75)
Function "build_context_from_parsed" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 75)
Function "build_context_from_parsed" uses parameter name "parsed_args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

Completed: 2025-12-30 02:56:59
Total violations: 3
Scanners executed: 30
