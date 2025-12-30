# Validation Status - code
Started: 2025-12-29 17:52:52
Files: 274

## eliminate_duplication
**headless_config.py** - 1 violation(s)

[X] ERROR (line 38)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_loads_api_key:38-42):
```python
config_path = Path(config_path_env)
if config_path.exists():
    config_data = json.loads(config_path.read_text())
    return config_data.get('api_key', '')
```

Location (_loads_log_dir:53-57):
```python
config_path = Path(config_path_env)
if config_path.exists():
    config_data = json.loads(config_path.read_text())
    return Path(config_data.get('log_dir', 'logs'))
```

---


## Cross-File Duplication Analysis
Scanning 1 changed file(s) against 274 total files...
Extracted 8 changed blocks, 4173 reference blocks
Starting 33,384 pairwise comparisons...
Comparing: 5% (1,670/33,384) - 0 violations - ETA: 18s  
Comparing: 10% (3,339/33,384) - 0 violations - ETA: 8s  
Comparing: 15% (5,008/33,384) - 0 violations - ETA: 5s  
Comparing: 20% (6,677/33,384) - 0 violations - ETA: 5s  
Comparing: 25% (8,346/33,384) - 0 violations - ETA: 5s  
Comparing: 30% (10,016/33,384) - 0 violations - ETA: 6s  
Comparing: 35% (11,685/33,384) - 0 violations - ETA: 6s  
Comparing: 40% (13,354/33,384) - 0 violations - ETA: 5s  
Comparing: 45% (15,023/33,384) - 0 violations - ETA: 5s  
Comparing: 50% (16,692/33,384) - 0 violations - ETA: 5s  
Comparing: 55% (18,362/33,384) - 0 violations - ETA: 4s  
Comparing: 60% (20,031/33,384) - 0 violations - ETA: 4s  
Comparing: 65% (21,700/33,384) - 0 violations - ETA: 3s  
Comparing: 70% (23,369/33,384) - 0 violations - ETA: 3s  
Comparing: 75% (25,038/33,384) - 0 violations - ETA: 2s  
Comparing: 80% (26,708/33,384) - 0 violations - ETA: 2s  
Comparing: 85% (28,377/33,384) - 0 violations - ETA: 1s  
Comparing: 90% (30,046/33,384) - 0 violations - ETA: 1s  
Comparing: 95% (31,715/33,384) - 0 violations - ETA: 0s  
Complete: 33320 comparisons, 0 violations

Completed: 2025-12-29 17:53:05
Total violations: 1
Scanners executed: 30
