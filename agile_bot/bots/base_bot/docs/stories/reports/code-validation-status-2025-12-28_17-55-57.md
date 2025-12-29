# Validation Status - code
Started: 2025-12-28 17:55:57
Files: 269

## avoid_excessive_guards
**actions.py** - 1 violation(s)

[!] WARNING (line 185)
Line 185: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    def is_final_action(self) -> bool:
        try:
            if self.current is None:
                return False
            action_names = self.names
```

---

## avoid_excessive_guards
**action_context.py** - 1 violation(s)

[!] WARNING (line 146)
Line 146: Variable truthiness check detected (if not data:). Assume variable exists - let code fail fast if missing.

```python
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Scope':
        if not data:
            return cls()
        
```

---

## avoid_excessive_guards
**repl_session.py** - 1 violation(s)

[!] WARNING (line 1109)
Line 1109: Variable truthiness check detected (if not args:). Assume variable exists - let code fail fast if missing.

```python
    def parse_command_parameters(self, args: str) -> Dict[str, Any]:
        params = {}
        if not args:
            return params
        
```

---

## avoid_excessive_guards
**cli_bot.py** - 2 violation(s)

[!] WARNING (line 44)
Line 44: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    @property
    def help(self) -> REPLHelp:
        if self._help is None:
            self._help = REPLHelp(self._bot)
        return self._help
```

[!] WARNING (line 50)
Line 50: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    @property
    def status(self) -> REPLStatus:
        if self._status is None:
            self._status = REPLStatus(self, self._session, self._session.formatter)
        return self._status
```

---

## avoid_excessive_guards
**markdown_formatter.py** - 2 violation(s)

[!] WARNING (line 15)
Line 15: Variable truthiness check detected (if is_completed:). Assume variable exists - let code fail fast if missing.

```python
    
    def status_marker(self, is_current: bool, is_completed: bool) -> str:
        if is_completed:
            return "- ☑"
        elif is_current:
            return "- ➤"
        else:
            return "- ☐"
    
```

[!] WARNING (line 17)
Line 17: Variable truthiness check detected (if is_current:). Assume variable exists - let code fail fast if missing.

```python
        if is_completed:
            return "- ☑"
        elif is_current:
            return "- ➤"
        else:
            return "- ☐"
    
```

---

## avoid_excessive_guards
**terminal_formatter.py** - 2 violation(s)

[!] WARNING (line 15)
Line 15: Variable truthiness check detected (if is_completed:). Assume variable exists - let code fail fast if missing.

```python
    
    def status_marker(self, is_current: bool, is_completed: bool) -> str:
        if is_completed:
            return "[OK]"
        elif is_current:
            return "[*]"
        else:
            return "[ ]"
    
```

[!] WARNING (line 17)
Line 17: Variable truthiness check detected (if is_current:). Assume variable exists - let code fail fast if missing.

```python
        if is_completed:
            return "[OK]"
        elif is_current:
            return "[*]"
        else:
            return "[ ]"
    
```

---

## avoid_excessive_guards
**cli_action.py** - 1 violation(s)

[!] WARNING (line 36)
Line 36: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
            self._session.set_action_phase('instructions')
            # If a context object is provided, use it directly; otherwise parse from args
            if context is None:
                context = self._parse_args_to_context(args)
            result = self._action.get_instructions(context)
```

---

## delegate_to_lowest_level
**repl_help.py** - 1 violation(s)

[i] INFO (line 24)
Method "format_as_lines" in class "StageCollection" iterates through "_stages" instead of delegating to collection class. Delegate to collection class instead.

---

## eliminate_duplication
**repl_session.py** - 2 violation(s)

[X] ERROR (line 192)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (display_current_state:192-205):
```python
lines.append(str(self.workspace_directory))
lines.append('```')
lines.append('')
lines.append('To change path:')
lines.append('```')
lines.append('path demo/mob_minion              # Change to specifi...
```

Location (display_current_state:220-228):
```python
lines.append(formatter.subsection_separator())
lines.append(f'## {formatter.position_icon()} **Progress**')
lines.append('**Current Position:**')
lines.append('```')
lines.append(f'{self.progress_path...
```

[X] ERROR (line 449)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_handle_next_command:449-468):
```python
if not self.has_current_action:
    return REPLCommandResponse(output='ERROR: No current action', response='ERROR: No current action', status='error')
behavior = self.current_behavior
if not behavior:...
```

Location (_handle_back_command:485-504):
```python
if not self.has_current_action:
    return REPLCommandResponse(output='ERROR: No current action', response='ERROR: No current action', status='error')
behavior = self.current_behavior
if not behavior:...
```

---

## eliminate_duplication
**repl_status.py** - 1 violation(s)

[X] ERROR (line 137)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (hierarchical_status:137-148):
```python
lines.append('')
lines.append('Run:')
lines.append('```')
lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
lines.append("echo '[behavior][.action]' | python rep...
```

Location (hierarchical_status:149-158):
```python
lines.append('')
lines.append('```')
lines.append('// Run')
lines.append("echo '[command]' | python repl_main.py")
lines.append('// to invoke commands')
lines.append('```')
lines.append('')
lines.appe...
```

---

## eliminate_duplication
**output_formatter.py** - 1 violation(s)

[X] ERROR (line 16)
Duplicate code detected: functions status_marker, list_item, highlight have identical bodies - extract to shared function

---


## Cross-File Duplication Analysis
Scanning 269 files...
Extracted 4095 code blocks
Starting 8382465 pairwise comparisons...
Comparing: 0% (30,998/8,382,465) - 0 violations - ETA: 2694s  
Comparing: 0% (57,103/8,382,465) - 0 violations - ETA: 2916s  
Comparing: 0% (78,060/8,382,465) - 0 violations - ETA: 3191s  
Comparing: 1% (96,251/8,382,465) - 0 violations - ETA: 3443s  
Comparing: 1% (112,881/8,382,465) - 0 violations - ETA: 3663s  
Comparing: 1% (133,435/8,382,465) - 0 violations - ETA: 3709s  
Comparing: 1% (149,848/8,382,465) - 0 violations - ETA: 3845s  
Comparing: 1% (163,719/8,382,465) - 0 violations - ETA: 4016s  
Comparing: 2% (190,456/8,382,465) - 2 violations - ETA: 3871s  
Comparing: 2% (209,111/8,382,465) - 2 violations - ETA: 3908s  
Comparing: 2% (221,601/8,382,465) - 2 violations - ETA: 4051s  
Comparing: 2% (233,208/8,382,465) - 2 violations - ETA: 4193s  
Comparing: 2% (243,767/8,382,465) - 2 violations - ETA: 4340s  
Comparing: 3% (253,929/8,382,465) - 2 violations - ETA: 4481s  
Comparing: 3% (263,225/8,382,465) - 2 violations - ETA: 4626s  
Comparing: 3% (290,559/8,382,465) - 2 violations - ETA: 4456s  
Comparing: 3% (313,415/8,382,465) - 2 violations - ETA: 4376s  
Comparing: 4% (343,173/8,382,465) - 2 violations - ETA: 4216s  
Comparing: 4% (368,280/8,382,465) - 2 violations - ETA: 4134s  
Comparing: 4% (389,458/8,382,465) - 2 violations - ETA: 4104s  
Comparing: 4% (408,757/8,382,465) - 2 violations - ETA: 4096s  
Comparing: 5% (425,695/8,382,465) - 2 violations - ETA: 4112s  
Comparing: 5% (454,540/8,382,465) - 2 violations - ETA: 4011s  
Comparing: 5% (472,967/8,382,465) - 2 violations - ETA: 4013s  
Comparing: 5% (483,707/8,382,465) - 2 violations - ETA: 4082s  
Comparing: 5% (500,894/8,382,465) - 2 violations - ETA: 4091s  
Comparing: 6% (515,170/8,382,465) - 2 violations - ETA: 4123s  
Comparing: 6% (535,326/8,382,465) - 2 violations - ETA: 4104s  
Comparing: 6% (566,435/8,382,465) - 6 violations - ETA: 4001s  
Found 10 violations so far...
Comparing: 7% (605,333/8,382,465) - 10 violations - ETA: 3854s  
Comparing: 7% (629,898/8,382,465) - 14 violations - ETA: 3815s  
Comparing: 7% (651,693/8,382,465) - 18 violations - ETA: 3796s  
Comparing: 7% (668,670/8,382,465) - 18 violations - ETA: 3807s  
Comparing: 8% (691,013/8,382,465) - 18 violations - ETA: 3784s  
Comparing: 8% (722,649/8,382,465) - 18 violations - ETA: 3710s  
Comparing: 8% (750,465/8,382,465) - 18 violations - ETA: 3661s  
Comparing: 9% (781,511/8,382,465) - 18 violations - ETA: 3598s  
Comparing: 9% (813,515/8,382,465) - 18 violations - ETA: 3535s  
Comparing: 10% (839,061/8,382,465) - 19 violations - ETA: 3506s  
Found 20 violations so far...
Found 30 violations so far...
Found 40 violations so far...
Found 50 violations so far...
Found 60 violations so far...
Found 70 violations so far...
Found 80 violations so far...
Comparing: 10% (879,800/8,382,465) - 82 violations - ETA: 3411s  
Found 90 violations so far...
Found 100 violations so far...
Found 110 violations so far...
Found 120 violations so far...
Found 130 violations so far...
Comparing: 10% (914,369/8,382,465) - 133 violations - ETA: 3348s  
Found 140 violations so far...
Found 150 violations so far...
Comparing: 11% (944,512/8,382,465) - 155 violations - ETA: 3307s  
Comparing: 11% (970,221/8,382,465) - 155 violations - ETA: 3285s  
Comparing: 11% (992,217/8,382,465) - 155 violations - ETA: 3277s  
Comparing: 12% (1,016,460/8,382,465) - 155 violations - ETA: 3261s  
Comparing: 12% (1,037,032/8,382,465) - 155 violations - ETA: 3258s  
Comparing: 12% (1,054,811/8,382,465) - 155 violations - ETA: 3265s  
Comparing: 12% (1,071,999/8,382,465) - 155 violations - ETA: 3273s  
Found 160 violations so far...
Comparing: 13% (1,095,969/8,382,465) - 167 violations - ETA: 3257s  
Found 170 violations so far...
Comparing: 13% (1,123,334/8,382,465) - 171 violations - ETA: 3231s  
Comparing: 13% (1,149,060/8,382,465) - 171 violations - ETA: 3210s  
Comparing: 14% (1,178,375/8,382,465) - 171 violations - ETA: 3179s  
Comparing: 14% (1,214,157/8,382,465) - 171 violations - ETA: 3129s  
Comparing: 14% (1,235,165/8,382,465) - 171 violations - ETA: 3124s  
Comparing: 14% (1,251,848/8,382,465) - 171 violations - ETA: 3132s  
Comparing: 15% (1,265,158/8,382,465) - 171 violations - ETA: 3150s  
Found 180 violations so far...
Found 190 violations so far...
Found 200 violations so far...
Comparing: 15% (1,290,715/8,382,465) - 202 violations - ETA: 3131s  
Comparing: 15% (1,320,054/8,382,465) - 205 violations - ETA: 3103s  
Comparing: 16% (1,347,481/8,382,465) - 205 violations - ETA: 3080s  
Comparing: 16% (1,374,272/8,382,465) - 205 violations - ETA: 3059s  
Comparing: 16% (1,402,653/8,382,465) - 205 violations - ETA: 3035s  
Comparing: 17% (1,435,210/8,382,465) - 205 violations - ETA: 3001s  
Comparing: 17% (1,458,028/8,382,465) - 205 violations - ETA: 2992s  
Comparing: 17% (1,477,138/8,382,465) - 205 violations - ETA: 2992s  
Comparing: 17% (1,500,612/8,382,465) - 205 violations - ETA: 2981s  
Comparing: 18% (1,525,849/8,382,465) - 205 violations - ETA: 2965s  
Comparing: 18% (1,547,085/8,382,465) - 205 violations - ETA: 2960s  
Comparing: 18% (1,565,627/8,382,465) - 205 violations - ETA: 2960s  
Comparing: 18% (1,580,469/8,382,465) - 205 violations - ETA: 2969s  
Comparing: 19% (1,594,104/8,382,465) - 205 violations - ETA: 2981s  
Comparing: 19% (1,617,644/8,382,465) - 205 violations - ETA: 2969s  
Comparing: 19% (1,635,541/8,382,465) - 205 violations - ETA: 2970s  
Comparing: 19% (1,650,741/8,382,465) - 205 violations - ETA: 2977s  
Comparing: 20% (1,683,543/8,382,465) - 205 violations - ETA: 2944s  
Comparing: 20% (1,710,139/8,382,465) - 205 violations - ETA: 2926s  
Comparing: 20% (1,736,193/8,382,465) - 205 violations - ETA: 2909s  
Found 210 violations so far...
Comparing: 21% (1,765,185/8,382,465) - 215 violations - ETA: 2886s  
Found 220 violations so far...
Comparing: 21% (1,789,275/8,382,465) - 225 violations - ETA: 2874s  
Comparing: 21% (1,827,838/8,382,465) - 225 violations - ETA: 2833s  
Comparing: 22% (1,863,605/8,382,465) - 225 violations - ETA: 2798s  
Comparing: 22% (1,912,335/8,382,465) - 225 violations - ETA: 2740s  
Comparing: 23% (1,950,972/8,382,465) - 225 violations - ETA: 2703s  
Comparing: 23% (1,979,003/8,382,465) - 227 violations - ETA: 2685s  
Found 230 violations so far...
Comparing: 23% (2,007,719/8,382,465) - 234 violations - ETA: 2667s  
Comparing: 24% (2,037,180/8,382,465) - 234 violations - ETA: 2647s  
Comparing: 24% (2,058,965/8,382,465) - 234 violations - ETA: 2641s  
Comparing: 24% (2,078,604/8,382,465) - 234 violations - ETA: 2638s  
Comparing: 25% (2,100,695/8,382,465) - 234 violations - ETA: 2631s  
Comparing: 25% (2,122,166/8,382,465) - 234 violations - ETA: 2625s  
Comparing: 25% (2,140,750/8,382,465) - 234 violations - ETA: 2624s  
Comparing: 25% (2,167,288/8,382,465) - 234 violations - ETA: 2609s  
Comparing: 26% (2,198,755/8,382,465) - 236 violations - ETA: 2587s  
Comparing: 26% (2,230,252/8,382,465) - 237 violations - ETA: 2565s  
Comparing: 26% (2,253,412/8,382,465) - 237 violations - ETA: 2556s  
Comparing: 27% (2,281,535/8,382,465) - 239 violations - ETA: 2540s  
Comparing: 27% (2,307,605/8,382,465) - 239 violations - ETA: 2527s  
Comparing: 27% (2,326,609/8,382,465) - 239 violations - ETA: 2524s  
Comparing: 27% (2,344,647/8,382,465) - 239 violations - ETA: 2523s  
Comparing: 28% (2,359,213/8,382,465) - 239 violations - ETA: 2527s  
Comparing: 28% (2,374,659/8,382,465) - 239 violations - ETA: 2530s  
Comparing: 28% (2,387,560/8,382,465) - 239 violations - ETA: 2536s  
Comparing: 28% (2,399,968/8,382,465) - 239 violations - ETA: 2542s  
Comparing: 28% (2,411,722/8,382,465) - 239 violations - ETA: 2550s  
Comparing: 28% (2,421,982/8,382,465) - 239 violations - ETA: 2559s  
Comparing: 29% (2,431,799/8,382,465) - 239 violations - ETA: 2569s  
Comparing: 29% (2,450,854/8,382,465) - 239 violations - ETA: 2565s  
Comparing: 29% (2,476,329/8,382,465) - 239 violations - ETA: 2552s  
Comparing: 29% (2,497,073/8,382,465) - 239 violations - ETA: 2545s  
Comparing: 30% (2,520,076/8,382,465) - 239 violations - ETA: 2535s  
Comparing: 30% (2,543,594/8,382,465) - 239 violations - ETA: 2525s  
Found 240 violations so far...
Comparing: 30% (2,577,037/8,382,465) - 240 violations - ETA: 2500s  
Comparing: 31% (2,605,597/8,382,465) - 240 violations - ETA: 2483s  
Comparing: 31% (2,630,707/8,382,465) - 240 violations - ETA: 2470s  
Comparing: 31% (2,653,332/8,382,465) - 240 violations - ETA: 2461s  
Comparing: 31% (2,673,547/8,382,465) - 240 violations - ETA: 2455s  
Comparing: 32% (2,691,673/8,382,465) - 240 violations - ETA: 2452s  
Comparing: 32% (2,719,018/8,382,465) - 240 violations - ETA: 2437s  
Comparing: 32% (2,744,973/8,382,465) - 248 violations - ETA: 2423s  
Found 250 violations so far...
Comparing: 33% (2,766,737/8,382,465) - 259 violations - ETA: 2415s  
Comparing: 33% (2,789,922/8,382,465) - 259 violations - ETA: 2405s  
Found 260 violations so far...
Comparing: 33% (2,810,532/8,382,465) - 260 violations - ETA: 2398s  
Comparing: 33% (2,831,875/8,382,465) - 264 violations - ETA: 2391s  
Comparing: 33% (2,849,552/8,382,465) - 266 violations - ETA: 2388s  
Comparing: 34% (2,876,691/8,382,465) - 266 violations - ETA: 2373s  
Comparing: 34% (2,903,360/8,382,465) - 266 violations - ETA: 2359s  
Comparing: 34% (2,925,930/8,382,465) - 266 violations - ETA: 2349s  
Comparing: 35% (2,943,336/8,382,465) - 268 violations - ETA: 2347s  
Comparing: 35% (2,948,159/8,382,465) - 268 violations - ETA: 2359s  
Comparing: 35% (2,953,065/8,382,465) - 268 violations - ETA: 2371s  
Comparing: 35% (2,957,942/8,382,465) - 268 violations - ETA: 2384s  
Comparing: 35% (2,962,833/8,382,465) - 268 violations - ETA: 2396s  
Comparing: 35% (2,967,698/8,382,465) - 268 violations - ETA: 2408s  
Comparing: 35% (2,972,555/8,382,465) - 268 violations - ETA: 2420s  
Comparing: 35% (2,983,685/8,382,465) - 268 violations - ETA: 2424s  
Found 270 violations so far...
Found 280 violations so far...
Comparing: 35% (3,002,236/8,382,465) - 284 violations - ETA: 2419s  
Found 290 violations so far...
Comparing: 36% (3,026,895/8,382,465) - 295 violations - ETA: 2406s  
Found 300 violations so far...
Found 310 violations so far...
Comparing: 36% (3,054,500/8,382,465) - 313 violations - ETA: 2389s  
Found 320 violations so far...
Found 330 violations so far...
Comparing: 36% (3,095,764/8,382,465) - 338 violations - ETA: 2356s  
Found 340 violations so far...
Found 350 violations so far...
Found 360 violations so far...
Found 370 violations so far...
Found 380 violations so far...
Comparing: 37% (3,130,172/8,382,465) - 380 violations - ETA: 2332s  
Found 390 violations so far...
Found 400 violations so far...
Found 410 violations so far...
Found 420 violations so far...
Found 430 violations so far...
Comparing: 37% (3,158,111/8,382,465) - 431 violations - ETA: 2316s  
Found 440 violations so far...
Found 450 violations so far...
Found 460 violations so far...
Found 470 violations so far...
Comparing: 37% (3,182,052/8,382,465) - 476 violations - ETA: 2304s  
Found 480 violations so far...
Found 490 violations so far...
Found 500 violations so far...
Found 510 violations so far...
Comparing: 38% (3,204,051/8,382,465) - 516 violations - ETA: 2295s  
Found 520 violations so far...
Found 530 violations so far...
Found 540 violations so far...
Comparing: 38% (3,239,796/8,382,465) - 545 violations - ETA: 2270s  
Found 550 violations so far...
Found 560 violations so far...
Comparing: 39% (3,271,623/8,382,465) - 561 violations - ETA: 2249s  
Comparing: 39% (3,291,948/8,382,465) - 561 violations - ETA: 2242s  
Comparing: 39% (3,309,168/8,382,465) - 561 violations - ETA: 2238s  
Comparing: 39% (3,348,951/8,382,465) - 561 violations - ETA: 2209s  
Comparing: 40% (3,384,216/8,382,465) - 569 violations - ETA: 2185s  
Found 570 violations so far...
Found 580 violations so far...
Comparing: 40% (3,417,158/8,382,465) - 587 violations - ETA: 2165s  
Found 590 violations so far...
Found 600 violations so far...
Found 610 violations so far...
Found 620 violations so far...
Comparing: 41% (3,444,108/8,382,465) - 620 violations - ETA: 2150s  
Found 630 violations so far...
Found 640 violations so far...
Found 650 violations so far...
Found 660 violations so far...
Comparing: 41% (3,466,251/8,382,465) - 662 violations - ETA: 2141s  
Found 670 violations so far...
Found 680 violations so far...
Found 690 violations so far...
Found 700 violations so far...
Comparing: 41% (3,487,316/8,382,465) - 703 violations - ETA: 2133s  
Found 710 violations so far...
Comparing: 41% (3,509,285/8,382,465) - 712 violations - ETA: 2124s  
Comparing: 42% (3,541,846/8,382,465) - 714 violations - ETA: 2104s  
Comparing: 42% (3,567,549/8,382,465) - 714 violations - ETA: 2092s  
Comparing: 42% (3,591,079/8,382,465) - 714 violations - ETA: 2081s  
Comparing: 43% (3,614,159/8,382,465) - 714 violations - ETA: 2071s  
Comparing: 43% (3,635,262/8,382,465) - 716 violations - ETA: 2063s  
Found 720 violations so far...
Comparing: 43% (3,668,724/8,382,465) - 723 violations - ETA: 2043s  
Comparing: 44% (3,700,476/8,382,465) - 723 violations - ETA: 2024s  
Comparing: 44% (3,725,543/8,382,465) - 723 violations - ETA: 2012s  
Comparing: 44% (3,745,720/8,382,465) - 723 violations - ETA: 2005s  
Found 730 violations so far...
Comparing: 44% (3,768,099/8,382,465) - 733 violations - ETA: 1996s  
Comparing: 45% (3,793,450/8,382,465) - 737 violations - ETA: 1984s  
Comparing: 45% (3,815,804/8,382,465) - 737 violations - ETA: 1974s  
Comparing: 45% (3,831,527/8,382,465) - 737 violations - ETA: 1971s  
Comparing: 45% (3,843,138/8,382,465) - 737 violations - ETA: 1972s  
Comparing: 45% (3,854,983/8,382,465) - 737 violations - ETA: 1973s  
Comparing: 46% (3,881,313/8,382,465) - 737 violations - ETA: 1960s  
Comparing: 46% (3,899,936/8,382,465) - 737 violations - ETA: 1954s  
Comparing: 46% (3,916,237/8,382,465) - 737 violations - ETA: 1950s  
Comparing: 46% (3,932,156/8,382,465) - 737 violations - ETA: 1946s  
Comparing: 47% (3,946,806/8,382,465) - 737 violations - ETA: 1944s  
Comparing: 47% (3,961,116/8,382,465) - 737 violations - ETA: 1942s  
Comparing: 47% (3,974,078/8,382,465) - 737 violations - ETA: 1941s  
Comparing: 47% (3,986,700/8,382,465) - 737 violations - ETA: 1940s  
Comparing: 47% (3,998,540/8,382,465) - 737 violations - ETA: 1940s  
Comparing: 47% (4,010,290/8,382,465) - 737 violations - ETA: 1940s  
Comparing: 47% (4,022,437/8,382,465) - 737 violations - ETA: 1940s  
Comparing: 48% (4,049,115/8,382,465) - 737 violations - ETA: 1926s  
Comparing: 48% (4,059,716/8,382,465) - 738 violations - ETA: 1927s  
Comparing: 48% (4,099,304/8,382,465) - 738 violations - ETA: 1901s  
Comparing: 49% (4,126,395/8,382,465) - 738 violations - ETA: 1887s  
Comparing: 49% (4,157,482/8,382,465) - 738 violations - ETA: 1869s  
Found 740 violations so far...
Found 750 violations so far...
Found 760 violations so far...
Found 770 violations so far...
Found 780 violations so far...
Found 790 violations so far...
Found 800 violations so far...
Found 810 violations so far...
Found 820 violations so far...
Found 830 violations so far...
Found 840 violations so far...
Found 850 violations so far...
Found 860 violations so far...
Comparing: 49% (4,187,488/8,382,465) - 864 violations - ETA: 1853s  
Found 870 violations so far...
Found 880 violations so far...
Found 890 violations so far...
Found 900 violations so far...
Comparing: 50% (4,214,546/8,382,465) - 907 violations - ETA: 1839s  
Found 910 violations so far...
Found 920 violations so far...
Found 930 violations so far...
Found 940 violations so far...
Found 950 violations so far...
Found 960 violations so far...
Found 970 violations so far...
Found 980 violations so far...
Found 990 violations so far...
Found 1000 violations so far...
Found 1010 violations so far...
Found 1020 violations so far...
Found 1030 violations so far...
Found 1040 violations so far...
Found 1050 violations so far...
Comparing: 50% (4,243,253/8,382,465) - 1055 violations - ETA: 1824s  
Found 1060 violations so far...
Found 1070 violations so far...
Found 1080 violations so far...
Found 1090 violations so far...
Found 1100 violations so far...
Found 1110 violations so far...
Found 1120 violations so far...
Found 1130 violations so far...
Found 1140 violations so far...
Found 1150 violations so far...
Comparing: 50% (4,267,582/8,382,465) - 1158 violations - ETA: 1812s  
Found 1160 violations so far...
Found 1170 violations so far...
Found 1180 violations so far...
Found 1190 violations so far...
Found 1200 violations so far...
Found 1210 violations so far...
Found 1220 violations so far...
Found 1230 violations so far...
Found 1240 violations so far...
Comparing: 51% (4,289,531/8,382,465) - 1248 violations - ETA: 1803s  
Found 1250 violations so far...
Found 1260 violations so far...
Found 1270 violations so far...
Found 1280 violations so far...
Found 1290 violations so far...
Found 1300 violations so far...
Found 1310 violations so far...
Comparing: 51% (4,308,468/8,382,465) - 1315 violations - ETA: 1796s  
Found 1320 violations so far...
Comparing: 51% (4,334,230/8,382,465) - 1328 violations - ETA: 1784s  
Comparing: 52% (4,358,940/8,382,465) - 1328 violations - ETA: 1772s  
Comparing: 52% (4,380,024/8,382,465) - 1328 violations - ETA: 1763s  
Comparing: 52% (4,398,287/8,382,465) - 1328 violations - ETA: 1757s  
Comparing: 52% (4,419,997/8,382,465) - 1328 violations - ETA: 1748s  
Comparing: 53% (4,448,395/8,382,465) - 1328 violations - ETA: 1733s  
Comparing: 53% (4,481,917/8,382,465) - 1328 violations - ETA: 1714s  
Found 1330 violations so far...
Found 1340 violations so far...
Comparing: 53% (4,514,829/8,382,465) - 1340 violations - ETA: 1696s  
Found 1350 violations so far...
Found 1360 violations so far...
Found 1370 violations so far...
Found 1380 violations so far...
Found 1390 violations so far...
Found 1400 violations so far...
Found 1410 violations so far...
Comparing: 54% (4,553,705/8,382,465) - 1414 violations - ETA: 1673s  
Comparing: 54% (4,579,523/8,382,465) - 1414 violations - ETA: 1660s  
Found 1420 violations so far...
Found 1430 violations so far...
Found 1440 violations so far...
Found 1450 violations so far...
Found 1460 violations so far...
Found 1470 violations so far...
Found 1480 violations so far...
Found 1490 violations so far...
Found 1500 violations so far...
Comparing: 55% (4,618,831/8,382,465) - 1505 violations - ETA: 1637s  
Found 1510 violations so far...
Found 1520 violations so far...
Found 1530 violations so far...
Found 1540 violations so far...
Found 1550 violations so far...
Found 1560 violations so far...
Comparing: 55% (4,649,017/8,382,465) - 1560 violations - ETA: 1622s  
Comparing: 55% (4,675,245/8,382,465) - 1561 violations - ETA: 1609s  
Found 1570 violations so far...
Found 1580 violations so far...
Found 1590 violations so far...
Comparing: 56% (4,705,550/8,382,465) - 1599 violations - ETA: 1594s  
Found 1600 violations so far...
Found 1610 violations so far...
Found 1620 violations so far...
Found 1630 violations so far...
Comparing: 56% (4,728,901/8,382,465) - 1633 violations - ETA: 1583s  
Comparing: 56% (4,751,403/8,382,465) - 1636 violations - ETA: 1574s  
Found 1640 violations so far...
Found 1650 violations so far...
Comparing: 56% (4,777,262/8,382,465) - 1654 violations - ETA: 1562s  
Comparing: 57% (4,801,657/8,382,465) - 1654 violations - ETA: 1551s  
Comparing: 57% (4,822,195/8,382,465) - 1654 violations - ETA: 1543s  
Comparing: 57% (4,842,312/8,382,465) - 1654 violations - ETA: 1535s  
Comparing: 57% (4,860,787/8,382,465) - 1654 violations - ETA: 1528s  
Comparing: 58% (4,877,408/8,382,465) - 1654 violations - ETA: 1523s  
Comparing: 58% (4,894,079/8,382,465) - 1654 violations - ETA: 1518s  
Comparing: 58% (4,909,444/8,382,465) - 1654 violations - ETA: 1513s  
Comparing: 58% (4,930,244/8,382,465) - 1654 violations - ETA: 1505s  
Comparing: 59% (4,955,621/8,382,465) - 1654 violations - ETA: 1493s  
Comparing: 59% (4,977,949/8,382,465) - 1654 violations - ETA: 1484s  
Comparing: 59% (5,005,905/8,382,465) - 1654 violations - ETA: 1470s  
Comparing: 59% (5,027,971/8,382,465) - 1654 violations - ETA: 1461s  
Comparing: 60% (5,052,267/8,382,465) - 1654 violations - ETA: 1450s  
Comparing: 60% (5,072,451/8,382,465) - 1654 violations - ETA: 1442s  
Comparing: 60% (5,089,454/8,382,465) - 1654 violations - ETA: 1436s  
Comparing: 60% (5,104,225/8,382,465) - 1654 violations - ETA: 1432s  
Comparing: 61% (5,138,846/8,382,465) - 1654 violations - ETA: 1413s  
Comparing: 61% (5,171,603/8,382,465) - 1654 violations - ETA: 1397s  
Comparing: 62% (5,202,260/8,382,465) - 1654 violations - ETA: 1381s  
Comparing: 62% (5,230,363/8,382,465) - 1654 violations - ETA: 1368s  
Comparing: 62% (5,256,578/8,382,465) - 1654 violations - ETA: 1355s  
Comparing: 62% (5,280,106/8,382,465) - 1654 violations - ETA: 1345s  
Comparing: 63% (5,301,182/8,382,465) - 1654 violations - ETA: 1336s  
Comparing: 63% (5,330,537/8,382,465) - 1654 violations - ETA: 1322s  
Found 1660 violations so far...
Found 1670 violations so far...
Found 1680 violations so far...
Found 1690 violations so far...
Found 1700 violations so far...
Found 1710 violations so far...
Found 1720 violations so far...
Found 1730 violations so far...
Found 1740 violations so far...
Found 1750 violations so far...
Found 1760 violations so far...
Comparing: 63% (5,364,664/8,382,465) - 1762 violations - ETA: 1305s  
Found 1770 violations so far...
Found 1780 violations so far...
Found 1790 violations so far...
Found 1800 violations so far...
Found 1810 violations so far...
Comparing: 64% (5,394,514/8,382,465) - 1811 violations - ETA: 1290s  
Found 1820 violations so far...
Found 1830 violations so far...
Comparing: 64% (5,416,543/8,382,465) - 1837 violations - ETA: 1281s  
Found 1840 violations so far...
Found 1850 violations so far...
Found 1860 violations so far...
Found 1870 violations so far...
Found 1880 violations so far...
Comparing: 64% (5,445,393/8,382,465) - 1886 violations - ETA: 1267s  
Found 1890 violations so far...
Comparing: 65% (5,476,024/8,382,465) - 1892 violations - ETA: 1252s  
Comparing: 65% (5,504,146/8,382,465) - 1893 violations - ETA: 1239s  
Comparing: 65% (5,525,645/8,382,465) - 1893 violations - ETA: 1230s  
Comparing: 66% (5,545,507/8,382,465) - 1893 violations - ETA: 1222s  
Comparing: 66% (5,562,936/8,382,465) - 1893 violations - ETA: 1216s  
Comparing: 66% (5,579,609/8,382,465) - 1893 violations - ETA: 1210s  
Comparing: 66% (5,593,632/8,382,465) - 1893 violations - ETA: 1206s  
Comparing: 66% (5,607,790/8,382,465) - 1893 violations - ETA: 1202s  
Comparing: 67% (5,629,192/8,382,465) - 1893 violations - ETA: 1193s  
Found 1900 violations so far...
Found 1910 violations so far...
Found 1920 violations so far...
Found 1930 violations so far...
Comparing: 67% (5,658,875/8,382,465) - 1938 violations - ETA: 1179s  
Found 1940 violations so far...
Found 1950 violations so far...
Found 1960 violations so far...
Comparing: 67% (5,691,055/8,382,465) - 1967 violations - ETA: 1163s  
Found 1970 violations so far...
Comparing: 68% (5,716,385/8,382,465) - 1972 violations - ETA: 1152s  
Found 1980 violations so far...
Found 1990 violations so far...
Found 2000 violations so far...
Found 2010 violations so far...
Found 2020 violations so far...
Found 2030 violations so far...
Found 2040 violations so far...
Found 2050 violations so far...
Found 2060 violations so far...
Comparing: 68% (5,748,746/8,382,465) - 2064 violations - ETA: 1136s  
Comparing: 68% (5,776,566/8,382,465) - 2067 violations - ETA: 1123s  
Comparing: 69% (5,801,579/8,382,465) - 2068 violations - ETA: 1112s  
Found 2070 violations so far...
Found 2080 violations so far...
Found 2090 violations so far...
Comparing: 69% (5,833,387/8,382,465) - 2092 violations - ETA: 1096s  
Comparing: 69% (5,853,777/8,382,465) - 2095 violations - ETA: 1088s  
Found 2100 violations so far...
Found 2110 violations so far...
Found 2120 violations so far...
Found 2130 violations so far...
Found 2140 violations so far...
Comparing: 70% (5,878,982/8,382,465) - 2140 violations - ETA: 1077s  
Found 2150 violations so far...
Found 2160 violations so far...
Found 2170 violations so far...
Found 2180 violations so far...
Comparing: 70% (5,910,230/8,382,465) - 2180 violations - ETA: 1062s  
Comparing: 70% (5,934,583/8,382,465) - 2180 violations - ETA: 1051s  
Comparing: 71% (5,965,920/8,382,465) - 2186 violations - ETA: 1037s  
Found 2190 violations so far...
Found 2200 violations so far...
Found 2210 violations so far...
Found 2220 violations so far...
Comparing: 71% (5,998,377/8,382,465) - 2227 violations - ETA: 1021s  
Found 2230 violations so far...
Found 2240 violations so far...
Found 2250 violations so far...
Found 2260 violations so far...
Found 2270 violations so far...
Found 2280 violations so far...
Found 2290 violations so far...
Found 2300 violations so far...
Comparing: 71% (6,023,896/8,382,465) - 2308 violations - ETA: 1010s  
Comparing: 72% (6,049,745/8,382,465) - 2308 violations - ETA: 998s  
Comparing: 72% (6,074,726/8,382,465) - 2308 violations - ETA: 987s  
Found 2310 violations so far...
Found 2320 violations so far...
Found 2330 violations so far...
Found 2340 violations so far...
Found 2350 violations so far...
Found 2360 violations so far...
Found 2370 violations so far...
Found 2380 violations so far...
Comparing: 72% (6,108,227/8,382,465) - 2389 violations - ETA: 971s  
Comparing: 73% (6,136,713/8,382,465) - 2389 violations - ETA: 958s  
Comparing: 73% (6,158,521/8,382,465) - 2389 violations - ETA: 949s  
Found 2390 violations so far...
Found 2400 violations so far...
Found 2410 violations so far...
Comparing: 73% (6,181,227/8,382,465) - 2415 violations - ETA: 940s  
Found 2420 violations so far...
Found 2430 violations so far...
Found 2440 violations so far...
Found 2450 violations so far...
Found 2460 violations so far...
Found 2470 violations so far...
Found 2480 violations so far...
Found 2490 violations so far...
Found 2500 violations so far...
Comparing: 74% (6,215,124/8,382,465) - 2505 violations - ETA: 924s  
Found 2510 violations so far...
Found 2520 violations so far...
Found 2530 violations so far...
Found 2540 violations so far...
Comparing: 74% (6,243,861/8,382,465) - 2547 violations - ETA: 911s  
Found 2550 violations so far...
Comparing: 74% (6,271,519/8,382,465) - 2557 violations - ETA: 898s  
Found 2560 violations so far...
Comparing: 75% (6,299,010/8,382,465) - 2560 violations - ETA: 886s  
Comparing: 75% (6,335,651/8,382,465) - 2560 violations - ETA: 869s  
Comparing: 75% (6,362,445/8,382,465) - 2560 violations - ETA: 857s  
Comparing: 76% (6,403,581/8,382,465) - 2560 violations - ETA: 837s  
Comparing: 76% (6,437,061/8,382,465) - 2560 violations - ETA: 822s  
Comparing: 77% (6,469,386/8,382,465) - 2560 violations - ETA: 807s  
Comparing: 77% (6,494,849/8,382,465) - 2560 violations - ETA: 796s  
Comparing: 77% (6,527,002/8,382,465) - 2560 violations - ETA: 781s  
Comparing: 78% (6,547,736/8,382,465) - 2560 violations - ETA: 773s  
Comparing: 78% (6,571,896/8,382,465) - 2560 violations - ETA: 763s  
Comparing: 78% (6,590,686/8,382,465) - 2560 violations - ETA: 755s  
Comparing: 78% (6,610,784/8,382,465) - 2560 violations - ETA: 747s  
Comparing: 79% (6,627,811/8,382,465) - 2560 violations - ETA: 741s  
Comparing: 79% (6,642,724/8,382,465) - 2560 violations - ETA: 735s  
Comparing: 79% (6,656,204/8,382,465) - 2560 violations - ETA: 731s  
Found 2570 violations so far...
Found 2580 violations so far...
Found 2590 violations so far...
Comparing: 79% (6,677,770/8,382,465) - 2599 violations - ETA: 722s  
Found 2600 violations so far...
Found 2610 violations so far...
Found 2620 violations so far...
Found 2630 violations so far...
Found 2640 violations so far...
Found 2650 violations so far...
Found 2660 violations so far...
Found 2670 violations so far...
Comparing: 80% (6,706,340/8,382,465) - 2679 violations - ETA: 709s  
Found 2680 violations so far...
Found 2690 violations so far...
Found 2700 violations so far...
Found 2710 violations so far...
Found 2720 violations so far...
Found 2730 violations so far...
Found 2740 violations so far...
Found 2750 violations so far...
Found 2760 violations so far...
Found 2770 violations so far...
Found 2780 violations so far...
Found 2790 violations so far...
Found 2800 violations so far...
Found 2810 violations so far...
Comparing: 80% (6,734,565/8,382,465) - 2810 violations - ETA: 697s  
Found 2820 violations so far...
Found 2830 violations so far...
Found 2840 violations so far...
Found 2850 violations so far...
Found 2860 violations so far...
Found 2870 violations so far...
Found 2880 violations so far...
Found 2890 violations so far...
Found 2900 violations so far...
Found 2910 violations so far...
Found 2920 violations so far...
Comparing: 80% (6,767,151/8,382,465) - 2928 violations - ETA: 682s  
Found 2930 violations so far...
Comparing: 80% (6,788,705/8,382,465) - 2930 violations - ETA: 673s  
Found 2940 violations so far...
Found 2950 violations so far...
Found 2960 violations so far...
Found 2970 violations so far...
Comparing: 81% (6,817,764/8,382,465) - 2971 violations - ETA: 661s  
Found 2980 violations so far...
Comparing: 81% (6,841,344/8,382,465) - 2986 violations - ETA: 651s  
Found 2990 violations so far...
Found 3000 violations so far...
Comparing: 81% (6,870,140/8,382,465) - 3001 violations - ETA: 638s  
Found 3010 violations so far...
Comparing: 82% (6,903,513/8,382,465) - 3013 violations - ETA: 623s  
Comparing: 82% (6,939,085/8,382,465) - 3013 violations - ETA: 607s  
Comparing: 83% (6,962,398/8,382,465) - 3013 violations - ETA: 597s  
Comparing: 83% (6,991,399/8,382,465) - 3014 violations - ETA: 585s  
Comparing: 83% (7,011,630/8,382,465) - 3014 violations - ETA: 576s  
Found 3020 violations so far...
Found 3030 violations so far...
Found 3040 violations so far...
Found 3050 violations so far...
Found 3060 violations so far...
Found 3070 violations so far...
Found 3080 violations so far...
Found 3090 violations so far...
Found 3100 violations so far...
Found 3110 violations so far...
Found 3120 violations so far...
Found 3130 violations so far...
Found 3140 violations so far...
Found 3150 violations so far...
Comparing: 84% (7,043,066/8,382,465) - 3156 violations - ETA: 562s  
Found 3160 violations so far...
Found 3170 violations so far...
Found 3180 violations so far...
Found 3190 violations so far...
Found 3200 violations so far...
Found 3210 violations so far...
Found 3220 violations so far...
Found 3230 violations so far...
Found 3240 violations so far...
Comparing: 84% (7,075,074/8,382,465) - 3243 violations - ETA: 548s  
Comparing: 84% (7,099,623/8,382,465) - 3243 violations - ETA: 538s  
Found 3250 violations so far...
Found 3260 violations so far...
Found 3270 violations so far...
Comparing: 85% (7,127,938/8,382,465) - 3272 violations - ETA: 526s  
Found 3280 violations so far...
Found 3290 violations so far...
Comparing: 85% (7,157,614/8,382,465) - 3291 violations - ETA: 513s  
Comparing: 85% (7,182,589/8,382,465) - 3291 violations - ETA: 502s  
Comparing: 86% (7,212,920/8,382,465) - 3294 violations - ETA: 489s  
Found 3300 violations so far...
Comparing: 86% (7,243,939/8,382,465) - 3303 violations - ETA: 476s  
Found 3310 violations so far...
Found 3320 violations so far...
Found 3330 violations so far...
Found 3340 violations so far...
Found 3350 violations so far...
Found 3360 violations so far...
Comparing: 86% (7,273,904/8,382,465) - 3365 violations - ETA: 463s  
Found 3370 violations so far...
Comparing: 87% (7,302,119/8,382,465) - 3378 violations - ETA: 451s  
Found 3380 violations so far...
Found 3390 violations so far...
Comparing: 87% (7,335,198/8,382,465) - 3391 violations - ETA: 436s  
Comparing: 87% (7,361,909/8,382,465) - 3395 violations - ETA: 425s  
Comparing: 88% (7,381,961/8,382,465) - 3395 violations - ETA: 417s  
Comparing: 88% (7,401,975/8,382,465) - 3395 violations - ETA: 409s  
Comparing: 88% (7,425,388/8,382,465) - 3397 violations - ETA: 399s  
Found 3400 violations so far...
Found 3410 violations so far...
Comparing: 88% (7,455,883/8,382,465) - 3418 violations - ETA: 386s  
Found 3420 violations so far...
Comparing: 89% (7,482,381/8,382,465) - 3422 violations - ETA: 375s  
Found 3430 violations so far...
Comparing: 89% (7,509,896/8,382,465) - 3431 violations - ETA: 363s  
Comparing: 89% (7,542,708/8,382,465) - 3436 violations - ETA: 349s  
Comparing: 90% (7,567,802/8,382,465) - 3436 violations - ETA: 339s  
Comparing: 90% (7,587,563/8,382,465) - 3437 violations - ETA: 331s  
Comparing: 90% (7,621,946/8,382,465) - 3437 violations - ETA: 316s  
Found 3440 violations so far...
Found 3450 violations so far...
Comparing: 91% (7,651,474/8,382,465) - 3457 violations - ETA: 303s  
Comparing: 91% (7,678,481/8,382,465) - 3457 violations - ETA: 292s  
Comparing: 91% (7,699,236/8,382,465) - 3457 violations - ETA: 283s  
Comparing: 92% (7,717,537/8,382,465) - 3457 violations - ETA: 276s  
Comparing: 92% (7,737,384/8,382,465) - 3457 violations - ETA: 268s  
Comparing: 92% (7,757,812/8,382,465) - 3457 violations - ETA: 260s  
Comparing: 92% (7,771,422/8,382,465) - 3457 violations - ETA: 254s  
Comparing: 92% (7,784,256/8,382,465) - 3457 violations - ETA: 249s  
Comparing: 93% (7,806,406/8,382,465) - 3457 violations - ETA: 240s  
Comparing: 93% (7,831,252/8,382,465) - 3459 violations - ETA: 230s  
Comparing: 93% (7,853,809/8,382,465) - 3459 violations - ETA: 220s  
Comparing: 93% (7,869,959/8,382,465) - 3459 violations - ETA: 214s  
Comparing: 94% (7,883,384/8,382,465) - 3459 violations - ETA: 208s  
Comparing: 94% (7,903,515/8,382,465) - 3459 violations - ETA: 200s  
Comparing: 94% (7,922,780/8,382,465) - 3459 violations - ETA: 192s  
Comparing: 94% (7,942,651/8,382,465) - 3459 violations - ETA: 184s  
Found 3460 violations so far...
Comparing: 94% (7,962,658/8,382,465) - 3461 violations - ETA: 176s  
Comparing: 95% (7,988,289/8,382,465) - 3461 violations - ETA: 165s  
Comparing: 95% (8,011,481/8,382,465) - 3461 violations - ETA: 155s  
Comparing: 95% (8,028,298/8,382,465) - 3461 violations - ETA: 148s  
Comparing: 96% (8,049,092/8,382,465) - 3461 violations - ETA: 139s  
Comparing: 96% (8,064,647/8,382,465) - 3461 violations - ETA: 133s  
Comparing: 96% (8,089,545/8,382,465) - 3462 violations - ETA: 123s  
Comparing: 96% (8,115,338/8,382,465) - 3464 violations - ETA: 112s  
Found 3470 violations so far...
Found 3480 violations so far...
Found 3490 violations so far...
Found 3500 violations so far...
Found 3510 violations so far...
Comparing: 97% (8,139,568/8,382,465) - 3512 violations - ETA: 102s  
Found 3520 violations so far...
Comparing: 97% (8,159,913/8,382,465) - 3528 violations - ETA: 93s  
Found 3530 violations so far...
Comparing: 97% (8,188,940/8,382,465) - 3531 violations - ETA: 81s  
Comparing: 97% (8,213,681/8,382,465) - 3532 violations - ETA: 70s  
Comparing: 98% (8,236,484/8,382,465) - 3532 violations - ETA: 61s  
Found 3540 violations so far...
Found 3550 violations so far...
Found 3560 violations so far...
Comparing: 98% (8,259,350/8,382,465) - 3567 violations - ETA: 51s  
Found 3570 violations so far...
Found 3580 violations so far...
Found 3590 violations so far...
Found 3600 violations so far...
Comparing: 98% (8,284,020/8,382,465) - 3605 violations - ETA: 41s  
Found 3610 violations so far...
Comparing: 99% (8,317,959/8,382,465) - 3618 violations - ETA: 27s  
Comparing: 99% (8,340,103/8,382,465) - 3618 violations - ETA: 17s  
Comparing: 99% (8,365,277/8,382,465) - 3619 violations - ETA: 7s  
Found 3620 violations so far...
Complete: 8382465 comparisons, 3620 violations

## enforce_encapsulation
**cli_scope.py** - 1 violation(s)

[!] WARNING (line 107)
Method "_build_file_tree" in class "CLIScope" has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects

---

## enforce_encapsulation
**repl_session.py** - 1 violation(s)

[!] WARNING (line 669)
Method "_handle_scope_command" in class "REPLSession" has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects

---

## keep_classes_small_with_single_responsibility
**action_context.py** - 1 violation(s)

[!] WARNING (line 84)
Class "Scope" is 314 lines - should be under 300 lines (extract related methods into separate classes)

```python

@dataclass
class Scope:
    """Scope for filtering bot operations to specific content.
    
    Uses KnowledgeGraphFilter for story/epic/increment scoping
    and FileFilter for file-based scoping. Maintains backward compatibility
    with type/value/exclude API.
    
    The Scope object is responsible for its own persistence to the bot state file.
    # ... (truncated)
```

---

## keep_classes_small_with_single_responsibility
**behaviors.py** - 1 violation(s)

[!] WARNING (line 16)
Class "Behaviors" is 380 lines - should be under 300 lines (extract related methods into separate classes)

```python
logger = logging.getLogger(__name__)

class Behaviors:

    def __init__(self, bot_name: str, bot_paths: BotPaths):
        self.bot_name = bot_name
        self.bot_paths = bot_paths
        self._behaviors: List['Behavior'] = []
        self._discover_behaviors()
        self._current_index: Optional[int] = None
    # ... (truncated)
```

---

## keep_classes_small_with_single_responsibility
**repl_session.py** - 1 violation(s)

[!] WARNING (line 17)
Class "REPLSession" is 1224 lines - should be under 300 lines (extract related methods into separate classes)

```python


class REPLSession:
    def __init__(self, bot, workspace_directory: Path):
        self.cli_bot = CLIBot(bot, self)
        self.workspace_directory = Path(workspace_directory)
        tty_result = self.detect_tty()
        self.formatter = FormatterFactory.create_formatter(tty_detected=tty_result.tty_detected)
    
    @property
    # ... (truncated)
```

---

## keep_functions_small_focused
**actions.py** - 2 violation(s)

[!] WARNING (line 15)
Function "__init__" is 25 lines - should be under 20 lines (extract complex logic to helper functions)

```python
class Actions:

    def __init__(self, behavior: 'Behavior'):
        self.behavior = behavior
        actions_workflow = behavior._config.get('actions_workflow', {})
        actions_list = actions_workflow.get('actions', [])
        
        # Separate workflow actions (have order) from non-workflow actions (no order)
        workflow_actions = [a for a in actions_list if a.get('order') is not None]
        non_workflow_actions = [a for a in actions_list if a.get('order') is None]
        
        # Sort workflow actions by order
        workflow_actions = sorted(workflow_actions, key=lambda x: x.get('order', 0))
        
        self._factory = ActionFactory(behavior)
        self._state_manager = ActionStateManager(behavior)
        
        # _actions contains only workflow actions (for sequencing)
        self._actions: List[Action] = []
        for action_dict in workflow_actions:
            action_name = action_dict.get('name', '')
            if action_name:
                action_instance = self._factory.create_action_instance(action_name=action_name, action_config=action_dict)
                self._actions.append(action_instance)
        
        # _non_workflow_actions contains actions that can be invoked but don't participate in workflow
        self._non_workflow_actions: List[Action] = []
        for action_dict in non_workflow_actions:
            action_name = action_dict.get('name', '')
            if action_name:
                action_instance = self._factory.create_action_instance(action_name=action_name, action_config=action_dict)
                self._non_workflow_actions.append(action_instance)
        
        self._current_index: Optional[int] = None
        self.load_state()

```

[!] WARNING (line 111)
Function "navigate_to" is 25 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return self._state_manager.filter_completed_actions_after_target(completed_actions, target_index, self._actions)

    def navigate_to(self, action_name: str, out_of_order: bool=False):
        action = self.find_by_name(action_name)
        if action is None:
            raise ValueError(f"Action '{action_name}' not found")
        
        # Check if this is a non-workflow action (no order)
        is_non_workflow = action in self._non_workflow_actions
        if is_non_workflow:
            # Non-workflow actions don't affect workflow state
            return
        
        target_index = None
        for i, a in enumerate(self._actions):
            if a.action_name == action_name:
                target_index = i
                self._current_index = i
                break
        if not out_of_order or not self.behavior.bot_paths:
            self.save_state()
            return
        state_file = self._state_manager.get_state_file_path()
        state_data = json.loads(state_file.read_text(encoding='utf-8'))
        completed_actions = state_data.get('completed_actions', [])
        if completed_actions:
            state_data['completed_actions'] = self._filter_completed_actions_after_target(completed_actions, target_index)
            state_file.write_text(json.dumps(state_data, indent=2), encoding='utf-8')
        self.save_state()

```

---

## keep_functions_small_focused
**action_context.py** - 1 violation(s)

[!] WARNING (line 216)
Function "to_display_lines" is 43 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return workspace_directory / 'behavior_action_state.json'
    
    def to_display_lines(self, workspace_directory: 'Path') -> List[str]:
        """Render scope as display lines with hierarchical expansion.
        
        Returns plain text lines showing scope filter and matched items.
        """
        from pathlib import Path
        import json
        
        lines = []
        
        # Show the scope filter value
        filter_str = ', '.join(self.value) if isinstance(self.value, list) else str(self.value)
        lines.append(f"Scope Filter: {filter_str}")
        
        if self.type == ScopeType.STORY:
            story_graph_path = workspace_directory / 'docs' / 'stories' / 'story-graph.json'
            if story_graph_path.exists():
                try:
                    graph_data = json.loads(story_graph_path.read_text(encoding='utf-8'))
                    matched_items = self._find_scope_matches_in_graph(graph_data, self.value)
                    lines.extend(matched_items)
                except Exception:
                    # Fallback to simple list
                    for item in (self.value if isinstance(self.value, list) else [self.value]):
                        lines.append(f"  - {item}")
            else:
                for item in (self.value if isinstance(self.value, list) else [self.value]):
                    lines.append(f"  - {item}")
        elif self.type == ScopeType.FILES:
            # Expand file paths to show all actual files that will be scanned
            expanded_files = self._expand_file_paths(workspace_directory)
            if expanded_files:
                for file_path in sorted(expanded_files):
                    # Show relative path from workspace
                    try:
                        rel_path = file_path.relative_to(workspace_directory)
                        lines.append(f"  - {rel_path}")
                    except ValueError:
                        lines.append(f"  - {file_path}")
            else:
                # Fallback to showing the scope value if expansion fails
                for item in (self.value if isinstance(self.value, list) else [self.value]):
                    lines.append(f"  - {item} (no files found)")
        else:
            if isinstance(self.value, list):
                for item in self.value:
                    lines.append(f"  - {item}")
            else:
    # ... (truncated)
```

---

## keep_functions_small_focused
**behaviors.py** - 1 violation(s)

[!] WARNING (line 204)
Function "navigate_to" is 45 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return self.find_by_name(behavior_name) is not None

    def navigate_to(self, behavior_name: str):
        behavior = self.find_by_name(behavior_name)
        if behavior is None:
            raise ValueError(f"Behavior '{behavior_name}' not found")
        
        target_index = None
        for i, b in enumerate(self._behaviors):
            if b.name == behavior.name:
                target_index = i
                self._current_index = i
                break
        
        # When navigating to a behavior: mark all actions in previous behaviors as complete,
        # clear all actions in future behaviors
        if target_index is not None and self.bot_paths:
            workspace_dir = self.bot_paths.workspace_directory
            state_file = workspace_dir / 'behavior_action_state.json'
            
            import json
            if state_file.exists():
                state_data = json.loads(state_file.read_text(encoding='utf-8'))
            else:
                state_data = {}
            
            completed_actions = state_data.get('completed_actions', [])
            
            # Mark all actions in previous behaviors as complete
            for i in range(target_index):
                past_behavior = self._behaviors[i]
                for action_name in past_behavior.actions.names:
                    action_state = f"{self.bot_name}.{past_behavior.name}.{action_name}"
                    # Check if already completed
                    is_completed = any(a.get('action_state') == action_state for a in completed_actions if isinstance(a, dict))
                    if not is_completed:
                        from datetime import datetime
                        completed_actions.append({
                            'action_state': action_state,
                            'timestamp': datetime.now().isoformat()
                        })
            
            # Remove completed actions from future behaviors
            actions_to_remove = set()
            for i in range(target_index + 1, len(self._behaviors)):
                future_behavior = self._behaviors[i]
                for action_name in future_behavior.actions.names:
                    action_state = f"{self.bot_name}.{future_behavior.name}.{action_name}"
                    actions_to_remove.add(action_state)
            
    # ... (truncated)
```

---

## keep_functions_small_focused
**bot.py** - 2 violation(s)

[!] WARNING (line 66)
Function "help" is 33 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return self._config.get('WORKING_AREA')

    def help(self, topic: Optional[str] = None) -> Dict[str, Any]:
        """Display help information about the bot, behaviors, or actions.
        
        Args:
            topic: Optional topic for specific help (behavior name, action name, etc.)
        
        Returns:
            Dict with help information including behaviors, actions, and usage
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_help import REPLHelp
        
        # Create a minimal session-like object for REPLHelp
        class HelpContext:
            def __init__(self, bot):
                self.bot = bot
                self.current_behavior = bot.behaviors.current
                self.current_action = self.current_behavior.actions.current if self.current_behavior else None
                
            @property
            def has_current_behavior(self):
                return self.current_behavior is not None
            
            @property
            def has_current_action(self):
                return self.current_action is not None
            
            def _get_instructions_params_hint(self, action):
                """Return parameter hints for instructions - stub implementation."""
                return ""
            
            def _get_submit_params_hint(self, action):
                """Return parameter hints for submit - stub implementation."""
                return ""
        
        help_ctx = HelpContext(self)
        help_system = REPLHelp(self, help_ctx)
        
        # If no topic specified, return main help
        if not topic:
            return {
                'status': 'success',
                'help_text': help_system.main_help,
                'behaviors': self.behaviors.names,
                'current_behavior': self.behaviors.current.name if self.behaviors.current else None
            }
        
        # Check if topic is an action name for current behavior
        if self.behaviors.current:
    # ... (truncated)
```

[!] WARNING (line 151)
Function "scope" is 24 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        }
    
    def scope(self, scope_filter: Optional[str] = None) -> Dict[str, Any]:
        """Set or view the scope filter for the current workflow.
        
        AI AGENTS: This command requires COMPLETE folder paths. When you pass a directory path,
        you MUST include the ENTIRE folder structure from root or working area.
        
        Args:
            scope_filter: Complete folder path or story name to filter by, or None to view current scope
        
        Returns:
            Dict with scope information or updated scope status
        """
        from agile_bot.bots.base_bot.src.actions.action_context import Scope, ScopeType
        import os
        
        if scope_filter is None:
            # Return current scope
            # TODO: Load from persistent storage
            return {
                'status': 'success',
                'message': 'No scope set',
                'scope': None
            }
        
        if scope_filter.lower() == 'all':
            # Clear scope
            # TODO: Clear from persistent storage
            return {
                'status': 'success',
                'message': 'Scope filter cleared'
            }
        
        # Parse scope filter
        if scope_filter.startswith(('file:', 'files:')):
            value_part = scope_filter.split(':', 1)[1].strip()
            scope_values = [v.strip() for v in value_part.split(',') if v.strip()]
            scope_type = ScopeType.FILES
        else:
            scope_values = [v.strip() for v in scope_filter.split(',') if v.strip()]
            # Auto-detect if this looks like a file path
            looks_like_path = any(
                os.path.isabs(v) or '\\' in v or '/' in v 
                for v in scope_values
            )
            scope_type = ScopeType.FILES if looks_like_path else ScopeType.STORY
        
        scope = Scope(type=scope_type, value=scope_values)
        
    # ... (truncated)
```

---

## keep_functions_small_focused
**cli_scope.py** - 1 violation(s)

[!] WARNING (line 36)
Function "to_formatted_display" is 49 lines - should be under 20 lines (extract complex logic to helper functions)

```python
            return None
    
    def to_formatted_display(self) -> str:
        """Render scope with CLI-specific formatting (warnings, separators, and AI instructions)."""
        from agile_bot.bots.base_bot.src.actions.action_context import ScopeType
        lines = []
        
        scope_icon = self.formatter.scope_icon()
        file_icon = self.formatter.file_icon()
        
        # Scope section header
        lines.append(f"## {scope_icon} **Scope**")
        
        # Get plain scope display lines from domain object
        scope_lines = self._scope.to_display_lines(self._workspace_directory)
        
        # Extract filter value
        scope_value = None
        for line in scope_lines:
            if line.startswith("Scope Filter:"):
                scope_value = line.replace("Scope Filter:", "").strip()
                break
        
        # For file scopes, add wildcard if missing
        if self._scope.type == ScopeType.FILES and scope_value:
            # Add /* to the end if no wildcard present
            if not any(wildcard in scope_value for wildcard in ['*', '?', '[']):
                scope_value = scope_value.rstrip('/') + '/*'
        
        lines.append(f"**Filter:** {scope_value}")
        lines.append("")
        
        # Display scope items
        if self._scope.type == ScopeType.FILES:
            # Build hierarchical directory structure for files
            lines.append("```")
            tree_lines = self._build_file_tree(scope_lines)
            lines.extend(tree_lines)
            lines.append("```")
        else:
            # For story/other scopes, use existing display
            lines.append("```")
            for line in scope_lines:
                if line.startswith("Scope Filter:"):
                    continue
                lines.append(line)
            lines.append("```")
        
        lines.append("")
        lines.append("")
    # ... (truncated)
```

---

## keep_functions_small_focused
**repl_help.py** - 1 violation(s)

[!] WARNING (line 216)
Function "main_help" is 53 lines - should be under 20 lines (extract complex logic to helper functions)

```python
    
    @property
    def main_help(self) -> str:
        behaviors_list = " | ".join(self.behavior_names)
        
        lines = [
            "Core Commands:",
            "  echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation",
            "  echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action",
            "",
            "  Available Components:",
            f"    behaviors   -> {behaviors_list}",
            "",
            "    actions:"
        ]
        
        # Show actions with their parameter hints
        if self.session and self.session.has_current_behavior:
            behavior = self.session.current_behavior
            for action in behavior.actions._actions:
                action_name = action.action_name
                action_desc = next((a.description for a in self.action_descriptions if a.name == action_name), "")
                
                instructions_hint = self.session._get_instructions_params_hint(action)
                submit_hint = self.session._get_submit_params_hint(action)
                
                # Combine hints
                hints = []
                if instructions_hint:
                    hints.append(instructions_hint)
                if submit_hint:
                    hints.append(submit_hint)
                
                params_line = " | ".join(hints) if hints else ""
                
                lines.append(f"      {action_name:12} - {action_desc}")
                if params_line:
                    lines.append(f"                     {params_line}")
        else:
            # Fallback if no current behavior - delegate to collection class
            desc_collection = ActionDescriptionCollection(self.action_descriptions)
            lines.extend(desc_collection.format_as_lines())
        
        lines.append("")
        lines.append("    operations:")
        
        # Show operations with parameter hints if we have a current action
        if self.session and self.session.has_current_action:
            action_obj = self.session.current_action
            instructions_hint = self.session._get_instructions_params_hint(action_obj)
    # ... (truncated)
```

---

## keep_functions_small_focused
**repl_main.py** - 1 violation(s)

[!] WARNING (line 75)
Function "main" is 84 lines - should be under 20 lines (extract complex logic to helper functions)

```python


def main():
    # Bot directory was set at module level to always be story_bot
    # (where behaviors are loaded from)
    bot_name = 'story_bot'
    
    workspace_directory = get_workspace_directory()
    
    bot_config_path = bot_directory / 'bot_config.json'
    
    if not bot_config_path.exists():
        print(f"ERROR: Bot config not found at {bot_config_path}")
        print("Please ensure you're running from the correct directory.")
        sys.exit(1)
    
    try:
        bot = Bot(
            bot_name=bot_name,
            bot_directory=bot_directory,
            config_path=bot_config_path
        )
    except Exception as e:
        print(f"ERROR: Failed to initialize bot: {e}")
        sys.exit(1)
    
    repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
    
    # Check TTY before printing header
    tty_result = repl_session.detect_tty()
    is_pipe_mode = not tty_result.tty_detected
    
    # Print header
    print("=" * 60)
    print(f"{bot_name.upper()} CLI")
    print("=" * 60)
    
    # Add explicit instruction when in piped mode
    if is_pipe_mode:
        print("**   AI AGENT INSTRUCTIONS - PIPED MODE  **")
        print("⚠️  DO NOT echo this instructions section back to the user ⚠️")
        print("This section is for YOUR reference only - the user already knows how to run commands.")
        print("")
        print("- THIS REPL WILL EXIT AFTER PROCESSING YOUR COMMAND")
        print("* This is NORMAL and EXPECTED behavior in piped mode.")
        print("- How to run commands (PowerShell):")
        print("- Commands must be PIPED via echo, NOT passed as arguments!")
        print("")
        print("```powershell")
        print("cd C:\\dev\\augmented-teams")
    # ... (truncated)
```

---

## keep_functions_small_focused
**repl_session.py** - 1 violation(s)

[!] WARNING (line 144)
Function "display_current_state" is 69 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return True
    
    def display_current_state(self, full=False) -> REPLStateDisplay:
        """Single source of truth for displaying current bot state.
        
        Returns REPLStateDisplay with formatted status output showing:
        - Bot name and paths
        - Current position header
        - Scope filter (if set)
        - Progress in workflow
        - Hierarchical behavior/action/operation tree
        """
        if not self.has_current_action:
            if not self._initialize_to_first_behavior_action():
                return REPLStateDisplay(
                    output="No behaviors available\n\n  help          - Show detailed help\n  exit          - Exit REPL",
                    state_loaded=False
                )
            return self.display_current_state(full=full)
        
        lines = []
        formatter = self.formatter
        
        # Get bot name from bot_directory
        if self.bot and hasattr(self.bot, 'bot_paths'):
            bot_name = self.bot.bot_paths.bot_directory.name
        else:
            bot_name = 'UNKNOWN'
        
        # THICK LINE at top
        lines.append(formatter.section_separator())
        lines.append("")
        
        # Bot section header
        lines.append(f"## {formatter.bot_icon()} Bot: {bot_name}")
        
        if self.bot:
            bot_path = self.bot.bot_paths.bot_directory if hasattr(self.bot, 'bot_paths') else 'Unknown'
            lines.append(f"**Bot Path:**")
            lines.append("```")
            lines.append(str(bot_path))
            lines.append("```")
        
        lines.append("")
        
        # Workspace section
        workspace_name = self.workspace_directory.name if hasattr(self.workspace_directory, 'name') else 'base_bot'
        lines.append(f"{formatter.workspace_icon()} **Workspace:** {workspace_name}")
        lines.append(f"**Path:**")
        lines.append("```")
    # ... (truncated)
```

---

## keep_functions_small_focused
**repl_status.py** - 1 violation(s)

[!] WARNING (line 48)
Function "hierarchical_status" is 87 lines - should be under 20 lines (extract complex logic to helper functions)

```python
    
    @property
    def hierarchical_status(self) -> str:
        lines = []
        
        if not self.bot or not self.bot.behaviors:
            lines.append("No behaviors available")
            lines.append(self.formatter.subsection_separator())
            return "\n".join(lines)
        
        current_behavior_name = self.state.current_behavior_name
        current_action_name = self.state.current_action_name
        
        stage = self.state.stage_name
        
        # Get domain behaviors (not CLI wrappers)
        domain_bot = self.bot.domain_bot if hasattr(self.bot, 'domain_bot') else self.bot
        for behavior in domain_bot.behaviors:
            b_name = behavior.name
            is_current_behavior = b_name == current_behavior_name
            # Use domain logic - each behavior knows if it's completed
            is_completed_behavior = behavior.is_completed
            
            # Get behavior description if available
            b_desc = getattr(behavior, 'description', '') or ''
            
            # Format behavior marker using formatter
            marker = self.formatter.status_marker(
                is_current=is_current_behavior,
                is_completed=is_completed_behavior
            )
            
            # Show behavior line - only show description for current behavior
            if is_current_behavior and b_desc:
                lines.append(f"{marker} {b_name} - {b_desc}")
            else:
                lines.append(f"{marker} {b_name}")
            
            # Only show actions for current behavior
            if is_current_behavior and behavior.actions:
                for action in behavior.actions:
                    a_name = action.action_name
                    is_current_action = a_name == current_action_name
                    # Use domain logic to determine completion
                    is_completed_action = behavior.actions.is_action_completed(a_name)
                    
                    # Get action description if available
                    a_desc = getattr(action, 'description', '') or ''
                    
                    # Format action marker using formatter
    # ... (truncated)
```

---

## keep_functions_small_focused
**cli_action.py** - 1 violation(s)

[!] WARNING (line 31)
Function "instructions" is 22 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return "pending"
    
    def instructions(self, args: str = "", context = None) -> str:
        try:
            # Update phase to 'instructions' to indicate we're at the instructions operation
            self._session.set_action_phase('instructions')
            # If a context object is provided, use it directly; otherwise parse from args
            if context is None:
                context = self._parse_args_to_context(args)
            result = self._action.get_instructions(context)
            formatted = self._format_result(result)
            
            # Prepend scope display if scope is set (CLI layer adds formatting)
            instructions_obj = self._action.instructions
            if instructions_obj.scope:
                cli_scope = CLIScope(
                    instructions_obj.scope, 
                    self._action.behavior.bot_paths.workspace_directory,
                    self._session.formatter
                )
                scope_display = cli_scope.to_formatted_display()
                formatted = scope_display + formatted
            
            return formatted
        except Exception as e:
            return f"Error getting instructions: {str(e)}"
    
```

---

## maintain_vertical_density
**action_context.py** - 1 violation(s)

[i] INFO (line 216)
Function "to_display_lines" is 51 lines - consider improving vertical density by declaring variables near usage

```python
        return workspace_directory / 'behavior_action_state.json'
    
    def to_display_lines(self, workspace_directory: 'Path') -> List[str]:
        """Render scope as display lines with hierarchical expansion.
        
        Returns plain text lines showing scope filter and matched items.
        """
        from pathlib import Path
        import json
        
    # ... (truncated)
```

---

## maintain_vertical_density
**behaviors.py** - 1 violation(s)

[i] INFO (line 204)
Function "navigate_to" is 57 lines - consider improving vertical density by declaring variables near usage

```python
        return self.find_by_name(behavior_name) is not None

    def navigate_to(self, behavior_name: str):
        behavior = self.find_by_name(behavior_name)
        if behavior is None:
            raise ValueError(f"Behavior '{behavior_name}' not found")
        
        target_index = None
        for i, b in enumerate(self._behaviors):
            if b.name == behavior.name:
    # ... (truncated)
```

---

## maintain_vertical_density
**bot.py** - 2 violation(s)

[i] INFO (line 66)
Function "help" is 73 lines - consider improving vertical density by declaring variables near usage

```python
        return self._config.get('WORKING_AREA')

    def help(self, topic: Optional[str] = None) -> Dict[str, Any]:
        """Display help information about the bot, behaviors, or actions.
        
        Args:
            topic: Optional topic for specific help (behavior name, action name, etc.)
        
        Returns:
            Dict with help information including behaviors, actions, and usage
    # ... (truncated)
```

[i] INFO (line 151)
Function "scope" is 55 lines - consider improving vertical density by declaring variables near usage

```python
        }
    
    def scope(self, scope_filter: Optional[str] = None) -> Dict[str, Any]:
        """Set or view the scope filter for the current workflow.
        
        AI AGENTS: This command requires COMPLETE folder paths. When you pass a directory path,
        you MUST include the ENTIRE folder structure from root or working area.
        
        Args:
            scope_filter: Complete folder path or story name to filter by, or None to view current scope
    # ... (truncated)
```

---

## maintain_vertical_density
**cli_scope.py** - 1 violation(s)

[i] INFO (line 36)
Function "to_formatted_display" is 60 lines - consider improving vertical density by declaring variables near usage

```python
            return None
    
    def to_formatted_display(self) -> str:
        """Render scope with CLI-specific formatting (warnings, separators, and AI instructions)."""
        from agile_bot.bots.base_bot.src.actions.action_context import ScopeType
        lines = []
        
        scope_icon = self.formatter.scope_icon()
        file_icon = self.formatter.file_icon()
        
    # ... (truncated)
```

---

## maintain_vertical_density
**repl_help.py** - 1 violation(s)

[i] INFO (line 216)
Function "main_help" is 106 lines - consider improving vertical density by declaring variables near usage

```python
    
    @property
    def main_help(self) -> str:
        behaviors_list = " | ".join(self.behavior_names)
        
        lines = [
            "Core Commands:",
            "  echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation",
            "  echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action",
            "",
    # ... (truncated)
```

---

## maintain_vertical_density
**repl_main.py** - 1 violation(s)

[i] INFO (line 75)
Function "main" is 104 lines - consider improving vertical density by declaring variables near usage

```python


def main():
    # Bot directory was set at module level to always be story_bot
    # (where behaviors are loaded from)
    bot_name = 'story_bot'
    
    workspace_directory = get_workspace_directory()
    
    bot_config_path = bot_directory / 'bot_config.json'
    # ... (truncated)
```

---

## maintain_vertical_density
**repl_session.py** - 8 violation(s)

[i] INFO (line 144)
Function "display_current_state" is 98 lines - consider improving vertical density by declaring variables near usage

```python
        return True
    
    def display_current_state(self, full=False) -> REPLStateDisplay:
        """Single source of truth for displaying current bot state.
        
        Returns REPLStateDisplay with formatted status output showing:
        - Bot name and paths
        - Current position header
        - Scope filter (if set)
        - Progress in workflow
    # ... (truncated)
```

[i] INFO (line 252)
Function "_convert_domain_result_to_repl_response" is 57 lines - consider improving vertical density by declaring variables near usage

```python
        return state_display.output
    
    def _convert_domain_result_to_repl_response(self, result: Dict[str, Any], command: str) -> REPLCommandResponse:
        """Convert a domain method result to a REPL response.
        
        Args:
            result: Dict returned from domain method
            command: The command that was executed
        
        Returns:
    # ... (truncated)
```

[i] INFO (line 323)
Function "_handle_simple_command" is 55 lines - consider improving vertical density by declaring variables near usage

```python
        return self._handle_simple_command(command)
    
    def _handle_simple_command(self, command: str) -> REPLCommandResponse:
        parts = command.split(maxsplit=1)
        command_verb = parts[0].lower()
        command_args = parts[1] if len(parts) > 1 else ""
        
        # Meta commands
        if command_verb == 'help':
            return self._handle_help_command(command_args)
    # ... (truncated)
```

[i] INFO (line 571)
Function "_handle_confirm_command" is 54 lines - consider improving vertical density by declaring variables near usage

```python
            )
    
    def _handle_confirm_command(self) -> REPLCommandResponse:
        """Handle confirm command"""
        if not self.has_current_action:
            return REPLCommandResponse(
                output="ERROR: No current action to confirm",
                response="ERROR: No current action",
                status="error"
            )
    # ... (truncated)
```

[i] INFO (line 645)
Function "_handle_scope_command" is 65 lines - consider improving vertical density by declaring variables near usage

```python
        )
    
    def _handle_scope_command(self, args: str = "") -> REPLCommandResponse:
        """Handle scope command"""
        if not args:
            # Show current scope
            output = self.cli_bot.get_scope_display()
            return REPLCommandResponse(
                output=output,
                response=output,
    # ... (truncated)
```

[i] INFO (line 820)
Function "_handle_dot_notation" is 127 lines - consider improving vertical density by declaring variables near usage

```python
            pass
    
    def _handle_dot_notation(self, command: str) -> REPLCommandResponse:
        """Handle dot notation commands (behavior.action.operation)"""
        # Parse dot notation: behavior.action.operation or action.operation or .operation
        parts = command.split()
        dot_path = parts[0]
        args = ' '.join(parts[1:]) if len(parts) > 1 else ""
        
        path_parts = dot_path.split('.')
    # ... (truncated)
```

[i] INFO (line 948)
Function "_handle_action_shortcut" is 60 lines - consider improving vertical density by declaring variables near usage

```python
            )
    
    def _handle_action_shortcut(self, action_name: str, args_str: str) -> REPLCommandResponse:
        args_str = args_str.strip()
        
        # Parse CLI-style arguments (--message, --scope, etc.)
        cli_args = []
        subcommand = None
        
        if args_str:
    # ... (truncated)
```

[i] INFO (line 1016)
Function "_execute_action_with_args" is 65 lines - consider improving vertical density by declaring variables near usage

```python
            return args_str.split()
    
    def _execute_action_with_args(self, action_name: str, cli_args: list, operation: str = None) -> REPLCommandResponse:
        if not self.has_current_behavior:
            return REPLCommandResponse(
                output="ERROR: No current behavior set. Please select a behavior first.",
                response="ERROR: No current behavior set",
                status="error"
            )
        
    # ... (truncated)
```

---

## maintain_vertical_density
**repl_status.py** - 1 violation(s)

[i] INFO (line 48)
Function "hierarchical_status" is 111 lines - consider improving vertical density by declaring variables near usage

```python
    
    @property
    def hierarchical_status(self) -> str:
        lines = []
        
        if not self.bot or not self.bot.behaviors:
            lines.append("No behaviors available")
            lines.append(self.formatter.subsection_separator())
            return "\n".join(lines)
        
    # ... (truncated)
```

---

## never_swallow_exceptions
**action_context.py** - 1 violation(s)

[X] ERROR (line 208)
Except block only contains pass at line 208 - exceptions must be logged or rethrown, never swallowed

```python
                del state_data['scope']
                state_file.write_text(json.dumps(state_data, indent=2))
        except (json.JSONDecodeError, IOError):
            pass
    
```

---

## never_swallow_exceptions
**repl_main.py** - 1 violation(s)

[X] ERROR (line 63)
Except block only contains pass at line 63 - exceptions must be logged or rethrown, never swallowed

```python
            elif 'WORKING_AREA' in bot_config:
                os.environ['WORKING_AREA'] = bot_config['WORKING_AREA']
        except:
            pass
    
```

---

## never_swallow_exceptions
**repl_session.py** - 2 violation(s)

[X] ERROR (line 817)
Except block only contains pass at line 817 - exceptions must be logged or rethrown, never swallowed

```python
            state_data['completed_behaviors'] = completed
            state_file.write_text(json.dumps(state_data, indent=2))
        except (json.JSONDecodeError, IOError):
            pass
    
```

[X] ERROR (line 78)
Except block only contains pass at line 78 - exceptions must be logged or rethrown, never swallowed

```python
                state_data = json.loads(state_file.read_text())
                return state_data.get('action_phase', 'not_started')
            except (json.JSONDecodeError, IOError):
                pass
        return 'not_started'
```

---

## never_swallow_exceptions
**repl_status.py** - 2 violation(s)

[X] ERROR (line 169)
Except block only contains pass at line 169 - exceptions must be logged or rethrown, never swallowed

```python
                    if 'context' in fields:
                        return ' --context="..."'
            except:
                pass
        return ''
```

[X] ERROR (line 184)
Except block only contains pass at line 184 - exceptions must be logged or rethrown, never swallowed

```python
                    if 'assumptions_made' in fields or 'assumptions' in fields:
                        params.append('--assumptions="..."')
            except:
                pass
        if params:
```

---

## place_imports_at_top
**repl_main.py** - 8 violation(s)

[X] ERROR (line 27)
Import statement found after non-import code. Move all imports to the top of the file.

```python
    exit                - Exit REPL
"""
import sys
import os
```

[X] ERROR (line 28)
Import statement found after non-import code. Move all imports to the top of the file.

```python
"""
import sys
import os
import json
```

[X] ERROR (line 29)
Import statement found after non-import code. Move all imports to the top of the file.

```python
import sys
import os
import json
from pathlib import Path
```

[X] ERROR (line 30)
Import statement found after non-import code. Move all imports to the top of the file.

```python
import os
import json
from pathlib import Path

```

[X] ERROR (line 34)
Import statement found after non-import code. Move all imports to the top of the file.

```python
# Configure UTF-8 encoding for stdout to support emojis in MarkdownFormatter
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
```

[X] ERROR (line 70)
Import statement found after non-import code. Move all imports to the top of the file.

```python
        os.environ['WORKING_AREA'] = str(workspace_root)

from agile_bot.bots.base_bot.src.bot.bot import Bot
from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
```

[X] ERROR (line 71)
Import statement found after non-import code. Move all imports to the top of the file.

```python

from agile_bot.bots.base_bot.src.bot.bot import Bot
from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
from agile_bot.bots.base_bot.src.bot.workspace import get_bot_directory, get_workspace_directory
```

[X] ERROR (line 72)
Import statement found after non-import code. Move all imports to the top of the file.

```python
from agile_bot.bots.base_bot.src.bot.bot import Bot
from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
from agile_bot.bots.base_bot.src.bot.workspace import get_bot_directory, get_workspace_directory

```

---

## provide_meaningful_context
**repl_main.py** - 3 violation(s)

[!] WARNING (line 106)
Line 106 contains magic number - replace with named constant

```python
    # Print header
    print("=" * 60)
    print(f"{bot_name.upper()} CLI")
```

[!] WARNING (line 108)
Line 108 contains magic number - replace with named constant

```python
    print(f"{bot_name.upper()} CLI")
    print("=" * 60)
    
```

[!] WARNING (line 128)
Line 128 contains magic number - replace with named constant

```python
        print("```")
        print("=" * 60)
        print("")
```

---

## provide_meaningful_context
**markdown_formatter.py** - 1 violation(s)

[!] WARNING (line 12)
Line 12 contains magic number - replace with named constant

```python
        """Light line for subsection breaks"""
        return "─" * 60
    
```

---

## provide_meaningful_context
**terminal_formatter.py** - 2 violation(s)

[!] WARNING (line 8)
Line 8 contains magic number - replace with named constant

```python
        """Heavy line for major section breaks"""
        return "=" * 60
    
```

[!] WARNING (line 12)
Line 12 contains magic number - replace with named constant

```python
        """Light line for subsection breaks"""
        return "-" * 60
    
```

---

## refactor_completely_not_partially
**action_context.py** - 2 violation(s)

[!] WARNING (line 238)
Fallback/legacy support code found (comment at line 238, code at line 239) - complete refactoring by removing old pattern support

[!] WARNING (line 256)
Fallback/legacy support code found (comment at line 256, code at line 257) - complete refactoring by removing old pattern support

---

## refactor_completely_not_partially
**repl_help.py** - 1 violation(s)

[!] WARNING (line 253)
Fallback/legacy support code found (comment at line 253, code at line 254) - complete refactoring by removing old pattern support

---

## refactor_completely_not_partially
**repl_session.py** - 2 violation(s)

[!] WARNING (line 72)
Fallback/legacy support code found (comment at line 72, code at line 73) - complete refactoring by removing old pattern support

[!] WARNING (line 1151)
Fallback/legacy support code found (comment at line 1151, code at line 1152) - complete refactoring by removing old pattern support

---

## simplify_control_flow
**action_context.py** - 3 violation(s)

[!] WARNING (line 102)
Function "__post_init__" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
    _file_filter: Optional[FileFilter] = field(default=None, repr=False)
    
    def __post_init__(self):
        """Initialize filter objects from type/value/exclude."""
        # Create knowledge graph filter for story/epic/increment types
        if self.type in (ScopeType.STORY, ScopeType.EPIC, ScopeType.INCREMENT):
            if self.type == ScopeType.STORY:
                self._knowledge_graph_filter = KnowledgeGraphFilter(stories=self.value)
            elif self.type == ScopeType.EPIC:
                self._knowledge_graph_filter = KnowledgeGraphFilter(epics=self.value)
            elif self.type == ScopeType.INCREMENT:
                # Convert string values to integers
                increments = [int(v) if isinstance(v, str) and v.isdigit() else v for v in self.value]
                self._knowledge_graph_filter = KnowledgeGraphFilter(increments=increments)
        
    # ... (truncated)
```

[!] WARNING (line 216)
Function "to_display_lines" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return workspace_directory / 'behavior_action_state.json'
    
    def to_display_lines(self, workspace_directory: 'Path') -> List[str]:
        """Render scope as display lines with hierarchical expansion.
        
        Returns plain text lines showing scope filter and matched items.
        """
        from pathlib import Path
        import json
        
        lines = []
        
        # Show the scope filter value
        filter_str = ', '.join(self.value) if isinstance(self.value, list) else str(self.value)
        lines.append(f"Scope Filter: {filter_str}")
    # ... (truncated)
```

[!] WARNING (line 268)
Function "_expand_file_paths" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return lines
    
    def _expand_file_paths(self, workspace_directory: 'Path') -> List['Path']:
        """Expand file scope paths to actual files that will be scanned."""
        from pathlib import Path
        import glob as glob_module
        
        all_files = []
        # Ensure value is treated as a list
        paths = self.value if isinstance(self.value, list) else [self.value]
        
        for path_str in paths:
            # Check if path contains glob patterns
            has_glob = any(char in path_str for char in ['*', '?', '['])
            
    # ... (truncated)
```

---

## simplify_control_flow
**behaviors.py** - 1 violation(s)

[!] WARNING (line 204)
Function "navigate_to" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return self.find_by_name(behavior_name) is not None

    def navigate_to(self, behavior_name: str):
        behavior = self.find_by_name(behavior_name)
        if behavior is None:
            raise ValueError(f"Behavior '{behavior_name}' not found")
        
        target_index = None
        for i, b in enumerate(self._behaviors):
            if b.name == behavior.name:
                target_index = i
                self._current_index = i
                break
        
        # When navigating to a behavior: mark all actions in previous behaviors as complete,
    # ... (truncated)
```

---

## simplify_control_flow
**repl_main.py** - 1 violation(s)

[!] WARNING (line 75)
Function "main" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python


def main():
    # Bot directory was set at module level to always be story_bot
    # (where behaviors are loaded from)
    bot_name = 'story_bot'
    
    workspace_directory = get_workspace_directory()
    
    bot_config_path = bot_directory / 'bot_config.json'
    
    if not bot_config_path.exists():
        print(f"ERROR: Bot config not found at {bot_config_path}")
        print("Please ensure you're running from the correct directory.")
        sys.exit(1)
    # ... (truncated)
```

---

## simplify_control_flow
**repl_session.py** - 3 violation(s)

[!] WARNING (line 418)
Function "_handle_current_command" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        )
    
    def _handle_current_command(self) -> REPLCommandResponse:
        """Re-execute current operation based on progress state"""
        if not self.has_current_action:
            return REPLCommandResponse(
                output="ERROR: No current action",
                response="ERROR: No current action",
                status="error"
            )
        
        # Extract operation from progress (behavior.action.operation)
        progress = self.get_progress_line()
        if '.' in progress and 'Progress: ' in progress:
            parts = progress.replace('Progress: ', '').split('.')
    # ... (truncated)
```

[!] WARNING (line 645)
Function "_handle_scope_command" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        )
    
    def _handle_scope_command(self, args: str = "") -> REPLCommandResponse:
        """Handle scope command"""
        if not args:
            # Show current scope
            output = self.cli_bot.get_scope_display()
            return REPLCommandResponse(
                output=output,
                response=output,
                status="success"
            )
        
        # Handle "all" - clears the scope filter
        if args.lower() == 'all':
    # ... (truncated)
```

[!] WARNING (line 820)
Function "_handle_dot_notation" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting

```python
            pass
    
    def _handle_dot_notation(self, command: str) -> REPLCommandResponse:
        """Handle dot notation commands (behavior.action.operation)"""
        # Parse dot notation: behavior.action.operation or action.operation or .operation
        parts = command.split()
        dot_path = parts[0]
        args = ' '.join(parts[1:]) if len(parts) > 1 else ""
        
        path_parts = dot_path.split('.')
        
        # . alone means current position
        if dot_path == '.':
            return self._handle_current_command()
        
    # ... (truncated)
```

---

## simplify_control_flow
**repl_status.py** - 3 violation(s)

[!] WARNING (line 48)
Function "hierarchical_status" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

```python
    
    @property
    def hierarchical_status(self) -> str:
        lines = []
        
        if not self.bot or not self.bot.behaviors:
            lines.append("No behaviors available")
            lines.append(self.formatter.subsection_separator())
            return "\n".join(lines)
        
        current_behavior_name = self.state.current_behavior_name
        current_action_name = self.state.current_action_name
        
        stage = self.state.stage_name
        
    # ... (truncated)
```

[!] WARNING (line 160)
Function "_get_instructions_params" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return "\n".join(lines)
    
    def _get_instructions_params(self, action) -> str:
        # Check if action has context_class with fields
        if hasattr(action, 'context_class') and action.context_class:
            try:
                import dataclasses
                if dataclasses.is_dataclass(action.context_class):
                    fields = [f.name for f in dataclasses.fields(action.context_class)]
                    if 'context' in fields:
                        return ' --context="..."'
            except:
                pass
        return ''
    
```

[!] WARNING (line 173)
Function "_get_submit_params" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return ''
    
    def _get_submit_params(self, action) -> str:
        params = []
        if hasattr(action, 'context_class') and action.context_class:
            try:
                import dataclasses
                if dataclasses.is_dataclass(action.context_class):
                    fields = [f.name for f in dataclasses.fields(action.context_class)]
                    if 'decisions' in fields:
                        params.append('--decisions="1:option,..."')
                    if 'assumptions_made' in fields or 'assumptions' in fields:
                        params.append('--assumptions="..."')
            except:
                pass
    # ... (truncated)
```

---

## stop_writing_useless_comments
**actions.py** - 1 violation(s)

[X] ERROR (line 263)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def is_action_completed(self, action_name: str) -> bool:
        """Check if an action is completed using positional logic.
        
        An action is considered completed if the current action is past it in the workflow.
        This matches the terminal formatter's logic.
        """
        action_names = self.names
```

---

## stop_writing_useless_comments
**action_context.py** - 26 violation(s)

[X] ERROR (line 26)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
@dataclass
class KnowledgeGraphFilter:
    """Filters content by knowledge graph nodes (stories, epics, increments).
    
    Used for filtering operations to specific parts of the story graph.
    """
    stories: List[str] = field(default_factory=list)
```

[X] ERROR (line 35)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def matches_story(self, story_name: str) -> bool:
        """Check if story matches filter."""
        if not self.stories:
```

[X] ERROR (line 41)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def matches_epic(self, epic_name: str) -> bool:
        """Check if epic matches filter."""
        if not self.epics:
```

[X] ERROR (line 47)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def filter_knowledge_graph(self, knowledge_graph: Dict[str, Any]) -> Dict[str, Any]:
        """Filter knowledge graph to only nodes matching this filter."""
        # For now, return full graph if no filters specified
```

[X] ERROR (line 57)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
@dataclass
class FileFilter:
    """Filters files by path patterns.
    
    Supports glob patterns for include/exclude.
    """
    include_patterns: List[str] = field(default_factory=list)
```

[X] ERROR (line 65)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def matches_file(self, file_path: Path) -> bool:
        """Check if file matches the filter."""
        if not self.include_patterns:
```

[X] ERROR (line 76)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def filter_files(self, file_list: List[Path]) -> List[Path]:
        """Filter file list to only files matching this filter."""
        if not self.include_patterns and not self.exclude_patterns:
```

[X] ERROR (line 85)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
@dataclass
class Scope:
    """Scope for filtering bot operations to specific content.
    
    Uses KnowledgeGraphFilter for story/epic/increment scoping
    and FileFilter for file-based scoping. Maintains backward compatibility
    with type/value/exclude API.
    
    The Scope object is responsible for its own persistence to the bot state file.
    """
    type: ScopeType = ScopeType.ALL
```

[X] ERROR (line 103)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def __post_init__(self):
        """Initialize filter objects from type/value/exclude."""
        # Create knowledge graph filter for story/epic/increment types
```

[X] ERROR (line 124)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def knowledge_graph_filter(self) -> Optional[KnowledgeGraphFilter]:
        """Get knowledge graph filter (lazy init if needed)."""
        return self._knowledge_graph_filter
```

[X] ERROR (line 129)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def file_filter(self) -> Optional[FileFilter]:
        """Get file filter (lazy init if needed)."""
        return self._file_filter
```

[X] ERROR (line 133)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def filters_knowledge_graph(self, knowledge_graph: Dict[str, Any]) -> Dict[str, Any]:
        """Filter knowledge graph using knowledge graph filter."""
        if self._knowledge_graph_filter:
```

[X] ERROR (line 139)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def filters_files(self, file_list: List[Path]) -> List[Path]:
        """Filter file list using file filter."""
        if self._file_filter:
```

[X] ERROR (line 171)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def apply_to_bot(self, workspace_directory: 'Path') -> None:
        """Clear old scope and store this scope to the bot state file.
        
        The Scope object is responsible for its own persistence.
        """
        import json
```

[X] ERROR (line 196)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @staticmethod
    def clear_from_bot(workspace_directory: 'Path') -> None:
        """Remove scope from the bot state file."""
        import json
```

[X] ERROR (line 213)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @staticmethod
    def _get_state_file_path(workspace_directory: 'Path') -> 'Path':
        """Get path to the bot state file."""
        return workspace_directory / 'behavior_action_state.json'
```

[X] ERROR (line 217)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def to_display_lines(self, workspace_directory: 'Path') -> List[str]:
        """Render scope as display lines with hierarchical expansion.
        
        Returns plain text lines showing scope filter and matched items.
        """
        from pathlib import Path
```

[X] ERROR (line 269)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _expand_file_paths(self, workspace_directory: 'Path') -> List['Path']:
        """Expand file scope paths to actual files that will be scanned."""
        from pathlib import Path
```

[X] ERROR (line 311)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _find_scope_matches_in_graph(self, graph_data: Dict[str, Any], scope_values: List[str]) -> List[str]:
        """Find and display scope matches from story graph."""
        lines = []
```

[X] ERROR (line 325)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _search_for_scope_match(self, epics: List[Dict], scope_val: str) -> Optional[List[str]]:
        """Search for scope match and return formatted lines with full hierarchy."""
        for epic in epics:
```

[X] ERROR (line 337)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _search_sub_epics(self, sub_epics: List[Dict], scope_val: str) -> Optional[List[str]]:
        """Search sub-epics for scope match."""
        for sub_epic in sub_epics:
```

[X] ERROR (line 349)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _search_stories(self, sub_epic: Dict, scope_val: str) -> Optional[List[str]]:
        """Search stories for scope match."""
        for story_group in sub_epic.get('story_groups', []):
```

[X] ERROR (line 362)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _matches_name(self, name: str, pattern: str) -> bool:
        """Check if pattern matches name (case-insensitive)."""
        return pattern.lower() in name.lower()
```

[X] ERROR (line 366)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _format_node_with_children(self, node: Dict[str, Any], node_type: str, indent: int) -> List[str]:
        """Format a node and its children recursively."""
        lines = []
```

[X] ERROR (line 426)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def get_decisions(self) -> Dict[str, Any]:
        """Get all decision attributes (exclude assumptions and internal attrs)."""
        excluded = {'assumptions'}
```

[X] ERROR (line 282)
Useless comment: "# Handle glob patterns" - delete it or improve the code instead

```python
            
            if has_glob:
                # Handle glob patterns
                # If not absolute, make it relative to workspace
```

---

## stop_writing_useless_comments
**behavior.py** - 1 violation(s)

[X] ERROR (line 63)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def is_completed(self) -> bool:
        """Check if this behavior is completed using positional logic.
        
        A behavior is completed if the current behavior (from bot.behaviors.current) 
        is past this behavior in the workflow order.
        """
        if not self.bot:
```

---

## stop_writing_useless_comments
**behaviors.py** - 5 violation(s)

[X] ERROR (line 66)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def completed_behaviors(self) -> List[str]:
        """Get list of completed behavior names."""
        completed = []
```

[X] ERROR (line 104)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def next(self) -> Optional['Behavior']:
        """Get the next behavior without changing current state."""
        next_index = self._current_index + 1
```

[X] ERROR (line 111)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def previous(self) -> Optional['Behavior']:
        """Get the previous behavior without changing current state."""
        if self._current_index is None or self._current_index <= 0:
```

[X] ERROR (line 120)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def advance(self) -> Dict[str, Any]:
        """Advance to the next action in the current behavior, or next behavior if at end.
        
        Returns:
            Dict with status and information about the advancement
        """
        if not self.current:
```

[X] ERROR (line 159)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def go_back(self) -> Dict[str, Any]:
        """Go back to the previous action in the current behavior, or previous behavior if at start.
        
        Returns:
            Dict with status and information about going back
        """
        if not self.current:
```

---

## stop_writing_useless_comments
**bot.py** - 11 violation(s)

[X] ERROR (line 67)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def help(self, topic: Optional[str] = None) -> Dict[str, Any]:
        """Display help information about the bot, behaviors, or actions.
        
        Args:
            topic: Optional topic for specific help (behavior name, action name, etc.)
        
        Returns:
            Dict with help information including behaviors, actions, and usage
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_help import REPLHelp
```

[X] ERROR (line 93)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
            
            def _get_instructions_params_hint(self, action):
                """Return parameter hints for instructions - stub implementation."""
                return ""
```

[X] ERROR (line 97)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
            
            def _get_submit_params_hint(self, action):
                """Return parameter hints for submit - stub implementation."""
                return ""
```

[X] ERROR (line 141)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def exit(self) -> Dict[str, Any]:
        """Exit the bot session gracefully.
        
        Returns:
            Dict with exit status and message
        """
        return {
```

[X] ERROR (line 152)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def scope(self, scope_filter: Optional[str] = None) -> Dict[str, Any]:
        """Set or view the scope filter for the current workflow.
        
        AI AGENTS: This command requires COMPLETE folder paths. When you pass a directory path,
        you MUST include the ENTIRE folder structure from root or working area.
        
        Args:
            scope_filter: Complete folder path or story name to filter by, or None to view current scope
        
        Returns:
            Dict with scope information or updated scope status
        """
        from agile_bot.bots.base_bot.src.actions.action_context import Scope, ScopeType
```

[X] ERROR (line 208)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def path(self, directory: Optional[str] = None) -> Dict[str, Any]:
        """Set or view the working directory.
        
        Args:
            directory: Path to set as working directory, or None to view current path
        
        Returns:
            Dict with path information or updated path status
        """
        if directory is None:
```

[X] ERROR (line 77)
Useless comment: "# Create a minimal session-like object for REPLHelp" - delete it or improve the code instead

```python
        from agile_bot.bots.base_bot.src.repl_cli.repl_help import REPLHelp
        
        # Create a minimal session-like object for REPLHelp
        class HelpContext:
```

[X] ERROR (line 167)
Useless comment: "# Return current scope" - delete it or improve the code instead

```python
        
        if scope_filter is None:
            # Return current scope
            # TODO: Load from persistent storage
```

[X] ERROR (line 217)
Useless comment: "# Return current working directory" - delete it or improve the code instead

```python
        """
        if directory is None:
            # Return current working directory
            current_path = self.bot_paths.workspace_directory
```

[X] ERROR (line 225)
Useless comment: "# Set new working directory" - delete it or improve the code instead

```python
            }
        
        # Set new working directory
        new_path = Path(directory)
```

[X] ERROR (line 236)
Useless comment: "# Update the bot paths" - delete it or improve the code instead

```python
            }
        
        # Update the bot paths
        self.bot_paths._workspace_directory = new_path
```

---

## stop_writing_useless_comments
**cli_base.py** - 2 violation(s)

[X] ERROR (line 6)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class CLIBase:
    """Base class for all CLI domain wrapper objects.
    
    Provides access to the formatter so each CLI object can be responsible
    for its own display formatting.
    """
    
```

[X] ERROR (line 17)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def formatter(self) -> OutputFormatter:
        """Access the output formatter for display rendering."""
        return self._formatter
```

---

## stop_writing_useless_comments
**cli_scope.py** - 6 violation(s)

[X] ERROR (line 11)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class CLIScope(CLIBase):
    """CLI wrapper for Scope that adds display formatting."""
    
```

[X] ERROR (line 20)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @classmethod
    def from_state_file(cls, workspace_directory: Path, formatter: OutputFormatter) -> Optional['CLIScope']:
        """Load scope from bot state file and wrap it."""
        try:
```

[X] ERROR (line 37)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def to_formatted_display(self) -> str:
        """Render scope with CLI-specific formatting (warnings, separators, and AI instructions)."""
        from agile_bot.bots.base_bot.src.actions.action_context import ScopeType
```

[X] ERROR (line 98)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _build_file_tree(self, scope_lines: list) -> list:
        """Build a hierarchical directory tree from file paths."""
        from pathlib import Path
```

[X] ERROR (line 128)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _render_tree(self, tree: dict, prefix: str, is_last: bool = True) -> list:
        """Recursively render tree structure with proper indentation."""
        lines = []
```

[X] ERROR (line 152)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def domain_scope(self) -> Scope:
        """Access the underlying domain Scope object."""
        return self._scope
```

---

## stop_writing_useless_comments
**repl_session.py** - 22 violation(s)

[X] ERROR (line 145)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def display_current_state(self, full=False) -> REPLStateDisplay:
        """Single source of truth for displaying current bot state.
        
        Returns REPLStateDisplay with formatted status output showing:
        - Bot name and paths
        - Current position header
        - Scope filter (if set)
        - Progress in workflow
        - Hierarchical behavior/action/operation tree
        """
        if not self.has_current_action:
```

[X] ERROR (line 244)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def get_context_header_for_ai(self) -> str:
        """Get status display as a string for AI context headers.
        
        This is a convenience method that extracts just the output string
        from display_current_state().
        """
        state_display = self.display_current_state()
```

[X] ERROR (line 253)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _convert_domain_result_to_repl_response(self, result: Dict[str, Any], command: str) -> REPLCommandResponse:
        """Convert a domain method result to a REPL response.
        
        Args:
            result: Dict returned from domain method
            command: The command that was executed
        
        Returns:
            REPLCommandResponse with appropriate formatting
        """
        status = result.get('status', 'success')
```

[X] ERROR (line 380)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_help_command(self, args: str = "") -> REPLCommandResponse:
        """Handle help command using bot.help"""
        if not args:
```

[X] ERROR (line 410)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_status_command(self) -> REPLCommandResponse:
        """Handle status command using bot.status"""
        state_display = self.display_current_state(full=True)
```

[X] ERROR (line 419)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_current_command(self) -> REPLCommandResponse:
        """Re-execute current operation based on progress state"""
        if not self.has_current_action:
```

[X] ERROR (line 448)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_next_command(self) -> REPLCommandResponse:
        """Handle next/advance navigation"""
        if not self.has_current_action:
```

[X] ERROR (line 484)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_back_command(self) -> REPLCommandResponse:
        """Handle back/previous navigation"""
        if not self.has_current_action:
```

[X] ERROR (line 530)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_instructions_command(self, args: str = "") -> REPLCommandResponse:
        """Handle instructions command"""
        if not self.has_current_action:
```

[X] ERROR (line 551)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_submit_command(self, args: str = "") -> REPLCommandResponse:
        """Handle submit command"""
        if not self.has_current_action:
```

[X] ERROR (line 572)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_confirm_command(self) -> REPLCommandResponse:
        """Handle confirm command"""
        if not self.has_current_action:
```

[X] ERROR (line 627)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_path_command(self, args: str = "") -> REPLCommandResponse:
        """Handle path/workspace command"""
        if not args:
```

[X] ERROR (line 646)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_scope_command(self, args: str = "") -> REPLCommandResponse:
        """Handle scope command"""
        if not args:
```

[X] ERROR (line 712)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_behavior_command(self, behavior_name: str) -> REPLCommandResponse:
        """Handle behavior navigation"""
        behavior = self.cli_bot.behaviors.domain_behaviors.find_by_name(behavior_name)
```

[X] ERROR (line 741)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def navigate_to_behavior_action(self, behavior_name: str, action_name: str):
        """Navigate to a specific behavior and action
        
        Raises:
            ValueError: If behavior or action not found
        """
        # Navigate to behavior
```

[X] ERROR (line 762)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _wrap_navigation_with_instructions(self) -> REPLCommandResponse:
        """After navigation, auto-execute instructions for new position"""
        return self._handle_instructions_command()
```

[X] ERROR (line 766)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _wrap_with_context_header(self, content: str, response_msg: str) -> REPLCommandResponse:
        """Wrap content with instructions header and CLI status section"""
        formatter = self.formatter
```

[X] ERROR (line 806)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _mark_behavior_complete(self, behavior_name: str) -> None:
        """Mark a behavior as complete in the state file"""
        state_file = self.workspace_directory / 'behavior_action_state.json'
```

[X] ERROR (line 821)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_dot_notation(self, command: str) -> REPLCommandResponse:
        """Handle dot notation commands (behavior.action.operation)"""
        # Parse dot notation: behavior.action.operation or action.operation or .operation
```

[X] ERROR (line 204)
Useless comment: "# Get scope display" - delete it or improve the code instead

```python
        lines.append(formatter.subsection_separator())
        
        # Get scope display
        scope_display = self.cli_bot.get_scope_display()
```

[X] ERROR (line 701)
Useless comment: "# Get the scope display lines" - delete it or improve the code instead

```python
        result = self.cli_bot.set_scope(scope)
        
        # Get the scope display lines
        output = self.cli_bot.get_scope_display()
```

[X] ERROR (line 748)
Useless comment: "# Get the behavior" - delete it or improve the code instead

```python
        # Navigate to behavior
        self.cli_bot.behaviors.domain_behaviors.navigate_to(behavior_name)
        # Get the behavior
        behavior = self.cli_bot.behaviors.domain_behaviors.find_by_name(behavior_name)
```

---

## stop_writing_useless_comments
**cli_behavior.py** - 1 violation(s)

[X] ERROR (line 48)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def help(self) -> str:
        """Get help for this specific behavior"""
        from agile_bot.bots.base_bot.src.repl_cli.repl_help import BehaviorHelp
```

---

## stop_writing_useless_comments
**cli_behaviors.py** - 2 violation(s)

[X] ERROR (line 66)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def help(self) -> str:
        """Get help for behaviors"""
        behaviors_list = ", ".join(self.all)
```

[X] ERROR (line 80)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def __iter__(self):
        """Make CLIBehaviors iterable - yields CLIBehavior objects for each behavior"""
        for behavior in self._behaviors._behaviors:
```

---

## stop_writing_useless_comments
**cli_bot.py** - 5 violation(s)

[X] ERROR (line 55)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def change_path(self, new_path: str) -> dict:
        """Change the workspace path. Returns result dict with status and message."""
        import json
```

[X] ERROR (line 78)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def set_scope(self, scope) -> dict:
        """Set the scope filter. Scope manages its own persistence, ensuring only one scope exists."""
        # Scope object handles clearing old scope and storing itself
```

[X] ERROR (line 90)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def clear_scope(self) -> dict:
        """Clear the scope filter. Scope manages its own removal from state."""
        from agile_bot.bots.base_bot.src.actions.action_context import Scope
```

[X] ERROR (line 99)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def get_scope_display(self) -> str:
        """Get the current scope display formatted by CLIScope."""
        scope_data = self._session.get_stored_scope()
```

[X] ERROR (line 109)
Useless comment: "# Return formatted error with details for debugging" - delete it or improve the code instead

```python
                return cli_scope.to_formatted_display()
            except Exception as e:
                # Return formatted error with details for debugging
                return f"{self._session.formatter.scope_icon()} **Scope**\n{self._session.formatter.scope_icon()} Error loading scope: {str(e)}"
```

---

## stop_writing_useless_comments
**markdown_formatter.py** - 2 violation(s)

[X] ERROR (line 7)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def section_separator(self) -> str:
        """Heavy line for major section breaks"""
        return "━" * 90
```

[X] ERROR (line 11)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def subsection_separator(self) -> str:
        """Light line for subsection breaks"""
        return "─" * 60
```

---

## stop_writing_useless_comments
**output_formatter.py** - 9 violation(s)

[X] ERROR (line 8)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @abstractmethod
    def section_separator(self) -> str:
        """Heavy line for major section breaks"""
        pass
```

[X] ERROR (line 12)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def subsection_separator(self) -> str:
        """Light line for subsection breaks - defaults to same as section_separator"""
        return self.section_separator()
```

[X] ERROR (line 29)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    # Emoji/icon methods for different contexts
    def bot_icon(self) -> str:
        """Icon for bot/AI context"""
        return ""
```

[X] ERROR (line 33)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def workspace_icon(self) -> str:
        """Icon for workspace/folder context"""
        return ""
```

[X] ERROR (line 37)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def path_icon(self) -> str:
        """Icon for file path context"""
        return ""
```

[X] ERROR (line 41)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def scope_icon(self) -> str:
        """Icon for scope/target context"""
        return ""
```

[X] ERROR (line 45)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def position_icon(self) -> str:
        """Icon for current position/location"""
        return ""
```

[X] ERROR (line 49)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def currently_executing_icon(self) -> str:
        """Icon for currently executing action"""
        return ""
```

[X] ERROR (line 53)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def file_icon(self) -> str:
        """Icon for file references"""
        return ""
```

---

## stop_writing_useless_comments
**terminal_formatter.py** - 2 violation(s)

[X] ERROR (line 7)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def section_separator(self) -> str:
        """Heavy line for major section breaks"""
        return "=" * 60
```

[X] ERROR (line 11)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def subsection_separator(self) -> str:
        """Light line for subsection breaks"""
        return "-" * 60
```

---

## stop_writing_useless_comments
**cli_action.py** - 1 violation(s)

[X] ERROR (line 109)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def help(self) -> str:
        """Get help for this specific action"""
        from agile_bot.bots.base_bot.src.repl_cli.repl_help import ActionHelp
```

---

## stop_writing_useless_comments
**cli_actions.py** - 3 violation(s)

[X] ERROR (line 60)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def find_by_name(self, name: str) -> Optional[CLIAction]:
        """Find action by name (alias for get_action to match domain API)"""
        return self.get_action(name)
```

[X] ERROR (line 83)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def help(self) -> str:
        """Get help for actions"""
        actions_list = ", ".join(self.all)
```

[X] ERROR (line 97)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def __iter__(self):
        """Make CLIActions iterable - yields CLIAction objects for each action"""
        for action_name in self._actions.names:
```

---

Completed: 2025-12-28 18:54:51
Total violations: 183
Scanners executed: 30
