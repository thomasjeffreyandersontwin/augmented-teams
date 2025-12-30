# Validation Status - code
Started: 2025-12-30 03:00:51
Files: 275

## avoid_excessive_guards
**cli_action_parsers.py** - 1 violation(s)

[!] WARNING (line 96)
Line 96: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
            value = parse_json_dict(value)
        
        if value is not None:
            kwargs[field_name] = value
    
```

---


## Cross-File Duplication Analysis
Scanning 1 changed file(s) against 20 total files...
Extracted 6 changed blocks, 494 reference blocks
Starting 2,964 pairwise comparisons...
Comparing: 5% (149/2,964) - 0 violations - ETA: 18s  
Comparing: 10% (297/2,964) - 0 violations - ETA: 8s  
Comparing: 15% (445/2,964) - 0 violations - ETA: 5s  
Comparing: 20% (593/2,964) - 0 violations - ETA: 3s  
Comparing: 25% (741/2,964) - 0 violations - ETA: 3s  
Comparing: 30% (890/2,964) - 0 violations - ETA: 2s  
Comparing: 35% (1,038/2,964) - 0 violations - ETA: 1s  
Comparing: 40% (1,186/2,964) - 0 violations - ETA: 1s  
Comparing: 45% (1,334/2,964) - 0 violations - ETA: 1s  
Comparing: 50% (1,482/2,964) - 0 violations - ETA: 1s  
Comparing: 55% (1,631/2,964) - 0 violations - ETA: 0s  
Comparing: 60% (1,779/2,964) - 0 violations - ETA: 0s  
Comparing: 65% (1,927/2,964) - 0 violations - ETA: 0s  
Comparing: 70% (2,075/2,964) - 0 violations - ETA: 0s  
Comparing: 75% (2,223/2,964) - 0 violations - ETA: 0s  
Comparing: 80% (2,372/2,964) - 0 violations - ETA: 0s  
Comparing: 85% (2,520/2,964) - 0 violations - ETA: 0s  
Comparing: 90% (2,668/2,964) - 0 violations - ETA: 0s  
Comparing: 95% (2,816/2,964) - 0 violations - ETA: 0s  
Complete: 2928 comparisons, 0 violations

## use_domain_language
**cli_action_parsers.py** - 2 violation(s)

[i] INFO (line 83)
Function "build_context_from_parsed" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 83)
Function "build_context_from_parsed" uses parameter name "parsed_args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

Completed: 2025-12-30 03:00:54
Total violations: 3
Scanners executed: 30
