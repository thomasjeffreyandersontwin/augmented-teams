# Validation Status - code
Started: 2025-12-18 16:54:28
Files: 1

## delegate_to_lowest_level
**bot.py** - 1 violation(s)

[i] INFO (line 43)
Method "__init__" in class "Bot" iterates through "behaviors" instead of delegating to collection class. Delegate to collection class instead.

---

## separate_concerns
**bot.py** - 1 violation(s)

[X] ERROR (line 27)
Function "__init__" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.

---

Completed: 2025-12-18 16:54:30
Total violations: 2
Scanners executed: 49
: 25% (58/231) - 0 violations - ETA: 2s
Comparing: 30% (70/231) - 0 violations - ETA: 2s
Comparing: 35% (81/231) - 0 violations - ETA: 1s
Comparing: 40% (93/231) - 0 violations - ETA: 1s
Comparing: 45% (104/231) - 0 violations - ETA: 1s
Comparing: 50% (116/231) - 0 violations - ETA: 0s
Comparing: 55% (128/231) - 0 violations - ETA: 0s
Comparing: 60% (139/231) - 0 violations - ETA: 0s
Comparing: 65% (151/231) - 0 violations - ETA: 0s
Comparing: 70% (162/231) - 0 violations - ETA: 0s
Comparing: 75% (174/231) - 0 violations - ETA: 0s
Comparing: 80% (185/231) - 0 violations - ETA: 0s
Comparing: 85% (197/231) - 0 violations - ETA: 0s
Comparing: 90% (208/231) - 0 violations - ETA: 0s
Comparing: 95% (220/231) - 0 violations - ETA: 0s
Comparing: 100% (231/231) - 0 violations - ETA: 0s
Complete: 231 comparisons, 0 violations

