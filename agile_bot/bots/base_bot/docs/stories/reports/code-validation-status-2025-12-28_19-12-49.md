# Validation Status - code
Started: 2025-12-28 19:12:49
Files: 269

## eliminate_duplication
**rules.py** - 1 violation(s)

[X] ERROR (line 356)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_log_validation_start:356-362):
```python
files = context.get_filtered_files(self)
import json
open('c:\\dev\\augmented-teams\\.cursor\\debug.log', 'a').write(json.dumps({'location': 'rules.py:356', 'message': 'get_filtered_files result', 'da...
```

Location (_process_all_rules:376-385):
```python
processed_rules = []
scanner_status_summary = []
rules_list = list(self)
files = context.get_filtered_files(self)
import json
open('c:\\dev\\augmented-teams\\.cursor\\debug.log', 'a').write(json.dumps...
```

---


## Cross-File Duplication Analysis
Scanning 269 files...
Extracted 4160 code blocks
Starting 8650720 pairwise comparisons...
Comparing: 0% (39,106/8,650,720) - 0 violations - ETA: 2202s  
Comparing: 0% (65,395/8,650,720) - 0 violations - ETA: 2625s  
Comparing: 1% (88,420/8,650,720) - 0 violations - ETA: 2905s  
Comparing: 1% (106,290/8,650,720) - 0 violations - ETA: 3215s  
Comparing: 1% (131,208/8,650,720) - 0 violations - ETA: 3246s  
Comparing: 1% (149,450/8,650,720) - 0 violations - ETA: 3413s  
Comparing: 1% (164,142/8,650,720) - 0 violations - ETA: 3619s  
Comparing: 2% (191,492/8,650,720) - 2 violations - ETA: 3534s  
Comparing: 2% (211,394/8,650,720) - 2 violations - ETA: 3593s  
Comparing: 2% (224,778/8,650,720) - 2 violations - ETA: 3748s  
Comparing: 2% (236,470/8,650,720) - 2 violations - ETA: 3914s  
Comparing: 2% (247,022/8,650,720) - 2 violations - ETA: 4082s  
Comparing: 2% (257,534/8,650,720) - 2 violations - ETA: 4236s  
Comparing: 3% (266,870/8,650,720) - 2 violations - ETA: 4398s  
Comparing: 3% (293,957/8,650,720) - 2 violations - ETA: 4264s  
Comparing: 3% (318,363/8,650,720) - 2 violations - ETA: 4187s  
Comparing: 4% (348,363/8,650,720) - 2 violations - ETA: 4051s  
Comparing: 4% (374,477/8,650,720) - 2 violations - ETA: 3978s  
Comparing: 4% (397,087/8,650,720) - 2 violations - ETA: 3949s  
Comparing: 4% (415,997/8,650,720) - 2 violations - ETA: 3959s  
Comparing: 5% (432,833/8,650,720) - 2 violations - ETA: 3987s  
Comparing: 5% (462,553/8,650,720) - 2 violations - ETA: 3894s  
Comparing: 5% (481,124/8,650,720) - 2 violations - ETA: 3905s  
Comparing: 5% (492,470/8,650,720) - 2 violations - ETA: 3976s  
Comparing: 5% (510,115/8,650,720) - 2 violations - ETA: 3989s  
Comparing: 6% (524,455/8,650,720) - 2 violations - ETA: 4028s  
Comparing: 6% (545,081/8,650,720) - 2 violations - ETA: 4015s  
Comparing: 6% (574,295/8,650,720) - 2 violations - ETA: 3937s  
Found 10 violations so far...
Comparing: 7% (614,065/8,650,720) - 10 violations - ETA: 3795s  
Comparing: 7% (639,316/8,650,720) - 14 violations - ETA: 3759s  
Comparing: 7% (661,671/8,650,720) - 18 violations - ETA: 3743s  
Comparing: 7% (678,649/8,650,720) - 18 violations - ETA: 3759s  
Comparing: 8% (700,852/8,650,720) - 18 violations - ETA: 3743s  
Comparing: 8% (733,759/8,650,720) - 18 violations - ETA: 3668s  
Comparing: 8% (761,964/8,650,720) - 18 violations - ETA: 3623s  
Comparing: 9% (794,093/8,650,720) - 18 violations - ETA: 3561s  
Comparing: 9% (827,184/8,650,720) - 18 violations - ETA: 3499s  
Comparing: 9% (854,701/8,650,720) - 19 violations - ETA: 3466s  
Found 20 violations so far...
Found 30 violations so far...
Found 40 violations so far...
Found 50 violations so far...
Found 60 violations so far...
Found 70 violations so far...
Found 80 violations so far...
Comparing: 10% (895,936/8,650,720) - 82 violations - ETA: 3375s  
Found 90 violations so far...
Found 100 violations so far...
Found 110 violations so far...
Found 120 violations so far...
Found 130 violations so far...
Comparing: 10% (931,223/8,650,720) - 133 violations - ETA: 3316s  
Found 140 violations so far...
Found 150 violations so far...
Comparing: 11% (961,213/8,650,720) - 155 violations - ETA: 3280s  
Comparing: 11% (987,606/8,650,720) - 155 violations - ETA: 3259s  
Comparing: 11% (1,010,482/8,650,720) - 155 violations - ETA: 3251s  
Comparing: 11% (1,034,934/8,650,720) - 155 violations - ETA: 3238s  
Comparing: 12% (1,055,602/8,650,720) - 155 violations - ETA: 3237s  
Comparing: 12% (1,073,918/8,650,720) - 155 violations - ETA: 3245s  
Comparing: 12% (1,094,075/8,650,720) - 155 violations - ETA: 3246s  
Found 160 violations so far...
Found 170 violations so far...
Comparing: 12% (1,116,422/8,650,720) - 171 violations - ETA: 3239s  
Comparing: 13% (1,146,236/8,650,720) - 171 violations - ETA: 3208s  
Comparing: 13% (1,174,979/8,650,720) - 171 violations - ETA: 3181s  
Comparing: 13% (1,204,198/8,650,720) - 171 violations - ETA: 3153s  
Comparing: 14% (1,237,066/8,650,720) - 171 violations - ETA: 3116s  
Comparing: 14% (1,259,182/8,650,720) - 171 violations - ETA: 3111s  
Comparing: 14% (1,274,706/8,650,720) - 171 violations - ETA: 3124s  
Comparing: 14% (1,288,543/8,650,720) - 171 violations - ETA: 3142s  
Found 180 violations so far...
Found 190 violations so far...
Found 200 violations so far...
Comparing: 15% (1,317,585/8,650,720) - 205 violations - ETA: 3116s  
Comparing: 15% (1,347,503/8,650,720) - 205 violations - ETA: 3089s  
Comparing: 15% (1,375,463/8,650,720) - 205 violations - ETA: 3067s  
Comparing: 16% (1,403,896/8,650,720) - 205 violations - ETA: 3045s  
Comparing: 16% (1,431,201/8,650,720) - 205 violations - ETA: 3026s  
Comparing: 16% (1,464,674/8,650,720) - 205 violations - ETA: 2992s  
Comparing: 17% (1,486,653/8,650,720) - 205 violations - ETA: 2987s  
Comparing: 17% (1,504,933/8,650,720) - 205 violations - ETA: 2991s  
Comparing: 17% (1,530,546/8,650,720) - 205 violations - ETA: 2977s  
Comparing: 17% (1,555,595/8,650,720) - 205 violations - ETA: 2964s  
Comparing: 18% (1,576,766/8,650,720) - 205 violations - ETA: 2961s  
Comparing: 18% (1,594,715/8,650,720) - 205 violations - ETA: 2964s  
Comparing: 18% (1,610,040/8,650,720) - 205 violations - ETA: 2973s  
Comparing: 18% (1,626,889/8,650,720) - 205 violations - ETA: 2979s  
Comparing: 19% (1,649,547/8,650,720) - 205 violations - ETA: 2971s  
Comparing: 19% (1,666,956/8,650,720) - 205 violations - ETA: 2974s  
Comparing: 19% (1,687,308/8,650,720) - 205 violations - ETA: 2971s  
Comparing: 19% (1,719,463/8,650,720) - 205 violations - ETA: 2942s  
Comparing: 20% (1,746,686/8,650,720) - 205 violations - ETA: 2925s  
Comparing: 20% (1,773,199/8,650,720) - 205 violations - ETA: 2909s  
Found 210 violations so far...
Comparing: 20% (1,800,457/8,650,720) - 218 violations - ETA: 2891s  
Found 220 violations so far...
Comparing: 21% (1,827,411/8,650,720) - 225 violations - ETA: 2875s  
Comparing: 21% (1,866,483/8,650,720) - 225 violations - ETA: 2835s  
Comparing: 22% (1,908,668/8,650,720) - 225 violations - ETA: 2790s  
Comparing: 22% (1,954,279/8,650,720) - 225 violations - ETA: 2741s  
Comparing: 23% (1,990,162/8,650,720) - 225 violations - ETA: 2711s  
Comparing: 23% (2,016,543/8,650,720) - 228 violations - ETA: 2697s  
Found 230 violations so far...
Comparing: 23% (2,046,200/8,650,720) - 234 violations - ETA: 2679s  
Comparing: 23% (2,074,334/8,650,720) - 234 violations - ETA: 2663s  
Comparing: 24% (2,096,688/8,650,720) - 234 violations - ETA: 2657s  
Comparing: 24% (2,115,791/8,650,720) - 234 violations - ETA: 2656s  
Comparing: 24% (2,138,168/8,650,720) - 234 violations - ETA: 2650s  
Comparing: 24% (2,158,962/8,650,720) - 234 violations - ETA: 2646s  
Comparing: 25% (2,178,577/8,650,720) - 234 violations - ETA: 2644s  
Comparing: 25% (2,205,082/8,650,720) - 234 violations - ETA: 2630s  
Comparing: 25% (2,237,888/8,650,720) - 236 violations - ETA: 2607s  
Comparing: 26% (2,269,954/8,650,720) - 237 violations - ETA: 2586s  
Comparing: 26% (2,293,362/8,650,720) - 237 violations - ETA: 2578s  
Comparing: 26% (2,324,156/8,650,720) - 239 violations - ETA: 2558s  
Comparing: 27% (2,351,596/8,650,720) - 239 violations - ETA: 2544s  
Comparing: 27% (2,370,989/8,650,720) - 239 violations - ETA: 2542s  
Comparing: 27% (2,390,987/8,650,720) - 239 violations - ETA: 2539s  
Comparing: 27% (2,407,429/8,650,720) - 239 violations - ETA: 2541s  
Comparing: 27% (2,421,648/8,650,720) - 239 violations - ETA: 2546s  
Comparing: 28% (2,436,477/8,650,720) - 239 violations - ETA: 2550s  
Comparing: 28% (2,449,349/8,650,720) - 239 violations - ETA: 2557s  
Comparing: 28% (2,461,484/8,650,720) - 239 violations - ETA: 2564s  
Comparing: 28% (2,472,884/8,650,720) - 239 violations - ETA: 2573s  
Comparing: 28% (2,494,465/8,650,720) - 239 violations - ETA: 2566s  
Comparing: 29% (2,522,644/8,650,720) - 239 violations - ETA: 2550s  
Comparing: 29% (2,545,127/8,650,720) - 239 violations - ETA: 2543s  
Comparing: 29% (2,573,979/8,650,720) - 239 violations - ETA: 2526s  
Found 240 violations so far...
Comparing: 30% (2,604,584/8,650,720) - 240 violations - ETA: 2507s  
Comparing: 30% (2,640,081/8,650,720) - 240 violations - ETA: 2481s  
Comparing: 30% (2,670,002/8,650,720) - 240 violations - ETA: 2464s  
Comparing: 31% (2,696,030/8,650,720) - 240 violations - ETA: 2451s  
Comparing: 31% (2,719,278/8,650,720) - 240 violations - ETA: 2443s  
Comparing: 31% (2,740,223/8,650,720) - 240 violations - ETA: 2437s  
Comparing: 32% (2,772,798/8,650,720) - 241 violations - ETA: 2416s  
Found 250 violations so far...
Comparing: 32% (2,800,324/8,650,720) - 251 violations - ETA: 2402s  
Comparing: 32% (2,826,153/8,650,720) - 259 violations - ETA: 2390s  
Comparing: 32% (2,850,284/8,650,720) - 259 violations - ETA: 2381s  
Found 260 violations so far...
Comparing: 33% (2,873,645/8,650,720) - 262 violations - ETA: 2372s  
