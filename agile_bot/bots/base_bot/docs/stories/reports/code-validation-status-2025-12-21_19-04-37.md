# Validation Status - code
Started: 2025-12-21 19:04:37
Files: 228

## avoid_excessive_guards
**action.py** - 1 violation(s)

[!] WARNING (line 162)
Line 162: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

---

## avoid_excessive_guards
**actions.py** - 1 violation(s)

[!] WARNING (line 183)
Line 183: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

---

## avoid_excessive_guards
**action_context.py** - 1 violation(s)

[!] WARNING (line 32)
Line 32: Variable truthiness check detected (if not data:). Assume variable exists - let code fail fast if missing.

---

## avoid_excessive_guards
**code_scanner.py** - 1 violation(s)

[!] WARNING (line 38)
Line 38: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

---

## avoid_excessive_guards
**cover_all_paths_scanner.py** - 1 violation(s)

[!] WARNING (line 40)
Line 40: Variable truthiness check detected (if has_code:). Assume variable exists - let code fail fast if missing.

---

## avoid_excessive_guards
**scanner_orchestrator.py** - 1 violation(s)

[!] WARNING (line 47)
Line 47: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

---

## avoid_excessive_guards
**violation.py** - 1 violation(s)

[!] WARNING (line 57)
Line 57: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

---

## avoid_excessive_guards
**rules.py** - 2 violation(s)

[!] WARNING (line 45)
Line 45: Variable truthiness check detected (if has_scope_in_params:). Assume variable exists - let code fail fast if missing.

[!] WARNING (line 142)
Line 142: Variable truthiness check detected (if changed:). Assume variable exists - let code fail fast if missing.

---

## avoid_excessive_guards
**file_link_builder.py** - 2 violation(s)

[!] WARNING (line 24)
Line 24: Variable truthiness check detected (if not is_absolute:). Assume variable exists - let code fail fast if missing.

[!] WARNING (line 47)
Line 47: Variable truthiness check detected (if line_number:). Assume variable exists - let code fail fast if missing.

---

## avoid_excessive_guards
**block.py** - 5 violation(s)

[!] WARNING (line 63)
Line 63: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

[!] WARNING (line 68)
Line 68: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

[!] WARNING (line 73)
Line 73: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

[!] WARNING (line 79)
Line 79: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

[!] WARNING (line 85)
Line 85: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

---

## chain_dependencies_properly
**prefer_object_model_over_config_scanner.py** - 1 violation(s)

[!] WARNING (line 36)
Method "scan_file" in class "PreferObjectModelOverConfigScanner" takes parameter "rule_obj" that is already injected in __init__. Use self.rule_obj instead.

---

## chain_dependencies_properly
**scanner_orchestrator.py** - 1 violation(s)

[!] WARNING (line 27)
Method "selects_scanner_helpers_by_rule" in class "ScannerOrchestrator" takes parameter "scanner_registry" that is already injected in __init__. Use self.scanner_registry instead.

---

## chain_dependencies_properly
**rule_loader.py** - 1 violation(s)

[!] WARNING (line 22)
Method "_load_rules_from_glob" in class "RuleLoader" takes parameter "behavior" that is already injected in __init__. Use self.behavior instead.

---

## chain_dependencies_properly
**validation_scope.py** - 1 violation(s)

[!] WARNING (line 41)
Method "_extract_skiprule_from_scope" in class "ValidationScope" takes parameter "parameters" that is already injected in __init__. Use self.parameters instead.

---

## eliminate_duplication
**help_renderer.py** - 1 violation(s)

[X] ERROR (line 9)
Duplicate code detected: functions render_header, _format_behavior_command, _format_behavior_title, _format_action_command have identical bodies - extract to shared function

---

## eliminate_duplication
**scanner.py** - 1 violation(s)

[X] ERROR (line 50)
Duplicate code detected: functions scan_file, scan_cross_file, _scan_block have identical bodies - extract to shared function

---

## eliminate_duplication
**test_scanner.py** - 1 violation(s)

[X] ERROR (line 26)
Duplicate code detected: functions scan_file, scan_cross_file have identical bodies - extract to shared function

---

## eliminate_duplication
**rules_action.py** - 1 violation(s)

[X] ERROR (line 42)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_add_rules_context:42-51):
```python
instructions.add('')
instructions.add(rules_digest)
instructions.add('')
instructions.add('CRITICAL: The rules digest above contains everything you need to get started.')
instructions.add('')
instruct...
```

Location (_add_rules_context:52-57):
```python
instructions.add('   - The full rule has detailed examples and detection patterns')
instructions.add('4. Cite rule names when making decisions')
instructions.add('')
instructions.add('The digest gives...
```

---

## eliminate_duplication
**validation_report_writer.py** - 1 violation(s)

[X] ERROR (line 149)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_get_status_path:149-153):
```python
docs_path = self.bot_paths.documentation_path
docs_dir = self.workspace_directory / docs_path / 'reports'
docs_dir.mkdir(parents=True, exist_ok=True)
status_file = docs_dir / f'{self.behavior_name}-va...
```

Location (get_report_path:240-244):
```python
docs_path = self.bot_paths.documentation_path
docs_dir = self.workspace_directory / docs_path / 'reports'
docs_dir.mkdir(parents=True, exist_ok=True)
report_file = docs_dir / f'{self.behavior_name}-va...
```

---


## Cross-File Duplication Analysis
Scanning 228 files...
Extracted 3254 code blocks
Starting 5292631 pairwise comparisons...
Comparing: 0% (30,455/5,292,631) - 0 violations - ETA: 1728s  
Comparing: 0% (51,654/5,292,631) - 0 violations - ETA: 2029s  
Comparing: 1% (74,260/5,292,631) - 0 violations - ETA: 2108s  
Comparing: 1% (94,047/5,292,631) - 0 violations - ETA: 2211s  
Comparing: 2% (113,687/5,292,631) - 0 violations - ETA: 2277s  
Comparing: 2% (137,082/5,292,631) - 0 violations - ETA: 2256s  
Comparing: 2% (151,749/5,292,631) - 0 violations - ETA: 2371s  
Comparing: 3% (181,797/5,292,631) - 0 violations - ETA: 2249s  
Comparing: 3% (195,456/5,292,631) - 0 violations - ETA: 2347s  
Comparing: 3% (208,462/5,292,631) - 0 violations - ETA: 2439s  
Comparing: 4% (220,318/5,292,631) - 0 violations - ETA: 2532s  
Comparing: 4% (230,638/5,292,631) - 0 violations - ETA: 2633s  
Comparing: 4% (262,164/5,292,631) - 0 violations - ETA: 2494s  
Comparing: 5% (287,111/5,292,631) - 0 violations - ETA: 2440s  
Comparing: 5% (309,133/5,292,631) - 0 violations - ETA: 2418s  
Comparing: 6% (328,684/5,292,631) - 0 violations - ETA: 2416s  
Comparing: 6% (355,632/5,292,631) - 0 violations - ETA: 2360s  
Comparing: 7% (373,863/5,292,631) - 0 violations - ETA: 2368s  
Comparing: 7% (387,695/5,292,631) - 0 violations - ETA: 2403s  
Comparing: 7% (403,969/5,292,631) - 0 violations - ETA: 2420s  
Comparing: 8% (424,984/5,292,631) - 0 violations - ETA: 2405s  
Comparing: 8% (447,095/5,292,631) - 0 violations - ETA: 2384s  
Comparing: 8% (474,428/5,292,631) - 1 violations - ETA: 2335s  
Comparing: 9% (506,877/5,292,631) - 1 violations - ETA: 2266s  
Comparing: 10% (530,777/5,292,631) - 1 violations - ETA: 2243s  
Comparing: 10% (545,100/5,292,631) - 1 violations - ETA: 2264s  
Comparing: 10% (563,713/5,292,631) - 1 violations - ETA: 2265s  
Found 10 violations so far...
Found 20 violations so far...
Found 30 violations so far...
Found 40 violations so far...
Found 50 violations so far...
Comparing: 11% (606,426/5,292,631) - 54 violations - ETA: 2163s  
Found 60 violations so far...
Comparing: 12% (638,778/5,292,631) - 64 violations - ETA: 2112s  
Comparing: 12% (666,741/5,292,631) - 64 violations - ETA: 2081s  
Comparing: 13% (691,762/5,292,631) - 64 violations - ETA: 2061s  
Comparing: 13% (714,929/5,292,631) - 64 violations - ETA: 2049s  
Comparing: 13% (733,901/5,292,631) - 64 violations - ETA: 2049s  
Comparing: 14% (761,813/5,292,631) - 65 violations - ETA: 2022s  
Comparing: 14% (792,984/5,292,631) - 65 violations - ETA: 1986s  
Comparing: 15% (828,712/5,292,631) - 65 violations - ETA: 1939s  
Comparing: 16% (853,007/5,292,631) - 65 violations - ETA: 1925s  
Comparing: 16% (868,735/5,292,631) - 65 violations - ETA: 1935s  
Found 70 violations so far...
Found 80 violations so far...
Comparing: 16% (892,199/5,292,631) - 87 violations - ETA: 1923s  
Found 90 violations so far...
Comparing: 17% (921,646/5,292,631) - 93 violations - ETA: 1897s  
Comparing: 18% (953,238/5,292,631) - 93 violations - ETA: 1866s  
Comparing: 18% (979,889/5,292,631) - 93 violations - ETA: 1848s  
Comparing: 18% (999,479/5,292,631) - 93 violations - ETA: 1847s  
Comparing: 19% (1,026,072/5,292,631) - 93 violations - ETA: 1829s  
Comparing: 19% (1,048,680/5,292,631) - 93 violations - ETA: 1821s  
Comparing: 20% (1,068,329/5,292,631) - 93 violations - ETA: 1819s  
Comparing: 20% (1,084,336/5,292,631) - 93 violations - ETA: 1824s  
Comparing: 20% (1,106,004/5,292,631) - 93 violations - ETA: 1817s  
Comparing: 21% (1,123,814/5,292,631) - 93 violations - ETA: 1817s  
Comparing: 21% (1,147,010/5,292,631) - 94 violations - ETA: 1807s  
Comparing: 22% (1,174,440/5,292,631) - 94 violations - ETA: 1788s  
Comparing: 22% (1,202,354/5,292,631) - 94 violations - ETA: 1769s  
Comparing: 23% (1,240,923/5,292,631) - 94 violations - ETA: 1730s  
Comparing: 24% (1,284,501/5,292,631) - 94 violations - ETA: 1685s  
Comparing: 25% (1,330,327/5,292,631) - 94 violations - ETA: 1638s  
Comparing: 25% (1,369,909/5,292,631) - 97 violations - ETA: 1603s  
Comparing: 26% (1,397,355/5,292,631) - 97 violations - ETA: 1589s  
Comparing: 26% (1,420,928/5,292,631) - 97 violations - ETA: 1580s  
Comparing: 27% (1,444,025/5,292,631) - 97 violations - ETA: 1572s  
Comparing: 27% (1,464,453/5,292,631) - 97 violations - ETA: 1568s  
Comparing: 28% (1,491,293/5,292,631) - 97 violations - ETA: 1554s  
Comparing: 28% (1,509,751/5,292,631) - 97 violations - ETA: 1553s  
Comparing: 28% (1,533,727/5,292,631) - 98 violations - ETA: 1544s  
Comparing: 29% (1,559,233/5,292,631) - 99 violations - ETA: 1532s  
Found 100 violations so far...
Found 110 violations so far...
Found 120 violations so far...
Comparing: 30% (1,601,459/5,292,631) - 125 violations - ETA: 1498s  
Found 130 violations so far...
Comparing: 30% (1,633,228/5,292,631) - 132 violations - ETA: 1478s  
Comparing: 31% (1,663,106/5,292,631) - 132 violations - ETA: 1462s  
Comparing: 31% (1,693,178/5,292,631) - 132 violations - ETA: 1445s  
Comparing: 32% (1,712,997/5,292,631) - 132 violations - ETA: 1441s  
Comparing: 32% (1,729,839/5,292,631) - 132 violations - ETA: 1441s  
Comparing: 32% (1,745,406/5,292,631) - 132 violations - ETA: 1443s  
Comparing: 33% (1,759,650/5,292,631) - 132 violations - ETA: 1445s  
Comparing: 33% (1,772,487/5,292,631) - 132 violations - ETA: 1449s  
Comparing: 33% (1,783,950/5,292,631) - 132 violations - ETA: 1455s  
Comparing: 34% (1,810,742/5,292,631) - 132 violations - ETA: 1442s  
Comparing: 34% (1,837,510/5,292,631) - 132 violations - ETA: 1429s  
Comparing: 35% (1,865,238/5,292,631) - 132 violations - ETA: 1414s  
Comparing: 35% (1,898,781/5,292,631) - 132 violations - ETA: 1394s  
Comparing: 36% (1,928,877/5,292,631) - 132 violations - ETA: 1377s  
Comparing: 36% (1,956,557/5,292,631) - 132 violations - ETA: 1364s  
Comparing: 37% (1,982,487/5,292,631) - 132 violations - ETA: 1352s  
Comparing: 37% (2,008,872/5,292,631) - 132 violations - ETA: 1340s  
Comparing: 38% (2,032,196/5,292,631) - 132 violations - ETA: 1331s  
Comparing: 38% (2,048,748/5,292,631) - 132 violations - ETA: 1330s  
Comparing: 38% (2,053,958/5,292,631) - 132 violations - ETA: 1340s  
Comparing: 38% (2,059,182/5,292,631) - 132 violations - ETA: 1350s  
Comparing: 39% (2,064,582/5,292,631) - 132 violations - ETA: 1360s  
Comparing: 39% (2,069,895/5,292,631) - 132 violations - ETA: 1370s  
Comparing: 39% (2,081,308/5,292,631) - 132 violations - ETA: 1373s  
Comparing: 39% (2,104,861/5,292,631) - 139 violations - ETA: 1363s  
Comparing: 40% (2,119,794/5,292,631) - 139 violations - ETA: 1362s  
Comparing: 40% (2,131,859/5,292,631) - 139 violations - ETA: 1364s  
Comparing: 40% (2,158,593/5,292,631) - 139 violations - ETA: 1350s  
Comparing: 41% (2,180,204/5,292,631) - 139 violations - ETA: 1342s  
Comparing: 41% (2,209,779/5,292,631) - 139 violations - ETA: 1325s  
Comparing: 42% (2,245,264/5,292,631) - 139 violations - ETA: 1303s  
Comparing: 42% (2,271,187/5,292,631) - 139 violations - ETA: 1290s  
Comparing: 43% (2,295,342/5,292,631) - 139 violations - ETA: 1279s  
Found 140 violations so far...
Comparing: 43% (2,320,831/5,292,631) - 140 violations - ETA: 1267s  
Comparing: 44% (2,330,217/5,292,631) - 141 violations - ETA: 1271s  
Comparing: 44% (2,352,621/5,292,631) - 142 violations - ETA: 1262s  
Comparing: 44% (2,375,555/5,292,631) - 142 violations - ETA: 1252s  
Comparing: 45% (2,387,512/5,292,631) - 142 violations - ETA: 1253s  
Comparing: 45% (2,399,439/5,292,631) - 142 violations - ETA: 1254s  
Comparing: 45% (2,427,874/5,292,631) - 142 violations - ETA: 1239s  
Comparing: 46% (2,448,842/5,292,631) - 142 violations - ETA: 1231s  
Comparing: 46% (2,466,635/5,292,631) - 142 violations - ETA: 1225s  
Comparing: 46% (2,483,201/5,292,631) - 142 violations - ETA: 1221s  
Comparing: 47% (2,498,677/5,292,631) - 142 violations - ETA: 1218s  
Comparing: 47% (2,512,515/5,292,631) - 142 violations - ETA: 1217s  
Comparing: 47% (2,526,364/5,292,631) - 142 violations - ETA: 1215s  
Comparing: 47% (2,538,321/5,292,631) - 142 violations - ETA: 1215s  
Comparing: 48% (2,557,703/5,292,631) - 144 violations - ETA: 1208s  
Comparing: 48% (2,592,647/5,292,631) - 144 violations - ETA: 1187s  
Comparing: 49% (2,618,492/5,292,631) - 144 violations - ETA: 1174s  
Comparing: 49% (2,638,929/5,292,631) - 144 violations - ETA: 1166s  
Comparing: 50% (2,657,075/5,292,631) - 144 violations - ETA: 1160s  
Comparing: 50% (2,687,065/5,292,631) - 145 violations - ETA: 1144s  
Comparing: 51% (2,720,946/5,292,631) - 145 violations - ETA: 1124s  
Found 150 violations so far...
Found 160 violations so far...
Found 170 violations so far...
Found 180 violations so far...
Found 190 violations so far...
Found 200 violations so far...
Found 210 violations so far...
Found 220 violations so far...
Found 230 violations so far...
Comparing: 52% (2,756,072/5,292,631) - 234 violations - ETA: 1104s  
Found 240 violations so far...
Found 250 violations so far...
Found 260 violations so far...
Found 270 violations so far...
Comparing: 52% (2,785,115/5,292,631) - 279 violations - ETA: 1089s  
Found 280 violations so far...
Found 290 violations so far...
Comparing: 53% (2,813,324/5,292,631) - 292 violations - ETA: 1075s  
Found 300 violations so far...
Comparing: 53% (2,843,833/5,292,631) - 302 violations - ETA: 1059s  
Comparing: 54% (2,877,777/5,292,631) - 303 violations - ETA: 1040s  
Comparing: 54% (2,901,160/5,292,631) - 303 violations - ETA: 1030s  
Comparing: 55% (2,921,802/5,292,631) - 303 violations - ETA: 1022s  
Comparing: 55% (2,940,629/5,292,631) - 303 violations - ETA: 1015s  
Comparing: 55% (2,957,075/5,292,631) - 303 violations - ETA: 1011s  
Comparing: 56% (2,972,558/5,292,631) - 303 violations - ETA: 1006s  
Comparing: 56% (2,995,126/5,292,631) - 303 violations - ETA: 997s  
Comparing: 57% (3,017,158/5,292,631) - 303 violations - ETA: 988s  
Found 310 violations so far...
Found 320 violations so far...
Found 330 violations so far...
Found 340 violations so far...
Found 350 violations so far...
Comparing: 57% (3,048,751/5,292,631) - 352 violations - ETA: 971s  
Found 360 violations so far...
Found 370 violations so far...
Found 380 violations so far...
Comparing: 58% (3,081,842/5,292,631) - 386 violations - ETA: 954s  
Found 390 violations so far...
Found 400 violations so far...
Found 410 violations so far...
Comparing: 58% (3,113,729/5,292,631) - 411 violations - ETA: 937s  
Comparing: 59% (3,142,649/5,292,631) - 415 violations - ETA: 923s  
Found 420 violations so far...
Found 430 violations so far...
Comparing: 60% (3,176,626/5,292,631) - 437 violations - ETA: 905s  
Found 440 violations so far...
Comparing: 60% (3,197,645/5,292,631) - 441 violations - ETA: 897s  
Found 450 violations so far...
Found 460 violations so far...
Found 470 violations so far...
Found 480 violations so far...
Comparing: 61% (3,231,643/5,292,631) - 486 violations - ETA: 880s  
Comparing: 61% (3,259,292/5,292,631) - 488 violations - ETA: 867s  
Found 490 violations so far...
Found 500 violations so far...
Found 510 violations so far...
Found 520 violations so far...
Comparing: 62% (3,298,113/5,292,631) - 521 violations - ETA: 846s  
Found 530 violations so far...
Found 540 violations so far...
Found 550 violations so far...
Found 560 violations so far...
Found 570 violations so far...
Found 580 violations so far...
Found 590 violations so far...
Found 600 violations so far...
Found 610 violations so far...
Comparing: 62% (3,327,840/5,292,631) - 614 violations - ETA: 832s  
