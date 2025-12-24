# Validation Status - code
Started: 2025-12-23 23:46:19
Files: 258

## avoid_excessive_guards
**actions.py** - 1 violation(s)

[!] WARNING (line 189)
Line 189: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    def is_final_action(self) -> bool:
        try:
            if self.current is None:
                return False
            action_names = self.names
```

---

## avoid_excessive_guards
**cli_action_parsers.py** - 1 violation(s)

[!] WARNING (line 74)
Line 74: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
            value = parse_json_dict(value)
        
        if value is not None:
            kwargs[field_name] = value
    
```

---

## avoid_excessive_guards
**repl_session.py** - 1 violation(s)

[!] WARNING (line 344)
Line 344: Variable truthiness check detected (if not args:). Assume variable exists - let code fail fast if missing.

```python
        """Parse --param value and --param "value with spaces" from command args."""
        params = {}
        if not args:
            return params
        
```

---

## avoid_excessive_guards
**rules.py** - 1 violation(s)

[!] WARNING (line 144)
Line 144: Variable truthiness check detected (if changed:). Assume variable exists - let code fail fast if missing.

```python
        for file_type, file_list in files.items():
            changed = [f for f in file_list if f.stat().st_mtime > last_report_time]
            if changed:
                changed_files[file_type] = changed
        
```

---

## avoid_excessive_guards
**meta.py** - 1 violation(s)

[!] WARNING (line 29)
Line 29: Variable truthiness check detected (if not args:). Assume variable exists - let code fail fast if missing.

```python
        args = args.strip()
        
        if not args:
            output = self.help_resource.main_help
        else:
            if not self.has_current_behavior:
                return self.error_no_current_behavior()
            action_help = self.help_resource.action_help(self.current_behavior_name, args)
            if not action_help:
                behavior_help = self.help_resource.behavior_help(self.current_behavior_name)
                if not behavior_help:
                    return self.error_behavior_not_found(self.current_behavior_name)
                output = f"ERROR: Action '{args}' not found"
            else:
                output = action_help.help_text
        
```

---

## avoid_excessive_guards
**state.py** - 1 violation(s)

[!] WARNING (line 148)
Line 148: Variable truthiness check detected (if not args:). Assume variable exists - let code fail fast if missing.

```python
    def execute(self, args: str = "") -> REPLCommandResponse:
        args = args.strip()
        if not args:
            return REPLCommandResponse(
                output="ERROR: No scope specified",
                response="ERROR: No scope specified",
                status="error"
            )
        return REPLCommandResponse(
```

---

## eliminate_duplication
**cli_parser_generator_visitor.py** - 1 violation(s)

[X] ERROR (line 28)
Duplicate code detected: functions visit_behavior, visit_action_help_section_header have identical bodies - extract to shared function

---

## eliminate_duplication
**navigation.py** - 1 violation(s)

[X] ERROR (line 56)
Duplicate code detected: functions _execute_instructions, _execute_instructions have identical bodies - extract to shared function

---

## eliminate_duplication
**repl_command.py** - 1 violation(s)

[X] ERROR (line 12)
Duplicate code detected: functions name, execute have identical bodies - extract to shared function

---


## Cross-File Duplication Analysis
Scanning 258 files...
Extracted 3745 code blocks
Starting 7010640 pairwise comparisons...
Comparing: 0% (32,969/7,010,640) - 0 violations - ETA: 2116s  
Comparing: 0% (55,321/7,010,640) - 0 violations - ETA: 2514s  
Comparing: 1% (79,171/7,010,640) - 0 violations - ETA: 2626s  
Comparing: 1% (100,242/7,010,640) - 0 violations - ETA: 2757s  
Comparing: 1% (118,059/7,010,640) - 0 violations - ETA: 2919s  
Comparing: 2% (143,016/7,010,640) - 0 violations - ETA: 2881s  
Comparing: 2% (161,307/7,010,640) - 0 violations - ETA: 2972s  
Comparing: 2% (178,107/7,010,640) - 2 violations - ETA: 3069s  
Comparing: 2% (208,839/7,010,640) - 2 violations - ETA: 2931s  
Comparing: 3% (222,967/7,010,640) - 2 violations - ETA: 3044s  
Comparing: 3% (236,513/7,010,640) - 2 violations - ETA: 3150s  
Comparing: 3% (248,479/7,010,640) - 2 violations - ETA: 3265s  
Comparing: 3% (259,435/7,010,640) - 2 violations - ETA: 3383s  
Comparing: 3% (277,505/7,010,640) - 2 violations - ETA: 3397s  
Comparing: 4% (307,626/7,010,640) - 2 violations - ETA: 3268s  
Comparing: 4% (333,864/7,010,640) - 2 violations - ETA: 3199s  
Comparing: 5% (356,582/7,010,640) - 2 violations - ETA: 3172s  
Comparing: 5% (376,572/7,010,640) - 2 violations - ETA: 3171s  
Comparing: 5% (403,082/7,010,640) - 2 violations - ETA: 3114s  
Comparing: 6% (426,336/7,010,640) - 2 violations - ETA: 3088s  
Comparing: 6% (437,916/7,010,640) - 2 violations - ETA: 3152s  
Comparing: 6% (456,145/7,010,640) - 2 violations - ETA: 3161s  
Comparing: 6% (471,311/7,010,640) - 2 violations - ETA: 3191s  
Comparing: 7% (496,208/7,010,640) - 2 violations - ETA: 3151s  
Comparing: 7% (515,847/7,010,640) - 2 violations - ETA: 3147s  
Comparing: 7% (544,180/7,010,640) - 2 violations - ETA: 3089s  
Comparing: 8% (572,756/7,010,640) - 2 violations - ETA: 3035s  
Comparing: 8% (604,486/7,010,640) - 2 violations - ETA: 2967s  
Comparing: 9% (632,753/7,010,640) - 2 violations - ETA: 2923s  
Comparing: 9% (649,644/7,010,640) - 2 violations - ETA: 2937s  
Comparing: 9% (662,129/7,010,640) - 2 violations - ETA: 2972s  
Comparing: 9% (699,673/7,010,640) - 2 violations - ETA: 2886s  
Comparing: 10% (736,724/7,010,640) - 2 violations - ETA: 2810s  
Comparing: 10% (770,176/7,010,640) - 2 violations - ETA: 2755s  
Comparing: 11% (797,728/7,010,640) - 2 violations - ETA: 2726s  
Comparing: 11% (823,140/7,010,640) - 2 violations - ETA: 2706s  
Comparing: 12% (847,642/7,010,640) - 2 violations - ETA: 2690s  
Comparing: 12% (867,283/7,010,640) - 2 violations - ETA: 2691s  
Comparing: 12% (887,775/7,010,640) - 7 violations - ETA: 2689s  
Found 10 violations so far...
Found 20 violations so far...
Found 30 violations so far...
Comparing: 13% (914,168/7,010,640) - 30 violations - ETA: 2667s  
Comparing: 13% (944,948/7,010,640) - 30 violations - ETA: 2631s  
Comparing: 13% (977,323/7,010,640) - 30 violations - ETA: 2592s  
Comparing: 14% (1,013,893/7,010,640) - 30 violations - ETA: 2543s  
Comparing: 14% (1,036,702/7,010,640) - 30 violations - ETA: 2535s  
Comparing: 14% (1,051,470/7,010,640) - 30 violations - ETA: 2550s  
Found 40 violations so far...
Comparing: 15% (1,075,189/7,010,640) - 48 violations - ETA: 2539s  
Found 50 violations so far...
Found 60 violations so far...
Comparing: 15% (1,105,532/7,010,640) - 61 violations - ETA: 2510s  
Comparing: 16% (1,135,815/7,010,640) - 61 violations - ETA: 2482s  
Comparing: 16% (1,168,246/7,010,640) - 61 violations - ETA: 2450s  
Comparing: 16% (1,191,018/7,010,640) - 61 violations - ETA: 2443s  
Comparing: 17% (1,213,284/7,010,640) - 61 violations - ETA: 2437s  
Comparing: 17% (1,240,763/7,010,640) - 61 violations - ETA: 2418s  
Comparing: 18% (1,264,492/7,010,640) - 61 violations - ETA: 2408s  
Comparing: 18% (1,283,806/7,010,640) - 61 violations - ETA: 2408s  
Comparing: 18% (1,300,267/7,010,640) - 61 violations - ETA: 2415s  
Comparing: 18% (1,320,856/7,010,640) - 61 violations - ETA: 2412s  
Comparing: 19% (1,340,690/7,010,640) - 61 violations - ETA: 2410s  
Comparing: 19% (1,356,706/7,010,640) - 61 violations - ETA: 2417s  
Comparing: 19% (1,390,197/7,010,640) - 61 violations - ETA: 2385s  
Comparing: 20% (1,421,162/7,010,640) - 61 violations - ETA: 2359s  
Comparing: 20% (1,450,428/7,010,640) - 66 violations - ETA: 2338s  
Found 70 violations so far...
Found 80 violations so far...
Comparing: 21% (1,477,413/7,010,640) - 80 violations - ETA: 2322s  
Comparing: 21% (1,516,650/7,010,640) - 80 violations - ETA: 2282s  
Comparing: 22% (1,561,916/7,010,640) - 80 violations - ETA: 2232s  
Comparing: 22% (1,609,727/7,010,640) - 80 violations - ETA: 2180s  
Comparing: 23% (1,644,831/7,010,640) - 81 violations - ETA: 2153s  
Comparing: 23% (1,676,262/7,010,640) - 89 violations - ETA: 2132s  
Comparing: 24% (1,706,793/7,010,640) - 89 violations - ETA: 2113s  
Comparing: 24% (1,729,488/7,010,640) - 89 violations - ETA: 2107s  
Comparing: 24% (1,750,021/7,010,640) - 89 violations - ETA: 2104s  
Comparing: 25% (1,775,718/7,010,640) - 89 violations - ETA: 2093s  
Comparing: 25% (1,794,443/7,010,640) - 89 violations - ETA: 2093s  
Comparing: 26% (1,823,389/7,010,640) - 89 violations - ETA: 2076s  
Found 90 violations so far...
Comparing: 26% (1,856,488/7,010,640) - 91 violations - ETA: 2054s  
Comparing: 26% (1,887,528/7,010,640) - 92 violations - ETA: 2035s  
Comparing: 27% (1,913,238/7,010,640) - 92 violations - ETA: 2024s  
Comparing: 27% (1,943,790/7,010,640) - 94 violations - ETA: 2007s  
Comparing: 28% (1,966,476/7,010,640) - 94 violations - ETA: 2000s  
Comparing: 28% (1,985,390/7,010,640) - 94 violations - ETA: 1999s  
Comparing: 28% (2,001,025/7,010,640) - 94 violations - ETA: 2002s  
Comparing: 28% (2,015,901/7,010,640) - 94 violations - ETA: 2007s  
Comparing: 28% (2,030,113/7,010,640) - 94 violations - ETA: 2011s  
Comparing: 29% (2,042,503/7,010,640) - 94 violations - ETA: 2018s  
Comparing: 29% (2,053,789/7,010,640) - 94 violations - ETA: 2027s  
Comparing: 29% (2,064,570/7,010,640) - 94 violations - ETA: 2036s  
Comparing: 29% (2,085,320/7,010,640) - 94 violations - ETA: 2031s  
Comparing: 30% (2,111,231/7,010,640) - 94 violations - ETA: 2019s  
Comparing: 30% (2,132,637/7,010,640) - 94 violations - ETA: 2012s  
Comparing: 30% (2,161,114/7,010,640) - 94 violations - ETA: 1997s  
Comparing: 31% (2,193,498/7,010,640) - 95 violations - ETA: 1976s  
Comparing: 31% (2,226,316/7,010,640) - 95 violations - ETA: 1955s  
Comparing: 32% (2,253,311/7,010,640) - 95 violations - ETA: 1942s  
Comparing: 32% (2,275,459/7,010,640) - 95 violations - ETA: 1935s  
Comparing: 32% (2,295,818/7,010,640) - 95 violations - ETA: 1930s  
Comparing: 33% (2,320,836/7,010,640) - 95 violations - ETA: 1919s  
Found 100 violations so far...
Comparing: 33% (2,349,711/7,010,640) - 103 violations - ETA: 1904s  
Found 110 violations so far...
Comparing: 33% (2,373,977/7,010,640) - 114 violations - ETA: 1894s  
Comparing: 34% (2,397,989/7,010,640) - 114 violations - ETA: 1885s  
Comparing: 34% (2,420,687/7,010,640) - 116 violations - ETA: 1877s  
Found 120 violations so far...
Comparing: 34% (2,440,308/7,010,640) - 121 violations - ETA: 1872s  
Comparing: 35% (2,467,818/7,010,640) - 121 violations - ETA: 1859s  
Comparing: 35% (2,495,560/7,010,640) - 121 violations - ETA: 1845s  
Comparing: 35% (2,520,625/7,010,640) - 121 violations - ETA: 1834s  
Comparing: 36% (2,532,913/7,010,640) - 123 violations - ETA: 1838s  
Comparing: 36% (2,537,965/7,010,640) - 123 violations - ETA: 1850s  
Comparing: 36% (2,543,372/7,010,640) - 123 violations - ETA: 1861s  
Comparing: 36% (2,548,675/7,010,640) - 123 violations - ETA: 1873s  
Comparing: 36% (2,553,937/7,010,640) - 123 violations - ETA: 1884s  
Comparing: 36% (2,559,173/7,010,640) - 123 violations - ETA: 1896s  
Found 130 violations so far...
Comparing: 36% (2,579,373/7,010,640) - 136 violations - ETA: 1889s  
Found 140 violations so far...
Comparing: 37% (2,601,912/7,010,640) - 148 violations - ETA: 1880s  
Found 150 violations so far...
Found 160 violations so far...
Comparing: 37% (2,632,725/7,010,640) - 167 violations - ETA: 1862s  
Found 170 violations so far...
Found 180 violations so far...
Found 190 violations so far...
Found 200 violations so far...
Comparing: 38% (2,678,106/7,010,640) - 202 violations - ETA: 1828s  
Found 210 violations so far...
Found 220 violations so far...
Found 230 violations so far...
Found 240 violations so far...
Found 250 violations so far...
Comparing: 38% (2,711,748/7,010,640) - 257 violations - ETA: 1807s  
Found 260 violations so far...
Found 270 violations so far...
Found 280 violations so far...
Found 290 violations so far...
Found 300 violations so far...
Found 310 violations so far...
Comparing: 39% (2,741,658/7,010,640) - 315 violations - ETA: 1790s  
Found 320 violations so far...
Found 330 violations so far...
Found 340 violations so far...
Found 350 violations so far...
Found 360 violations so far...
Comparing: 39% (2,765,392/7,010,640) - 360 violations - ETA: 1780s  
Found 370 violations so far...
Found 380 violations so far...
Found 390 violations so far...
Comparing: 39% (2,802,211/7,010,640) - 397 violations - ETA: 1757s  
Found 400 violations so far...
Comparing: 40% (2,833,704/7,010,640) - 409 violations - ETA: 1739s  
Comparing: 40% (2,854,527/7,010,640) - 409 violations - ETA: 1732s  
Comparing: 41% (2,889,930/7,010,640) - 409 violations - ETA: 1711s  
Found 410 violations so far...
Comparing: 41% (2,927,615/7,010,640) - 415 violations - ETA: 1687s  
Found 420 violations so far...
Found 430 violations so far...
Comparing: 42% (2,963,989/7,010,640) - 438 violations - ETA: 1665s  
Found 440 violations so far...
Found 450 violations so far...
Found 460 violations so far...
Found 470 violations so far...
Found 480 violations so far...
Comparing: 42% (2,991,317/7,010,640) - 485 violations - ETA: 1652s  
Found 490 violations so far...
Found 500 violations so far...
Found 510 violations so far...
Found 520 violations so far...
Found 530 violations so far...
Comparing: 42% (3,013,503/7,010,640) - 536 violations - ETA: 1644s  
Found 540 violations so far...
Found 550 violations so far...
Comparing: 43% (3,039,087/7,010,640) - 558 violations - ETA: 1633s  
Found 560 violations so far...
Comparing: 43% (3,072,811/7,010,640) - 560 violations - ETA: 1614s  
Comparing: 44% (3,099,895/7,010,640) - 560 violations - ETA: 1602s  
Comparing: 44% (3,126,572/7,010,640) - 560 violations - ETA: 1590s  
Comparing: 44% (3,150,795/7,010,640) - 562 violations - ETA: 1580s  
Comparing: 45% (3,184,113/7,010,640) - 569 violations - ETA: 1562s  
Comparing: 45% (3,218,257/7,010,640) - 569 violations - ETA: 1543s  
Comparing: 46% (3,244,374/7,010,640) - 569 violations - ETA: 1532s  
Found 570 violations so far...
Comparing: 46% (3,267,591/7,010,640) - 575 violations - ETA: 1523s  
Comparing: 46% (3,294,507/7,010,640) - 579 violations - ETA: 1511s  
Comparing: 47% (3,318,136/7,010,640) - 579 violations - ETA: 1502s  
Comparing: 47% (3,335,189/7,010,640) - 579 violations - ETA: 1498s  
Comparing: 47% (3,345,340/7,010,640) - 579 violations - ETA: 1501s  
Comparing: 48% (3,368,228/7,010,640) - 579 violations - ETA: 1492s  
Comparing: 48% (3,389,188/7,010,640) - 579 violations - ETA: 1485s  
Comparing: 48% (3,407,238/7,010,640) - 579 violations - ETA: 1480s  
Comparing: 48% (3,424,186/7,010,640) - 579 violations - ETA: 1476s  
Comparing: 49% (3,439,435/7,010,640) - 579 violations - ETA: 1474s  
Comparing: 49% (3,454,628/7,010,640) - 579 violations - ETA: 1472s  
Comparing: 49% (3,467,844/7,010,640) - 579 violations - ETA: 1471s  
Comparing: 49% (3,481,214/7,010,640) - 579 violations - ETA: 1470s  
Comparing: 49% (3,493,348/7,010,640) - 579 violations - ETA: 1470s  
Comparing: 50% (3,507,290/7,010,640) - 579 violations - ETA: 1468s  
Comparing: 50% (3,530,649/7,010,640) - 579 violations - ETA: 1458s  
Found 580 violations so far...
Comparing: 50% (3,553,762/7,010,640) - 580 violations - ETA: 1449s  
Comparing: 51% (3,591,011/7,010,640) - 580 violations - ETA: 1428s  
Comparing: 51% (3,620,981/7,010,640) - 580 violations - ETA: 1413s  
Comparing: 52% (3,661,048/7,010,640) - 580 violations - ETA: 1390s  
Comparing: 52% (3,701,802/7,010,640) - 580 violations - ETA: 1367s  
Comparing: 53% (3,737,450/7,010,640) - 580 violations - ETA: 1348s  
Comparing: 53% (3,768,177/7,010,640) - 580 violations - ETA: 1333s  
Comparing: 54% (3,788,058/7,010,640) - 580 violations - ETA: 1327s  
Comparing: 54% (3,810,237/7,010,640) - 580 violations - ETA: 1318s  
Comparing: 54% (3,837,273/7,010,640) - 580 violations - ETA: 1306s  
Comparing: 55% (3,859,500/7,010,640) - 580 violations - ETA: 1298s  
Found 590 violations so far...
Found 600 violations so far...
Found 610 violations so far...
Found 620 violations so far...
Found 630 violations so far...
Found 640 violations so far...
Found 650 violations so far...
Found 660 violations so far...
Found 670 violations so far...
Found 680 violations so far...
Comparing: 55% (3,893,841/7,010,640) - 688 violations - ETA: 1280s  
Found 690 violations so far...
Found 700 violations so far...
Found 710 violations so far...
Found 720 violations so far...
Found 730 violations so far...
Found 740 violations so far...
Comparing: 55% (3,925,713/7,010,640) - 741 violations - ETA: 1265s  
Found 750 violations so far...
Found 760 violations so far...
Comparing: 56% (3,949,479/7,010,640) - 764 violations - ETA: 1255s  
Found 770 violations so far...
Found 780 violations so far...
Found 790 violations so far...
Found 800 violations so far...
Found 810 violations so far...
Comparing: 56% (3,982,245/7,010,640) - 818 violations - ETA: 1239s  
Comparing: 57% (4,018,723/7,010,640) - 819 violations - ETA: 1221s  
Comparing: 57% (4,042,796/7,010,640) - 819 violations - ETA: 1211s  
Comparing: 58% (4,066,372/7,010,640) - 819 violations - ETA: 1201s  
Comparing: 58% (4,086,807/7,010,640) - 819 violations - ETA: 1194s  
Comparing: 58% (4,104,548/7,010,640) - 819 violations - ETA: 1189s  
Comparing: 58% (4,120,887/7,010,640) - 819 violations - ETA: 1185s  
Comparing: 59% (4,136,525/7,010,640) - 819 violations - ETA: 1181s  
Comparing: 59% (4,156,345/7,010,640) - 819 violations - ETA: 1174s  
Found 820 violations so far...
Found 830 violations so far...
Found 840 violations so far...
Found 850 violations so far...
Comparing: 59% (4,184,728/7,010,640) - 853 violations - ETA: 1161s  
Found 860 violations so far...
Comparing: 60% (4,217,933/7,010,640) - 867 violations - ETA: 1145s  
Found 870 violations so far...
Found 880 violations so far...
Found 890 violations so far...
Comparing: 60% (4,248,638/7,010,640) - 898 violations - ETA: 1131s  
Found 900 violations so far...
Found 910 violations so far...
Found 920 violations so far...
Found 930 violations so far...
Found 940 violations so far...
Found 950 violations so far...
Found 960 violations so far...
Found 970 violations so far...
Found 980 violations so far...
Found 990 violations so far...
Comparing: 61% (4,282,172/7,010,640) - 990 violations - ETA: 1115s  
Comparing: 61% (4,313,340/7,010,640) - 993 violations - ETA: 1100s  
Comparing: 61% (4,339,822/7,010,640) - 994 violations - ETA: 1089s  
Found 1000 violations so far...
Found 1010 violations so far...
Comparing: 62% (4,373,179/7,010,640) - 1018 violations - ETA: 1073s  
Found 1020 violations so far...
Comparing: 62% (4,394,382/7,010,640) - 1021 violations - ETA: 1065s  
Found 1030 violations so far...
Found 1040 violations so far...
Found 1050 violations so far...
Found 1060 violations so far...
Found 1070 violations so far...
Comparing: 63% (4,425,726/7,010,640) - 1074 violations - ETA: 1051s  
Found 1080 violations so far...
Found 1090 violations so far...
Found 1100 violations so far...
Comparing: 63% (4,458,267/7,010,640) - 1106 violations - ETA: 1036s  
Comparing: 63% (4,484,416/7,010,640) - 1107 violations - ETA: 1025s  
Found 1110 violations so far...
Found 1120 violations so far...
Comparing: 64% (4,520,267/7,010,640) - 1121 violations - ETA: 1008s  
Found 1130 violations so far...
Found 1140 violations so far...
Found 1150 violations so far...
Found 1160 violations so far...
Found 1170 violations so far...
Comparing: 64% (4,550,256/7,010,640) - 1171 violations - ETA: 994s  
Found 1180 violations so far...
Found 1190 violations so far...
Found 1200 violations so far...
Found 1210 violations so far...
Found 1220 violations so far...
Found 1230 violations so far...
Comparing: 65% (4,580,142/7,010,640) - 1234 violations - ETA: 981s  
Comparing: 65% (4,604,548/7,010,640) - 1234 violations - ETA: 971s  
Found 1240 violations so far...
Found 1250 violations so far...
Found 1260 violations so far...
Found 1270 violations so far...
Found 1280 violations so far...
Found 1290 violations so far...
Found 1300 violations so far...
Found 1310 violations so far...
Comparing: 66% (4,639,808/7,010,640) - 1315 violations - ETA: 955s  
Comparing: 66% (4,674,170/7,010,640) - 1315 violations - ETA: 939s  
Comparing: 67% (4,697,546/7,010,640) - 1315 violations - ETA: 930s  
Found 1320 violations so far...
Found 1330 violations so far...
Comparing: 67% (4,719,862/7,010,640) - 1338 violations - ETA: 922s  
Found 1340 violations so far...
Found 1350 violations so far...
Found 1360 violations so far...
Found 1370 violations so far...
Found 1380 violations so far...
Found 1390 violations so far...
Found 1400 violations so far...
Found 1410 violations so far...
Found 1420 violations so far...
Comparing: 67% (4,756,062/7,010,640) - 1427 violations - ETA: 905s  
Found 1430 violations so far...
Found 1440 violations so far...
Found 1450 violations so far...
Found 1460 violations so far...
Found 1470 violations so far...
Comparing: 68% (4,787,955/7,010,640) - 1473 violations - ETA: 891s  
Found 1480 violations so far...
Comparing: 68% (4,817,512/7,010,640) - 1483 violations - ETA: 878s  
Comparing: 69% (4,846,338/7,010,640) - 1486 violations - ETA: 866s  
Comparing: 69% (4,885,020/7,010,640) - 1486 violations - ETA: 848s  
Comparing: 70% (4,917,329/7,010,640) - 1486 violations - ETA: 834s  
Comparing: 70% (4,958,283/7,010,640) - 1486 violations - ETA: 815s  
Comparing: 71% (4,995,187/7,010,640) - 1486 violations - ETA: 798s  
Comparing: 71% (5,030,025/7,010,640) - 1486 violations - ETA: 783s  
Comparing: 72% (5,056,035/7,010,640) - 1486 violations - ETA: 773s  
Comparing: 72% (5,084,888/7,010,640) - 1486 violations - ETA: 761s  
Comparing: 72% (5,107,992/7,010,640) - 1486 violations - ETA: 752s  
Comparing: 73% (5,133,525/7,010,640) - 1486 violations - ETA: 742s  
Comparing: 73% (5,156,787/7,010,640) - 1486 violations - ETA: 733s  
Comparing: 73% (5,175,704/7,010,640) - 1486 violations - ETA: 726s  
Comparing: 74% (5,192,948/7,010,640) - 1486 violations - ETA: 721s  
Comparing: 74% (5,207,801/7,010,640) - 1486 violations - ETA: 716s  
Found 1490 violations so far...
Found 1500 violations so far...
Found 1510 violations so far...
Comparing: 74% (5,230,840/7,010,640) - 1518 violations - ETA: 707s  
Found 1520 violations so far...
Found 1530 violations so far...
Found 1540 violations so far...
Found 1550 violations so far...
Found 1560 violations so far...
Found 1570 violations so far...
Found 1580 violations so far...
Found 1590 violations so far...
Found 1600 violations so far...
Found 1610 violations so far...
Found 1620 violations so far...
Found 1630 violations so far...
Found 1640 violations so far...
Comparing: 75% (5,264,731/7,010,640) - 1640 violations - ETA: 693s  
Found 1650 violations so far...
Found 1660 violations so far...
Found 1670 violations so far...
Found 1680 violations so far...
Found 1690 violations so far...
Found 1700 violations so far...
Found 1710 violations so far...
Found 1720 violations so far...
Found 1730 violations so far...
Comparing: 75% (5,296,550/7,010,640) - 1737 violations - ETA: 679s  
Found 1740 violations so far...
Found 1750 violations so far...
Found 1760 violations so far...
Found 1770 violations so far...
Found 1780 violations so far...
Found 1790 violations so far...
Found 1800 violations so far...
Found 1810 violations so far...
Found 1820 violations so far...
Found 1830 violations so far...
Found 1840 violations so far...
Found 1850 violations so far...
Comparing: 75% (5,327,845/7,010,640) - 1854 violations - ETA: 666s  
Found 1860 violations so far...
Found 1870 violations so far...
Comparing: 76% (5,354,833/7,010,640) - 1873 violations - ETA: 655s  
Found 1880 violations so far...
Found 1890 violations so far...
Found 1900 violations so far...
Comparing: 76% (5,382,223/7,010,640) - 1904 violations - ETA: 644s  
Found 1910 violations so far...
Found 1920 violations so far...
Comparing: 77% (5,411,476/7,010,640) - 1925 violations - ETA: 632s  
Comparing: 77% (5,442,381/7,010,640) - 1927 violations - ETA: 619s  
Found 1930 violations so far...
Comparing: 78% (5,483,254/7,010,640) - 1939 violations - ETA: 601s  
Comparing: 78% (5,514,010/7,010,640) - 1939 violations - ETA: 589s  
Comparing: 79% (5,540,080/7,010,640) - 1939 violations - ETA: 578s  
Found 1940 violations so far...
Comparing: 79% (5,568,090/7,010,640) - 1940 violations - ETA: 567s  
Found 1950 violations so far...
Found 1960 violations so far...
Found 1970 violations so far...
Found 1980 violations so far...
Found 1990 violations so far...
Found 2000 violations so far...
Found 2010 violations so far...
Found 2020 violations so far...
Found 2030 violations so far...
Found 2040 violations so far...
Found 2050 violations so far...
Comparing: 79% (5,598,019/7,010,640) - 2055 violations - ETA: 555s  
Found 2060 violations so far...
Found 2070 violations so far...
Found 2080 violations so far...
Found 2090 violations so far...
Found 2100 violations so far...
Found 2110 violations so far...
Found 2120 violations so far...
Found 2130 violations so far...
Comparing: 80% (5,630,665/7,010,640) - 2132 violations - ETA: 541s  
Found 2140 violations so far...
Found 2150 violations so far...
Found 2160 violations so far...
Comparing: 80% (5,660,933/7,010,640) - 2169 violations - ETA: 529s  
Found 2170 violations so far...
Found 2180 violations so far...
Found 2190 violations so far...
Comparing: 81% (5,694,987/7,010,640) - 2190 violations - ETA: 515s  
Found 2200 violations so far...
Found 2210 violations so far...
Comparing: 81% (5,725,496/7,010,640) - 2216 violations - ETA: 502s  
Comparing: 82% (5,754,426/7,010,640) - 2217 violations - ETA: 491s  
Comparing: 82% (5,785,657/7,010,640) - 2217 violations - ETA: 478s  
Found 2220 violations so far...
Comparing: 83% (5,818,841/7,010,640) - 2223 violations - ETA: 464s  
Found 2230 violations so far...
Found 2240 violations so far...
Found 2250 violations so far...
Found 2260 violations so far...
Found 2270 violations so far...
Found 2280 violations so far...
Comparing: 83% (5,851,926/7,010,640) - 2284 violations - ETA: 451s  
Found 2290 violations so far...
Found 2300 violations so far...
Comparing: 83% (5,883,359/7,010,640) - 2304 violations - ETA: 438s  
Found 2310 violations so far...
Comparing: 84% (5,918,967/7,010,640) - 2317 violations - ETA: 424s  
Found 2320 violations so far...
Comparing: 84% (5,947,210/7,010,640) - 2321 violations - ETA: 413s  
Comparing: 85% (5,968,991/7,010,640) - 2321 violations - ETA: 404s  
Comparing: 85% (5,990,631/7,010,640) - 2322 violations - ETA: 396s  
Found 2330 violations so far...
Comparing: 85% (6,020,394/7,010,640) - 2331 violations - ETA: 384s  
Found 2340 violations so far...
Comparing: 86% (6,054,690/7,010,640) - 2348 violations - ETA: 371s  
Comparing: 86% (6,080,493/7,010,640) - 2348 violations - ETA: 361s  
Found 2350 violations so far...
Comparing: 87% (6,115,875/7,010,640) - 2358 violations - ETA: 346s  
Found 2360 violations so far...
Comparing: 87% (6,149,210/7,010,640) - 2362 violations - ETA: 333s  
Comparing: 88% (6,170,610/7,010,640) - 2362 violations - ETA: 325s  
Comparing: 88% (6,208,885/7,010,640) - 2363 violations - ETA: 309s  
Found 2370 violations so far...
Found 2380 violations so far...
Comparing: 89% (6,241,193/7,010,640) - 2383 violations - ETA: 297s  
Comparing: 89% (6,272,318/7,010,640) - 2383 violations - ETA: 284s  
Comparing: 89% (6,294,924/7,010,640) - 2383 violations - ETA: 276s  
Comparing: 90% (6,314,484/7,010,640) - 2383 violations - ETA: 269s  
Comparing: 90% (6,340,046/7,010,640) - 2383 violations - ETA: 259s  
Comparing: 90% (6,358,621/7,010,640) - 2383 violations - ETA: 252s  
Comparing: 90% (6,371,343/7,010,640) - 2383 violations - ETA: 247s  
Comparing: 91% (6,392,406/7,010,640) - 2383 violations - ETA: 239s  
Comparing: 91% (6,409,653/7,010,640) - 2383 violations - ETA: 233s  
Comparing: 91% (6,439,416/7,010,640) - 2383 violations - ETA: 221s  
Comparing: 92% (6,464,208/7,010,640) - 2384 violations - ETA: 212s  
Comparing: 92% (6,483,969/7,010,640) - 2384 violations - ETA: 204s  
Comparing: 92% (6,509,026/7,010,640) - 2384 violations - ETA: 194s  
Comparing: 93% (6,533,605/7,010,640) - 2384 violations - ETA: 185s  
Comparing: 93% (6,561,487/7,010,640) - 2386 violations - ETA: 174s  
Comparing: 93% (6,584,434/7,010,640) - 2386 violations - ETA: 165s  
Comparing: 94% (6,611,373/7,010,640) - 2386 violations - ETA: 155s  
Comparing: 94% (6,629,646/7,010,640) - 2386 violations - ETA: 148s  
Comparing: 94% (6,654,725/7,010,640) - 2386 violations - ETA: 138s  
Comparing: 95% (6,673,361/7,010,640) - 2386 violations - ETA: 131s  
Comparing: 95% (6,701,293/7,010,640) - 2387 violations - ETA: 120s  
Found 2390 violations so far...
Found 2400 violations so far...
Found 2410 violations so far...
Comparing: 95% (6,727,201/7,010,640) - 2412 violations - ETA: 110s  
Found 2420 violations so far...
Found 2430 violations so far...
Found 2440 violations so far...
Comparing: 96% (6,752,409/7,010,640) - 2449 violations - ETA: 100s  
Found 2450 violations so far...
Comparing: 96% (6,778,175/7,010,640) - 2456 violations - ETA: 90s  
Comparing: 97% (6,801,470/7,010,640) - 2456 violations - ETA: 81s  
Comparing: 97% (6,827,588/7,010,640) - 2457 violations - ETA: 71s  
Comparing: 97% (6,851,218/7,010,640) - 2457 violations - ETA: 62s  
Found 2460 violations so far...
Found 2470 violations so far...
Found 2480 violations so far...
Found 2490 violations so far...
Comparing: 98% (6,874,483/7,010,640) - 2497 violations - ETA: 53s  
Found 2500 violations so far...
Found 2510 violations so far...
Found 2520 violations so far...
Found 2530 violations so far...
Comparing: 98% (6,903,409/7,010,640) - 2530 violations - ETA: 41s  
Found 2540 violations so far...
Comparing: 98% (6,937,411/7,010,640) - 2543 violations - ETA: 28s  
Comparing: 99% (6,962,622/7,010,640) - 2543 violations - ETA: 18s  
Comparing: 99% (6,987,229/7,010,640) - 2544 violations - ETA: 9s  
Complete: 7010640 comparisons, 2544 violations

## keep_classes_small_with_single_responsibility
**repl_session.py** - 1 violation(s)

[!] WARNING (line 22)
Class "REPLSession" is 371 lines - should be under 300 lines (extract related methods into separate classes)

```python


class REPLSession:
    STAGE_MAP = {
        'not_started': 'instructions',
        'instructions_given': 'instructions',
        'submitted': 'submitted'
    }
    
    def __init__(self, bot, workspace_directory: Path):
    # ... (truncated)
```

---

## keep_functions_small_focused
**actions.py** - 2 violation(s)

[!] WARNING (line 15)
Function "__init__" is 24 lines - should be under 20 lines (extract complex logic to helper functions)

```python
class Actions:

    def __init__(self, behavior: 'Behavior'):
        self.behavior = behavior
        actions_list = behavior.actions_workflow
        
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

[!] WARNING (line 116)
Function "navigate_to" is 24 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return self._state_manager.filter_completed_actions_after_target(completed_actions, target_index, self._actions)

    def navigate_to(self, action_name: str, out_of_order: bool=False):
        action = self.find_by_name(action_name)
        if action is None:
            raise ValueError(f"Action '{action_name}' not found")
        
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
**rules.py** - 1 violation(s)

[!] WARNING (line 105)
Function "get_last_report_timestamp" is 22 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return rules_instance._rule_filter.filter_files(self.files, self.exclude)

    def get_last_report_timestamp(self) -> float:
        logger = logging.getLogger(__name__)
        docs_path = self.bot_paths.documentation_path
        reports_dir = self.bot_paths.workspace_directory / docs_path / 'reports'
        logger.info(f'Looking for previous reports in: {reports_dir}')
        if not reports_dir.exists():
            logger.info('Reports directory does not exist - returning 0.0')
            return 0.0
        
        report_files = list(reports_dir.glob(f'{self.behavior.name}-validation-status-*.md'))
        logger.info(f'Found {len(report_files)} report files')
        if not report_files:
            logger.info('No report files found - returning 0.0')
            return 0.0
        
        current_time = time.time()
        previous_run_files = [f for f in report_files if (current_time - f.stat().st_mtime) > 10]
        logger.info(f'Found {len(previous_run_files)} previous run files (excluding files < 10 seconds old)')
        
        if not previous_run_files:
            logger.info('No previous run files found - returning 0.0')
            return 0.0
        
        most_recent = max(previous_run_files, key=lambda p: p.stat().st_mtime)
        logger.info(f'Most recent previous report: {most_recent.name} (timestamp: {most_recent.stat().st_mtime})')
        return most_recent.stat().st_mtime

```

---

## keep_functions_small_focused
**state.py** - 1 violation(s)

[!] WARNING (line 42)
Function "execute" is 21 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return True
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        behavior_name = args.strip()
        if not behavior_name:
            return REPLCommandResponse(
                output="ERROR: No behavior specified",
                response="ERROR: No behavior specified",
                status="error"
            )
        
        behavior = self.find_behavior(behavior_name)
        if not behavior:
            return self.error_behavior_not_found(behavior_name)
        
        if not behavior.actions.names:
            return REPLCommandResponse(
                output=f"ERROR: behavior '{behavior_name}' has no actions",
                response=f"ERROR: behavior '{behavior_name}' has no actions",
                status="error"
            )
        
        self.bot.behaviors.navigate_to(behavior_name)
        first_action_name = behavior.actions.names[0]
        behavior.actions.navigate_to(first_action_name)
        return self.execute_instructions()

```

---

## keep_functions_small_focused
**workflow.py** - 1 violation(s)

[!] WARNING (line 83)
Function "execute" is 29 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return "confirm"
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        if not self.has_current_action:
            return self.error_no_current_action("confirm")
        
        behavior = self.current_behavior
        if not behavior:
            return self.error_no_current_behavior()
        
        current_behavior_name = behavior.name
        
        # Check if at last action BEFORE closing
        is_last_action = behavior.actions.next() is None
        
        # Mark current action as complete and advance
        behavior.actions.close_current()
        
        # If not at last action, show next action's instructions
        if not is_last_action:
            return self.execute_instructions()
        
        # At last action - behavior is complete
        # Mark behavior as complete in state file
        self._mark_behavior_complete(current_behavior_name)
        
        # Check for next behavior BEFORE close_current since it advances the index
        next_behavior = self.bot.behaviors.next()
        
        if next_behavior:
            # Advance to next behavior
            self.bot.behaviors.close_current()
            # Navigate to next behavior's first action
            self.bot.behaviors.navigate_to(next_behavior.name)
            if next_behavior.actions.names:
                next_behavior.actions.navigate_to(next_behavior.actions.names[0])
                return self.execute_instructions()
        
        # No more behaviors - all complete
        return REPLCommandResponse(
            output=f"COMPLETE: {current_behavior_name} behavior finished\n\nALL BEHAVIORS COMPLETE!",
            response="COMPLETE: All behaviors finished",
            status="success"
        )
    
```

---

## maintain_vertical_density
**repl_session.py** - 1 violation(s)

[i] INFO (line 244)
Function "_execute_action_with_args" is 71 lines - consider improving vertical density by declaring variables near usage

```python
            return args_str.split()
    
    def _execute_action_with_args(self, action_name: str, cli_args: list, operation: str = None) -> REPLCommandResponse:
        """Execute action with parsed CLI arguments."""
        if not self.has_current_behavior:
            return REPLCommandResponse(
                output="ERROR: No current behavior set. Please select a behavior first.",
                response="ERROR: No current behavior set",
                status="error"
            )
    # ... (truncated)
```

---

## never_swallow_exceptions
**workflow.py** - 1 violation(s)

[X] ERROR (line 138)
Except block only contains pass at line 138 - exceptions must be logged or rethrown, never swallowed

```python
            state_data['completed_behaviors'] = completed
            state_file.write_text(json.dumps(state_data, indent=2))
        except (json.JSONDecodeError, IOError):
            pass

```

---

## place_imports_at_top
**repl_session.py** - 4 violation(s)

[X] ERROR (line 12)
Import statement found after non-import code. Move all imports to the top of the file.

```python
    TTYDetectionResult
)
from agile_bot.bots.base_bot.src.repl_cli.repl_help import REPLHelp
from agile_bot.bots.base_bot.src.repl_cli.repl_status import REPLStatus
```

[X] ERROR (line 13)
Import statement found after non-import code. Move all imports to the top of the file.

```python
)
from agile_bot.bots.base_bot.src.repl_cli.repl_help import REPLHelp
from agile_bot.bots.base_bot.src.repl_cli.repl_status import REPLStatus
from agile_bot.bots.base_bot.src.repl_cli.repl_commands import (
```

[X] ERROR (line 14)
Import statement found after non-import code. Move all imports to the top of the file.

```python
from agile_bot.bots.base_bot.src.repl_cli.repl_help import REPLHelp
from agile_bot.bots.base_bot.src.repl_cli.repl_status import REPLStatus
from agile_bot.bots.base_bot.src.repl_cli.repl_commands import (
    register_commands,
```

[X] ERROR (line 19)
Import statement found after non-import code. Move all imports to the top of the file.

```python
    DotNotationCommand
)
from agile_bot.bots.base_bot.src.actions.action_context import Scope, ScopeType

```

---

## provide_meaningful_context
**cli_parser_generator.py** - 1 violation(s)

[!] WARNING (line 222)
Line 222 uses numbered variable "s1" - use meaningful descriptive name

```python
        import re
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
```

---

## provide_meaningful_context
**cli_parser_generator_visitor.py** - 1 violation(s)

[!] WARNING (line 231)
Line 231 uses numbered variable "s1" - use meaningful descriptive name

```python
        import re
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
```

---

## stop_writing_useless_comments
**orchestrator.py** - 2 violation(s)

[X] ERROR (line 93)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def generate_for_all_actions(self) -> None:
        """Traverse all (behavior, action) pairs - used for code generation."""
        self.visitor.visit_header(self.bot_name)
```

[X] ERROR (line 101)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _visit_behavior_action(self, behavior, action) -> None:
        """Visit a specific behavior-action pair with full object access."""
        context = ActionHelpContext(
```

---

## stop_writing_useless_comments
**repl_session.py** - 8 violation(s)

[X] ERROR (line 237)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _tokenize_cli_args(self, args_str: str) -> list:
        """Tokenize CLI-style arguments, handling quoted strings."""
        import shlex
```

[X] ERROR (line 245)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _execute_action_with_args(self, action_name: str, cli_args: list, operation: str = None) -> REPLCommandResponse:
        """Execute action with parsed CLI arguments."""
        if not self.has_current_behavior:
```

[X] ERROR (line 342)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_parameters(self, args: str) -> Dict[str, Any]:
        """Parse --param value and --param "value with spaces" from command args."""
        params = {}
```

[X] ERROR (line 357)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_scope_from_string(self, scope_str: str) -> Optional[Scope]:
        """Parse scope JSON/dict string into Scope object."""
        if not scope_str:
```

[X] ERROR (line 368)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def get_stored_scope(self) -> Optional[Dict[str, Any]]:
        """Get scope parameters from behavior action state file."""
        state_file = self._get_state_file_path()
```

[X] ERROR (line 379)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def store_scope_parameters(self, scope: Scope) -> None:
        """Store scope parameters in behavior action state file."""
        state_file = self._get_state_file_path()
```

[X] ERROR (line 391)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _get_state_file_path(self) -> Path:
        """Get the path to behavior_action_state.json."""
        return self.workspace_directory / 'behavior_action_state.json'
```

[X] ERROR (line 361)
Useless comment: "# Handle Python-style dict syntax" - delete it or improve the code instead

```python
            return None
        try:
            # Handle Python-style dict syntax
            data = json.loads(scope_str.replace("'", '"'))
```

---

## stop_writing_useless_comments
**dot_notation.py** - 1 violation(s)

[X] ERROR (line 6)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class DotNotationCommand(REPLCommand):
    """Handles dot notation commands like behavior.action or behavior.action.operation."""
    
```

---

## stop_writing_useless_comments
**meta.py** - 1 violation(s)

[X] ERROR (line 6)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class MetaCommand(REPLCommand):
    """Base for meta commands - provides access to help and status resources."""
    
```

---

## stop_writing_useless_comments
**navigation.py** - 2 violation(s)

[X] ERROR (line 6)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class NavigationCommand(REPLCommand):
    """Base for navigation commands - provides navigation-specific state."""
    
```

[X] ERROR (line 83)
Useless comment: "# Get previous action" - delete it or improve the code instead

```python
            return self.error_no_current_behavior()
        
        # Get previous action
        prev_action = behavior.actions.previous()
```

---

## stop_writing_useless_comments
**state.py** - 3 violation(s)

[X] ERROR (line 7)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class StateCommand(REPLCommand):
    """Base for state commands - provides access to behavior/action lookup."""
    
```

[X] ERROR (line 126)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _update_state_file(self, workspace_path: str) -> None:
        """Update behavior_action_state.json with working_directory."""
        state_file = self.session.workspace_directory / 'behavior_action_state.json'
```

[X] ERROR (line 116)
Useless comment: "# Update state file with working_directory" - delete it or improve the code instead

```python
            )
        
        # Update state file with working_directory
        self._update_state_file(workspace_path)
```

---

## stop_writing_useless_comments
**workflow.py** - 2 violation(s)

[X] ERROR (line 8)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class WorkflowCommand(REPLCommand):
    """Base for workflow commands - provides action phase/state properties."""
    
```

[X] ERROR (line 127)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _mark_behavior_complete(self, behavior_name: str) -> None:
        """Add behavior to completed_behaviors in state file."""
        state_file = self.session.workspace_directory / 'behavior_action_state.json'
```

---

## use_clear_function_parameters
**rules.py** - 5 violation(s)

[!] WARNING (line 293)
Function "_process_scanner_result" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
            return data

    def _process_scanner_result(self, rule, rule_result: dict, scanner_results: Any, scanner_path: str, scanner_name: str, logger) -> str:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        execution_status = rule.scanner_execution_status or 'SUCCESS'
    # ... (truncated)
```

[!] WARNING (line 309)
Function "_execute_scanner" has 9 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return f'  [OK] {rule.rule_file}: Scanner executed successfully ({violations_count} violations)'

    def _execute_scanner(self, rule, rule_result: dict, context: ValidationContext, scanner_path: str, logger, files: Dict, changed_files: Dict, all_files: Dict) -> str:
        scanner_name = scanner_path.split('.')[-1] if '.' in scanner_path else scanner_path
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # ... (truncated)
```

[!] WARNING (line 329)
Function "_process_rule" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
            raise

    def _process_rule(self, rule, rule_result: dict, context: ValidationContext, logger, files: Dict, changed_files: Dict, all_files: Dict) -> str:
        scanner_path = rule.scanner_path
        if not scanner_path:
    # ... (truncated)
```

[!] WARNING (line 341)
Function "validate" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return self._execute_scanner(rule, rule_result, context, scanner_path, logger, files, changed_files, all_files)

    def validate(self, context: ValidationContext, files: Optional[Dict[str, List[Path]]]=None, callbacks: Optional[ValidationCallbacks]=None, skiprule: Optional[List[str]]=None, exclude: Optional[List[str]]=None) -> List[Dict[str, Any]]:
        if isinstance(context, ValidationContext):
            return self._execute_validation(context)
    # ... (truncated)
```

[!] WARNING (line 346)
Function "_create_legacy_context" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return self._execute_validation(self._create_legacy_context(context, files, callbacks, skiprule, exclude))

    def _create_legacy_context(self, knowledge_graph: Dict, files: Optional[Dict], callbacks: Optional[ValidationCallbacks], skiprule: Optional[List[str]], exclude: Optional[List[str]]) -> ValidationContext:
        return ValidationContext(knowledge_graph=knowledge_graph, files=files or {}, callbacks=callbacks or ValidationCallbacks(), skiprule=skiprule or [], exclude=exclude or [], skip_cross_file=True, all_files=False, behavior=self.behavior, bot_paths=getattr(self, 'bot_paths', None), working_dir=Path.cwd())

```

---

## use_domain_language
**actions.py** - 2 violation(s)

[i] INFO (line 97)
Function "previous" doesn't match domain terms. Use domain-specific language from specification: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 103)
Function "__iter__" doesn't match domain terms. Use domain-specific language from specification: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

---

## use_domain_language
**cli_parser_generator.py** - 5 violation(s)

[i] INFO (line 44)
Function "_add_header" doesn't match domain terms. Use domain-specific language from specification: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 124)
Function "_add_bool_argument" doesn't match domain terms. Use domain-specific language from specification: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 131)
Function "_add_optional_bool_argument" doesn't match domain terms. Use domain-specific language from specification: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 142)
Function "_add_dict_argument" doesn't match domain terms. Use domain-specific language from specification: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[!] WARNING (line 226)
Function "generate_parsers_for_story_bot" uses generate/calculate. Use property instead (e.g., "recommended_trades" not "generate_recommendation").

---

## use_domain_language
**cli_parser_generator_visitor.py** - 4 violation(s)

[i] INFO (line 59)
Function "_add_header" doesn't match domain terms. Use domain-specific language from specification: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 138)
Function "_add_bool_argument" doesn't match domain terms. Use domain-specific language from specification: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 145)
Function "_add_optional_bool_argument" doesn't match domain terms. Use domain-specific language from specification: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 156)
Function "_add_dict_argument" doesn't match domain terms. Use domain-specific language from specification: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

---

## use_domain_language
**orchestrator.py** - 1 violation(s)

[!] WARNING (line 92)
Function "generate_for_all_actions" uses generate/calculate. Use property instead (e.g., "recommended_trades" not "generate_recommendation").

---

## use_domain_language
**repl_session.py** - 5 violation(s)

[i] INFO (line 132)
Function "display_current_state" uses parameter name "full" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 187)
Function "_handle_action_shortcut" uses parameter name "args_str" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 236)
Function "_tokenize_cli_args" uses parameter name "args_str" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 244)
Function "_execute_action_with_args" uses parameter name "cli_args" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 341)
Function "parse_command_parameters" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

---

## use_domain_language
**rules.py** - 11 violation(s)

[i] INFO (line 38)
Function "from_action_context" uses parameter name "cls" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 66)
Function "from_parameters" uses parameter name "cls" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 190)
Function "__iter__" doesn't match domain terms. Use domain-specific language from specification: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 195)
Function "__len__" doesn't match domain terms. Use domain-specific language from specification: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 279)
Function "_flush_logger_handlers" uses parameter name "logger" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 293)
Function "_process_scanner_result" uses parameter name "logger" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 309)
Function "_execute_scanner" uses parameter name "logger" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 329)
Function "_process_rule" uses parameter name "logger" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 355)
Function "_log_validation_start" uses parameter name "logger" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 370)
Function "_process_all_rules" uses parameter name "logger" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 396)
Function "_log_scanner_status_summary" uses parameter name "logger" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

---

## use_domain_language
**dot_notation.py** - 1 violation(s)

[i] INFO (line 14)
Function "execute" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

---

## use_domain_language
**meta.py** - 6 violation(s)

[i] INFO (line 23)
Function "takes_args" doesn't match domain terms. Use domain-specific language from specification: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 26)
Function "execute" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 51)
Function "execute" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 65)
Function "execute" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 79)
Function "execute" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 122)
Function "execute" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

---

## use_domain_language
**navigation.py** - 3 violation(s)

[i] INFO (line 31)
Function "execute" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 75)
Function "execute" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 114)
Function "execute" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

---

## use_domain_language
**repl_command.py** - 2 violation(s)

[i] INFO (line 16)
Function "takes_args" doesn't match domain terms. Use domain-specific language from specification: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 20)
Function "execute" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

---

## use_domain_language
**state.py** - 8 violation(s)

[i] INFO (line 39)
Function "takes_args" doesn't match domain terms. Use domain-specific language from specification: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 42)
Function "execute" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 74)
Function "takes_args" doesn't match domain terms. Use domain-specific language from specification: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 77)
Function "execute" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 104)
Function "takes_args" doesn't match domain terms. Use domain-specific language from specification: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 107)
Function "execute" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 143)
Function "takes_args" doesn't match domain terms. Use domain-specific language from specification: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 146)
Function "execute" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

---

## use_domain_language
**workflow.py** - 3 violation(s)

[i] INFO (line 49)
Function "execute" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 60)
Function "execute" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 83)
Function "execute" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

---

Completed: 2025-12-24 00:31:55
Total violations: 98
Scanners executed: 30
