# Validation Status - code
Started: 2025-12-24 01:47:58
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
**action_context.py** - 1 violation(s)

[!] WARNING (line 32)
Line 32: Variable truthiness check detected (if not data:). Assume variable exists - let code fail fast if missing.

```python
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Scope':
        if not data:
            return cls()
        
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


## Cross-File Duplication Analysis
Scanning 258 files...
Extracted 3745 code blocks
Starting 7010640 pairwise comparisons...
Comparing: 0% (33,540/7,010,640) - 0 violations - ETA: 2080s  
Comparing: 0% (56,412/7,010,640) - 0 violations - ETA: 2465s  
Comparing: 1% (81,045/7,010,640) - 0 violations - ETA: 2565s  
Comparing: 1% (102,313/7,010,640) - 0 violations - ETA: 2701s  
Comparing: 1% (120,580/7,010,640) - 0 violations - ETA: 2857s  
Comparing: 2% (144,921/7,010,640) - 0 violations - ETA: 2842s  
Comparing: 2% (163,282/7,010,640) - 0 violations - ETA: 2935s  
Comparing: 2% (182,422/7,010,640) - 2 violations - ETA: 2994s  
Comparing: 3% (211,528/7,010,640) - 2 violations - ETA: 2893s  
Comparing: 3% (224,964/7,010,640) - 2 violations - ETA: 3016s  
Comparing: 3% (238,285/7,010,640) - 2 violations - ETA: 3126s  
Comparing: 3% (249,703/7,010,640) - 2 violations - ETA: 3249s  
Comparing: 3% (260,480/7,010,640) - 2 violations - ETA: 3369s  
Comparing: 4% (281,619/7,010,640) - 2 violations - ETA: 3345s  
Comparing: 4% (311,894/7,010,640) - 2 violations - ETA: 3221s  
Comparing: 4% (337,765/7,010,640) - 2 violations - ETA: 3161s  
Comparing: 5% (360,154/7,010,640) - 2 violations - ETA: 3139s  
Comparing: 5% (379,250/7,010,640) - 2 violations - ETA: 3147s  
Comparing: 5% (408,067/7,010,640) - 2 violations - ETA: 3074s  
Comparing: 6% (428,314/7,010,640) - 2 violations - ETA: 3073s  
Comparing: 6% (441,291/7,010,640) - 2 violations - ETA: 3126s  
Comparing: 6% (458,239/7,010,640) - 2 violations - ETA: 3145s  
Comparing: 6% (472,959/7,010,640) - 2 violations - ETA: 3179s  
Comparing: 7% (497,225/7,010,640) - 2 violations - ETA: 3144s  
Comparing: 7% (516,940/7,010,640) - 2 violations - ETA: 3140s  
Comparing: 7% (545,241/7,010,640) - 2 violations - ETA: 3083s  
Comparing: 8% (574,618/7,010,640) - 2 violations - ETA: 3024s  
Comparing: 8% (606,445/7,010,640) - 2 violations - ETA: 2957s  
Comparing: 9% (634,758/7,010,640) - 2 violations - ETA: 2913s  
Comparing: 9% (650,332/7,010,640) - 2 violations - ETA: 2934s  
Comparing: 9% (662,711/7,010,640) - 2 violations - ETA: 2969s  
Comparing: 10% (702,827/7,010,640) - 2 violations - ETA: 2872s  
Comparing: 10% (741,673/7,010,640) - 2 violations - ETA: 2789s  
Comparing: 11% (774,347/7,010,640) - 2 violations - ETA: 2738s  
Comparing: 11% (801,983/7,010,640) - 2 violations - ETA: 2709s  
Comparing: 11% (827,065/7,010,640) - 2 violations - ETA: 2691s  
Comparing: 12% (850,146/7,010,640) - 2 violations - ETA: 2681s  
Comparing: 12% (869,375/7,010,640) - 2 violations - ETA: 2684s  
Found 10 violations so far...
Comparing: 12% (891,920/7,010,640) - 16 violations - ETA: 2675s  
Found 20 violations so far...
Found 30 violations so far...
Comparing: 13% (920,058/7,010,640) - 30 violations - ETA: 2648s  
Comparing: 13% (950,177/7,010,640) - 30 violations - ETA: 2615s  
Comparing: 14% (983,776/7,010,640) - 30 violations - ETA: 2573s  
Comparing: 14% (1,018,015/7,010,640) - 30 violations - ETA: 2531s  
Comparing: 14% (1,039,062/7,010,640) - 30 violations - ETA: 2528s  
Comparing: 15% (1,054,638/7,010,640) - 30 violations - ETA: 2541s  
Found 40 violations so far...
Found 50 violations so far...
Comparing: 15% (1,081,656/7,010,640) - 59 violations - ETA: 2521s  
Found 60 violations so far...
Comparing: 15% (1,113,015/7,010,640) - 61 violations - ETA: 2490s  
Comparing: 16% (1,142,491/7,010,640) - 61 violations - ETA: 2465s  
Comparing: 16% (1,174,620/7,010,640) - 61 violations - ETA: 2434s  
Comparing: 17% (1,196,592/7,010,640) - 61 violations - ETA: 2429s  
Comparing: 17% (1,221,847/7,010,640) - 61 violations - ETA: 2416s  
Comparing: 17% (1,249,521/7,010,640) - 61 violations - ETA: 2397s  
Comparing: 18% (1,271,198/7,010,640) - 61 violations - ETA: 2393s  
Comparing: 18% (1,289,172/7,010,640) - 61 violations - ETA: 2396s  
Comparing: 18% (1,304,598/7,010,640) - 61 violations - ETA: 2405s  
Comparing: 18% (1,328,158/7,010,640) - 61 violations - ETA: 2396s  
Comparing: 19% (1,346,504/7,010,640) - 61 violations - ETA: 2397s  
Comparing: 19% (1,369,867/7,010,640) - 61 violations - ETA: 2388s  
Comparing: 19% (1,399,181/7,010,640) - 61 violations - ETA: 2366s  
Comparing: 20% (1,427,971/7,010,640) - 61 violations - ETA: 2345s  
Found 70 violations so far...
Comparing: 20% (1,456,615/7,010,640) - 71 violations - ETA: 2326s  
Found 80 violations so far...
Comparing: 21% (1,485,988/7,010,640) - 80 violations - ETA: 2305s  
Comparing: 21% (1,525,574/7,010,640) - 80 violations - ETA: 2265s  
Comparing: 22% (1,575,574/7,010,640) - 80 violations - ETA: 2207s  
Comparing: 23% (1,618,651/7,010,640) - 80 violations - ETA: 2164s  
Comparing: 23% (1,648,308/7,010,640) - 82 violations - ETA: 2146s  
Comparing: 23% (1,676,304/7,010,640) - 89 violations - ETA: 2131s  
Comparing: 24% (1,705,165/7,010,640) - 89 violations - ETA: 2115s  
Comparing: 24% (1,727,142/7,010,640) - 89 violations - ETA: 2110s  
Comparing: 24% (1,747,020/7,010,640) - 89 violations - ETA: 2108s  
Comparing: 25% (1,769,814/7,010,640) - 89 violations - ETA: 2101s  
Comparing: 25% (1,788,475/7,010,640) - 89 violations - ETA: 2101s  
Comparing: 25% (1,813,182/7,010,640) - 89 violations - ETA: 2092s  
Found 90 violations so far...
Comparing: 26% (1,842,586/7,010,640) - 90 violations - ETA: 2075s  
Comparing: 26% (1,878,838/7,010,640) - 92 violations - ETA: 2048s  
Comparing: 27% (1,904,865/7,010,640) - 92 violations - ETA: 2036s  
Comparing: 27% (1,937,061/7,010,640) - 94 violations - ETA: 2016s  
Comparing: 27% (1,962,477/7,010,640) - 94 violations - ETA: 2006s  
Comparing: 28% (1,981,011/7,010,640) - 94 violations - ETA: 2005s  
Comparing: 28% (1,997,785/7,010,640) - 94 violations - ETA: 2006s  
Comparing: 28% (2,014,503/7,010,640) - 94 violations - ETA: 2008s  
Comparing: 28% (2,028,783/7,010,640) - 94 violations - ETA: 2013s  
Comparing: 29% (2,041,156/7,010,640) - 94 violations - ETA: 2020s  
Comparing: 29% (2,052,507/7,010,640) - 94 violations - ETA: 2028s  
Comparing: 29% (2,063,550/7,010,640) - 94 violations - ETA: 2037s  
Comparing: 29% (2,083,995/7,010,640) - 94 violations - ETA: 2032s  
Comparing: 30% (2,111,694/7,010,640) - 94 violations - ETA: 2017s  
Comparing: 30% (2,133,649/7,010,640) - 94 violations - ETA: 2011s  
Comparing: 30% (2,162,484/7,010,640) - 94 violations - ETA: 1994s  
Comparing: 31% (2,197,169/7,010,640) - 95 violations - ETA: 1971s  
Comparing: 31% (2,229,437/7,010,640) - 95 violations - ETA: 1951s  
Comparing: 32% (2,256,779/7,010,640) - 95 violations - ETA: 1937s  
Comparing: 32% (2,280,519/7,010,640) - 95 violations - ETA: 1928s  
Comparing: 32% (2,301,357/7,010,640) - 95 violations - ETA: 1923s  
Comparing: 33% (2,332,858/7,010,640) - 96 violations - ETA: 1904s  
Found 100 violations so far...
Comparing: 33% (2,359,631/7,010,640) - 109 violations - ETA: 1891s  
Found 110 violations so far...
Comparing: 34% (2,385,261/7,010,640) - 114 violations - ETA: 1880s  
Comparing: 34% (2,408,810/7,010,640) - 115 violations - ETA: 1871s  
Comparing: 34% (2,432,807/7,010,640) - 119 violations - ETA: 1862s  
Found 120 violations so far...
Comparing: 35% (2,457,311/7,010,640) - 121 violations - ETA: 1852s  
Comparing: 35% (2,486,792/7,010,640) - 121 violations - ETA: 1837s  
Comparing: 35% (2,513,144/7,010,640) - 121 violations - ETA: 1825s  
Comparing: 36% (2,531,398/7,010,640) - 123 violations - ETA: 1822s  
Comparing: 36% (2,537,112/7,010,640) - 123 violations - ETA: 1833s  
Comparing: 36% (2,542,801/7,010,640) - 123 violations - ETA: 1844s  
Comparing: 36% (2,548,392/7,010,640) - 123 violations - ETA: 1855s  
Comparing: 36% (2,553,901/7,010,640) - 123 violations - ETA: 1866s  
Comparing: 36% (2,559,144/7,010,640) - 123 violations - ETA: 1878s  
Found 130 violations so far...
Comparing: 36% (2,578,616/7,010,640) - 136 violations - ETA: 1873s  
Found 140 violations so far...
Comparing: 37% (2,602,492/7,010,640) - 148 violations - ETA: 1862s  
Found 150 violations so far...
Found 160 violations so far...
Comparing: 37% (2,633,448/7,010,640) - 167 violations - ETA: 1844s  
Found 170 violations so far...
Found 180 violations so far...
Found 190 violations so far...
Found 200 violations so far...
Comparing: 38% (2,679,828/7,010,640) - 207 violations - ETA: 1809s  
Found 210 violations so far...
Found 220 violations so far...
Found 230 violations so far...
Found 240 violations so far...
Found 250 violations so far...
Found 260 violations so far...
Comparing: 38% (2,713,781/7,010,640) - 260 violations - ETA: 1788s  
Found 270 violations so far...
Found 280 violations so far...
Found 290 violations so far...
Found 300 violations so far...
Found 310 violations so far...
Found 320 violations so far...
Comparing: 39% (2,744,138/7,010,640) - 322 violations - ETA: 1772s  
Found 330 violations so far...
Found 340 violations so far...
Found 350 violations so far...
Found 360 violations so far...
Comparing: 39% (2,770,671/7,010,640) - 368 violations - ETA: 1759s  
Found 370 violations so far...
Found 380 violations so far...
Found 390 violations so far...
Found 400 violations so far...
Comparing: 40% (2,809,206/7,010,640) - 405 violations - ETA: 1734s  
Comparing: 40% (2,839,233/7,010,640) - 409 violations - ETA: 1718s  
Comparing: 40% (2,861,419/7,010,640) - 409 violations - ETA: 1710s  
Comparing: 41% (2,906,341/7,010,640) - 409 violations - ETA: 1680s  
Found 410 violations so far...
Found 420 violations so far...
Comparing: 42% (2,947,755/7,010,640) - 426 violations - ETA: 1653s  
Found 430 violations so far...
Found 440 violations so far...
Found 450 violations so far...
Found 460 violations so far...
Comparing: 42% (2,980,384/7,010,640) - 463 violations - ETA: 1636s  
Found 470 violations so far...
Found 480 violations so far...
Found 490 violations so far...
Found 500 violations so far...
Found 510 violations so far...
Comparing: 42% (3,005,670/7,010,640) - 518 violations - ETA: 1625s  
Found 520 violations so far...
Found 530 violations so far...
Found 540 violations so far...
Found 550 violations so far...
Comparing: 43% (3,030,434/7,010,640) - 558 violations - ETA: 1615s  
Comparing: 43% (3,057,531/7,010,640) - 558 violations - ETA: 1603s  
Found 560 violations so far...
Comparing: 44% (3,093,068/7,010,640) - 560 violations - ETA: 1583s  
Comparing: 44% (3,117,420/7,010,640) - 560 violations - ETA: 1573s  
Comparing: 44% (3,142,628/7,010,640) - 561 violations - ETA: 1562s  
Comparing: 45% (3,170,231/7,010,640) - 562 violations - ETA: 1550s  
Comparing: 45% (3,206,947/7,010,640) - 569 violations - ETA: 1529s  
Comparing: 46% (3,234,984/7,010,640) - 569 violations - ETA: 1517s  
Comparing: 46% (3,257,678/7,010,640) - 569 violations - ETA: 1509s  
Found 570 violations so far...
Comparing: 46% (3,284,257/7,010,640) - 578 violations - ETA: 1497s  
Comparing: 47% (3,309,228/7,010,640) - 579 violations - ETA: 1487s  
Comparing: 47% (3,330,421/7,010,640) - 579 violations - ETA: 1480s  
Comparing: 47% (3,343,211/7,010,640) - 579 violations - ETA: 1480s  
Comparing: 47% (3,359,609/7,010,640) - 579 violations - ETA: 1477s  
Comparing: 48% (3,384,026/7,010,640) - 579 violations - ETA: 1468s  
Comparing: 48% (3,403,875/7,010,640) - 579 violations - ETA: 1462s  
Comparing: 48% (3,421,530/7,010,640) - 579 violations - ETA: 1457s  
Comparing: 49% (3,437,211/7,010,640) - 579 violations - ETA: 1455s  
Comparing: 49% (3,452,803/7,010,640) - 579 violations - ETA: 1452s  
Comparing: 49% (3,466,526/7,010,640) - 579 violations - ETA: 1451s  
Comparing: 49% (3,480,153/7,010,640) - 579 violations - ETA: 1450s  
Comparing: 49% (3,492,166/7,010,640) - 579 violations - ETA: 1450s  
Comparing: 49% (3,505,168/7,010,640) - 579 violations - ETA: 1450s  
Comparing: 50% (3,530,245/7,010,640) - 579 violations - ETA: 1439s  
Found 580 violations so far...
Comparing: 50% (3,551,727/7,010,640) - 580 violations - ETA: 1431s  
Comparing: 51% (3,590,458/7,010,640) - 580 violations - ETA: 1409s  
Comparing: 51% (3,621,112/7,010,640) - 580 violations - ETA: 1394s  
Comparing: 52% (3,661,454/7,010,640) - 580 violations - ETA: 1371s  
Comparing: 52% (3,703,284/7,010,640) - 580 violations - ETA: 1348s  
Comparing: 53% (3,737,963/7,010,640) - 580 violations - ETA: 1330s  
Comparing: 53% (3,767,335/7,010,640) - 580 violations - ETA: 1317s  
Comparing: 54% (3,788,032/7,010,640) - 580 violations - ETA: 1310s  
Comparing: 54% (3,810,554/7,010,640) - 580 violations - ETA: 1301s  
Comparing: 54% (3,838,437/7,010,640) - 580 violations - ETA: 1289s  
Comparing: 55% (3,861,293/7,010,640) - 580 violations - ETA: 1280s  
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
Found 690 violations so far...
Comparing: 55% (3,896,123/7,010,640) - 695 violations - ETA: 1262s  
Found 700 violations so far...
Found 710 violations so far...
Found 720 violations so far...
Found 730 violations so far...
Found 740 violations so far...
Comparing: 56% (3,927,245/7,010,640) - 743 violations - ETA: 1248s  
Found 750 violations so far...
Found 760 violations so far...
Comparing: 56% (3,951,752/7,010,640) - 764 violations - ETA: 1238s  
Found 770 violations so far...
Found 780 violations so far...
Found 790 violations so far...
Found 800 violations so far...
Found 810 violations so far...
Comparing: 56% (3,983,908/7,010,640) - 818 violations - ETA: 1223s  
Comparing: 57% (4,018,620/7,010,640) - 818 violations - ETA: 1206s  
Comparing: 57% (4,042,073/7,010,640) - 819 violations - ETA: 1197s  
Comparing: 57% (4,065,350/7,010,640) - 819 violations - ETA: 1188s  
Comparing: 58% (4,086,242/7,010,640) - 819 violations - ETA: 1180s  
Comparing: 58% (4,104,826/7,010,640) - 819 violations - ETA: 1175s  
Comparing: 58% (4,121,811/7,010,640) - 819 violations - ETA: 1170s  
Comparing: 59% (4,137,440/7,010,640) - 819 violations - ETA: 1166s  
Comparing: 59% (4,158,192/7,010,640) - 819 violations - ETA: 1159s  
Found 820 violations so far...
Found 830 violations so far...
Found 840 violations so far...
Found 850 violations so far...
Found 860 violations so far...
Comparing: 59% (4,188,129/7,010,640) - 860 violations - ETA: 1145s  
Found 870 violations so far...
Found 880 violations so far...
Comparing: 60% (4,223,344/7,010,640) - 889 violations - ETA: 1128s  
Found 890 violations so far...
Comparing: 60% (4,253,257/7,010,640) - 899 violations - ETA: 1115s  
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
Comparing: 61% (4,290,059/7,010,640) - 990 violations - ETA: 1097s  
Comparing: 61% (4,319,153/7,010,640) - 993 violations - ETA: 1084s  
Comparing: 62% (4,347,118/7,010,640) - 994 violations - ETA: 1072s  
Found 1000 violations so far...
Found 1010 violations so far...
Comparing: 62% (4,379,319/7,010,640) - 1018 violations - ETA: 1057s  
Found 1020 violations so far...
Comparing: 62% (4,398,461/7,010,640) - 1021 violations - ETA: 1051s  
Found 1030 violations so far...
Found 1040 violations so far...
Found 1050 violations so far...
Found 1060 violations so far...
Found 1070 violations so far...
Found 1080 violations so far...
Found 1090 violations so far...
Comparing: 63% (4,435,604/7,010,640) - 1093 violations - ETA: 1033s  
Found 1100 violations so far...
Comparing: 63% (4,466,086/7,010,640) - 1106 violations - ETA: 1019s  
Found 1110 violations so far...
Comparing: 64% (4,498,156/7,010,640) - 1112 violations - ETA: 1005s  
Found 1120 violations so far...
Found 1130 violations so far...
Found 1140 violations so far...
Comparing: 64% (4,535,595/7,010,640) - 1149 violations - ETA: 987s  
Found 1150 violations so far...
Found 1160 violations so far...
Found 1170 violations so far...
Found 1180 violations so far...
Found 1190 violations so far...
Found 1200 violations so far...
Found 1210 violations so far...
Found 1220 violations so far...
Found 1230 violations so far...
Comparing: 65% (4,564,805/7,010,640) - 1234 violations - ETA: 975s  
Comparing: 65% (4,594,031/7,010,640) - 1234 violations - ETA: 962s  
Comparing: 65% (4,624,487/7,010,640) - 1234 violations - ETA: 949s  
Found 1240 violations so far...
Found 1250 violations so far...
Found 1260 violations so far...
Found 1270 violations so far...
Found 1280 violations so far...
Found 1290 violations so far...
Found 1300 violations so far...
Found 1310 violations so far...
Comparing: 66% (4,663,391/7,010,640) - 1315 violations - ETA: 931s  
Comparing: 66% (4,691,690/7,010,640) - 1315 violations - ETA: 919s  
Comparing: 67% (4,713,226/7,010,640) - 1315 violations - ETA: 911s  
Found 1320 violations so far...
Found 1330 violations so far...
Found 1340 violations so far...
Found 1350 violations so far...
Found 1360 violations so far...
Found 1370 violations so far...
Found 1380 violations so far...
Found 1390 violations so far...
Found 1400 violations so far...
Comparing: 67% (4,749,294/7,010,640) - 1404 violations - ETA: 895s  
Found 1410 violations so far...
Found 1420 violations so far...
Found 1430 violations so far...
Found 1440 violations so far...
Found 1450 violations so far...
Found 1460 violations so far...
Found 1470 violations so far...
Comparing: 68% (4,784,490/7,010,640) - 1473 violations - ETA: 879s  
Found 1480 violations so far...
Comparing: 68% (4,815,675/7,010,640) - 1483 violations - ETA: 865s  
Comparing: 69% (4,846,973/7,010,640) - 1486 violations - ETA: 852s  
Comparing: 69% (4,888,635/7,010,640) - 1486 violations - ETA: 833s  
Comparing: 70% (4,921,547/7,010,640) - 1486 violations - ETA: 819s  
Comparing: 70% (4,961,101/7,010,640) - 1486 violations - ETA: 801s  
Comparing: 71% (4,999,333/7,010,640) - 1486 violations - ETA: 784s  
Comparing: 71% (5,032,877/7,010,640) - 1486 violations - ETA: 770s  
Comparing: 72% (5,061,022/7,010,640) - 1486 violations - ETA: 758s  
Comparing: 72% (5,089,383/7,010,640) - 1486 violations - ETA: 747s  
Comparing: 72% (5,113,656/7,010,640) - 1486 violations - ETA: 738s  
Comparing: 73% (5,138,487/7,010,640) - 1486 violations - ETA: 728s  
Comparing: 73% (5,161,413/7,010,640) - 1486 violations - ETA: 720s  
Comparing: 73% (5,180,069/7,010,640) - 1486 violations - ETA: 713s  
Comparing: 74% (5,197,114/7,010,640) - 1486 violations - ETA: 708s  
Comparing: 74% (5,212,942/7,010,640) - 1486 violations - ETA: 703s  
Found 1490 violations so far...
Found 1500 violations so far...
Found 1510 violations so far...
Found 1520 violations so far...
Found 1530 violations so far...
Found 1540 violations so far...
Found 1550 violations so far...
Found 1560 violations so far...
Found 1570 violations so far...
Found 1580 violations so far...
Found 1590 violations so far...
Comparing: 74% (5,243,167/7,010,640) - 1599 violations - ETA: 691s  
Found 1600 violations so far...
Found 1610 violations so far...
Found 1620 violations so far...
Found 1630 violations so far...
Found 1640 violations so far...
Found 1650 violations so far...
Found 1660 violations so far...
Found 1670 violations so far...
Found 1680 violations so far...
Found 1690 violations so far...
Found 1700 violations so far...
Found 1710 violations so far...
Found 1720 violations so far...
Comparing: 75% (5,276,212/7,010,640) - 1720 violations - ETA: 677s  
Found 1730 violations so far...
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
Comparing: 75% (5,310,865/7,010,640) - 1850 violations - ETA: 662s  
Comparing: 76% (5,334,546/7,010,640) - 1854 violations - ETA: 653s  
Found 1860 violations so far...
Found 1870 violations so far...
Found 1880 violations so far...
Comparing: 76% (5,362,795/7,010,640) - 1881 violations - ETA: 642s  
Found 1890 violations so far...
Found 1900 violations so far...
Comparing: 76% (5,386,662/7,010,640) - 1908 violations - ETA: 633s  
Found 1910 violations so far...
Found 1920 violations so far...
Comparing: 77% (5,415,228/7,010,640) - 1925 violations - ETA: 621s  
Comparing: 77% (5,446,772/7,010,640) - 1927 violations - ETA: 608s  
Found 1930 violations so far...
Comparing: 78% (5,487,036/7,010,640) - 1939 violations - ETA: 591s  
Comparing: 78% (5,516,442/7,010,640) - 1939 violations - ETA: 579s  
Comparing: 79% (5,543,177/7,010,640) - 1939 violations - ETA: 569s  
Found 1940 violations so far...
Comparing: 79% (5,571,245/7,010,640) - 1940 violations - ETA: 558s  
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
Found 2060 violations so far...
Found 2070 violations so far...
Comparing: 79% (5,602,271/7,010,640) - 2072 violations - ETA: 545s  
Found 2080 violations so far...
Found 2090 violations so far...
Found 2100 violations so far...
Found 2110 violations so far...
Found 2120 violations so far...
Found 2130 violations so far...
Comparing: 80% (5,632,858/7,010,640) - 2135 violations - ETA: 533s  
Found 2140 violations so far...
Found 2150 violations so far...
Found 2160 violations so far...
Comparing: 80% (5,662,657/7,010,640) - 2169 violations - ETA: 521s  
Found 2170 violations so far...
Found 2180 violations so far...
Found 2190 violations so far...
Comparing: 81% (5,695,968/7,010,640) - 2190 violations - ETA: 507s  
Found 2200 violations so far...
Found 2210 violations so far...
Comparing: 81% (5,726,199/7,010,640) - 2216 violations - ETA: 495s  
Comparing: 82% (5,755,994/7,010,640) - 2217 violations - ETA: 483s  
Comparing: 82% (5,787,522/7,010,640) - 2217 violations - ETA: 471s  
Found 2220 violations so far...
Comparing: 83% (5,820,616/7,010,640) - 2223 violations - ETA: 457s  
Found 2230 violations so far...
Found 2240 violations so far...
Found 2250 violations so far...
Found 2260 violations so far...
Found 2270 violations so far...
Found 2280 violations so far...
Comparing: 83% (5,854,318/7,010,640) - 2288 violations - ETA: 444s  
Found 2290 violations so far...
Found 2300 violations so far...
Comparing: 83% (5,885,697/7,010,640) - 2304 violations - ETA: 431s  
Found 2310 violations so far...
Found 2320 violations so far...
Comparing: 84% (5,922,882/7,010,640) - 2320 violations - ETA: 416s  
Comparing: 84% (5,952,221/7,010,640) - 2321 violations - ETA: 405s  
Comparing: 85% (5,972,429/7,010,640) - 2321 violations - ETA: 398s  
Comparing: 85% (5,994,368/7,010,640) - 2323 violations - ETA: 389s  
Found 2330 violations so far...
Comparing: 85% (6,028,243/7,010,640) - 2335 violations - ETA: 376s  
Found 2340 violations so far...
Comparing: 86% (6,062,301/7,010,640) - 2348 violations - ETA: 362s  
Found 2350 violations so far...
Comparing: 86% (6,092,701/7,010,640) - 2356 violations - ETA: 351s  
Found 2360 violations so far...
Comparing: 87% (6,130,990/7,010,640) - 2362 violations - ETA: 335s  
Comparing: 87% (6,158,096/7,010,640) - 2362 violations - ETA: 325s  
Comparing: 88% (6,181,734/7,010,640) - 2363 violations - ETA: 316s  
Found 2370 violations so far...
Comparing: 88% (6,221,783/7,010,640) - 2371 violations - ETA: 300s  
Found 2380 violations so far...
Comparing: 89% (6,254,973/7,010,640) - 2383 violations - ETA: 287s  
Comparing: 89% (6,283,064/7,010,640) - 2383 violations - ETA: 276s  
Comparing: 89% (6,304,863/7,010,640) - 2383 violations - ETA: 268s  
Comparing: 90% (6,326,122/7,010,640) - 2383 violations - ETA: 260s  
Comparing: 90% (6,349,918/7,010,640) - 2383 violations - ETA: 251s  
Comparing: 90% (6,365,431/7,010,640) - 2383 violations - ETA: 246s  
Comparing: 91% (6,383,230/7,010,640) - 2383 violations - ETA: 239s  
Comparing: 91% (6,401,104/7,010,640) - 2383 violations - ETA: 233s  
Comparing: 91% (6,428,367/7,010,640) - 2383 violations - ETA: 222s  
Comparing: 92% (6,452,350/7,010,640) - 2383 violations - ETA: 213s  
Comparing: 92% (6,475,106/7,010,640) - 2384 violations - ETA: 205s  
Comparing: 92% (6,498,317/7,010,640) - 2384 violations - ETA: 196s  
Comparing: 93% (6,525,854/7,010,640) - 2384 violations - ETA: 185s  
Comparing: 93% (6,550,185/7,010,640) - 2386 violations - ETA: 176s  
Comparing: 93% (6,576,203/7,010,640) - 2386 violations - ETA: 166s  
Comparing: 94% (6,603,311/7,010,640) - 2386 violations - ETA: 156s  
Comparing: 94% (6,623,079/7,010,640) - 2386 violations - ETA: 148s  
Comparing: 94% (6,647,475/7,010,640) - 2386 violations - ETA: 139s  
Comparing: 95% (6,663,882/7,010,640) - 2386 violations - ETA: 133s  
Comparing: 95% (6,691,589/7,010,640) - 2386 violations - ETA: 122s  
Comparing: 95% (6,715,940/7,010,640) - 2387 violations - ETA: 113s  
Found 2390 violations so far...
Found 2400 violations so far...
Found 2410 violations so far...
Found 2420 violations so far...
Found 2430 violations so far...
Comparing: 96% (6,744,830/7,010,640) - 2437 violations - ETA: 102s  
Found 2440 violations so far...
Found 2450 violations so far...
Comparing: 96% (6,766,052/7,010,640) - 2453 violations - ETA: 93s  
Comparing: 96% (6,793,271/7,010,640) - 2456 violations - ETA: 83s  
Comparing: 97% (6,817,853/7,010,640) - 2457 violations - ETA: 74s  
Comparing: 97% (6,842,482/7,010,640) - 2457 violations - ETA: 64s  
Found 2460 violations so far...
Found 2470 violations so far...
Found 2480 violations so far...
Comparing: 97% (6,868,236/7,010,640) - 2480 violations - ETA: 54s  
Found 2490 violations so far...
Found 2500 violations so far...
Found 2510 violations so far...
Found 2520 violations so far...
Found 2530 violations so far...
Comparing: 98% (6,890,079/7,010,640) - 2530 violations - ETA: 46s  
Comparing: 98% (6,928,171/7,010,640) - 2534 violations - ETA: 31s  
Found 2540 violations so far...
Comparing: 99% (6,950,317/7,010,640) - 2543 violations - ETA: 23s  
Comparing: 99% (6,978,834/7,010,640) - 2543 violations - ETA: 12s  
Comparing: 99% (7,006,546/7,010,640) - 2544 violations - ETA: 1s  
Complete: 7010640 comparisons, 2544 violations

## keep_classes_small_with_single_responsibility
**repl_session.py** - 1 violation(s)

[!] WARNING (line 22)
Class "REPLSession" is 382 lines - should be under 300 lines (extract related methods into separate classes)

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
**state.py** - 2 violation(s)

[!] WARNING (line 19)
Function "execute_instructions" is 55 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return behavior.actions.find_by_name(action_name)
    
    def execute_instructions(self) -> REPLCommandResponse:
        """Execute the current action's get_instructions() method."""
        action = self.current_action
        if not action:
            return REPLCommandResponse(
                output="ERROR: No current action",
                response="ERROR: No current action",
                status="error"
            )
        
        try:
            # Call the real action.get_instructions() method
            context = action.context_class()
            result = action.get_instructions(context)
            instructions_dict = result.get('instructions', {})
            
            # Format all instruction components
            output_lines = [
                f"EXECUTING {self.current_behavior_name}.{self.current_action_name}.instructions",
                ""
            ]
            
            # Add base instructions
            base_instructions = instructions_dict.get('base_instructions', [])
            output_lines.extend(base_instructions)
            
            # Add guardrails (questions and evidence) if present
            guardrails = instructions_dict.get('guardrails', {})
            if guardrails:
                output_lines.append("")
                output_lines.append("**GUARDRAILS:**")
                
                required_context = guardrails.get('required_context', {})
                if required_context:
                    # Display key questions
                    key_questions = required_context.get('key_questions', {})
                    if key_questions:
                        output_lines.append("")
                        output_lines.append("**Required Key Questions:**")
                        for question_key, question_text in key_questions.items():
                            output_lines.append(f"- **{question_key}**: {question_text}")
                    
                    # Display evidence requirements
                    evidence = required_context.get('evidence', {})
                    if evidence:
                        output_lines.append("")
                        output_lines.append("**Required Evidence:**")
                        for evidence_key, evidence_desc in evidence.items():
    # ... (truncated)
```

[!] WARNING (line 105)
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
**workflow.py** - 3 violation(s)

[!] WARNING (line 30)
Function "execute_instructions" is 33 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return self.action_phase in ('not_started', 'instructions_given')
    
    def execute_instructions(self) -> REPLCommandResponse:
        """Execute the current action's get_instructions() method."""
        action = self.current_action
        if not action:
            return REPLCommandResponse(
                output="ERROR: No current action",
                response="ERROR: No current action",
                status="error"
            )
        
        try:
            # Call the real action.get_instructions() method
            context = action.context_class()  # Create empty context for now
            result = action.get_instructions(context)
            instructions_dict = result.get('instructions', {})
            base_instructions = instructions_dict.get('base_instructions', [])
            
            # Build output with real instructions
            output_lines = [
                f"EXECUTING {self.current_behavior_name}.{self.current_action_name}.instructions",
                ""
            ]
            output_lines.extend(base_instructions)
            output_lines.append("")
            output_lines.append("Next: Provide your work using 'submit'.")
            
            output = "\n".join(output_lines)
            
            return REPLCommandResponse(
                output=output, 
                response=output, 
                status="success", 
                action=self.current_action_name
            )
        except Exception as e:
            error_msg = f"ERROR executing {self.current_action_name}.get_instructions(): {str(e)}"
            return REPLCommandResponse(
                output=error_msg,
                response=error_msg,
                status="error",
                action=self.current_action_name
            )

```

[!] WARNING (line 90)
Function "execute" is 31 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return "submit"
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        if not self.has_current_action:
            return self.error_no_current_action("submit for")
        
        action = self.current_action
        if not action:
            return REPLCommandResponse(
                output="ERROR: No current action",
                response="ERROR: No current action",
                status="error"
            )
        
        try:
            # Call the real action.submit() method
            context = action.context_class()  # Create empty context for now
            result = action.submit(context)
            
            # Format output
            status = result.get('status', 'unknown')
            message = result.get('message', 'Work submitted')
            
            output = "\n".join([
                f"EXECUTING {self.current_behavior_name}.{self.current_action_name}.submit",
                "",
                f"[{status.upper()}]",
                f"- {message}",
                "",
                "Next: Type 'confirm' to mark complete and advance."
            ])
            
            return REPLCommandResponse(
                output=output, 
                response=output, 
                status="success", 
                action=self.current_action_name
            )
        except Exception as e:
            error_msg = f"ERROR executing {self.current_action_name}.submit(): {str(e)}"
            return REPLCommandResponse(
                output=error_msg,
                response=error_msg,
                status="error",
                action=self.current_action_name
            )

```

[!] WARNING (line 141)
Function "execute" is 47 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return "confirm"
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        if not self.has_current_action:
            return self.error_no_current_action("confirm")
        
        action = self.current_action
        behavior = self.current_behavior
        if not behavior or not action:
            return self.error_no_current_behavior()
        
        current_behavior_name = behavior.name
        current_action_name = action.action_name
        
        try:
            # Call the real action.confirm() method
            context = action.context_class()
            result = action.confirm(context)
            
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
    # ... (truncated)
```

---

## maintain_vertical_density
**repl_session.py** - 1 violation(s)

[i] INFO (line 244)
Function "_execute_action_with_args" is 82 lines - consider improving vertical density by declaring variables near usage

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

## maintain_vertical_density
**state.py** - 1 violation(s)

[i] INFO (line 19)
Function "execute_instructions" is 75 lines - consider improving vertical density by declaring variables near usage

```python
        return behavior.actions.find_by_name(action_name)
    
    def execute_instructions(self) -> REPLCommandResponse:
        """Execute the current action's get_instructions() method."""
        action = self.current_action
        if not action:
            return REPLCommandResponse(
                output="ERROR: No current action",
                response="ERROR: No current action",
                status="error"
    # ... (truncated)
```

---

## maintain_vertical_density
**workflow.py** - 1 violation(s)

[i] INFO (line 141)
Function "execute" is 57 lines - consider improving vertical density by declaring variables near usage

```python
        return "confirm"
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        if not self.has_current_action:
            return self.error_no_current_action("confirm")
        
        action = self.current_action
        behavior = self.current_behavior
        if not behavior or not action:
            return self.error_no_current_behavior()
    # ... (truncated)
```

---

## never_swallow_exceptions
**workflow.py** - 1 violation(s)

[X] ERROR (line 211)
Except block only contains pass at line 211 - exceptions must be logged or rethrown, never swallowed

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

## simplify_control_flow
**type_hint_converter.py** - 1 violation(s)

[!] WARNING (line 4)
Function "to_cli_type" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
    
    @staticmethod
    def to_cli_type(field_type) -> str:
        type_str = str(field_type)
        if 'Dict' in type_str:
            return 'dict'
        elif 'List' in type_str:
            return 'list'
        elif 'bool' in type_str:
            return 'flag'
        elif 'Scope' in type_str:
            return 'dict'
        return 'str'

```

---

## simplify_control_flow
**state.py** - 1 violation(s)

[!] WARNING (line 19)
Function "execute_instructions" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return behavior.actions.find_by_name(action_name)
    
    def execute_instructions(self) -> REPLCommandResponse:
        """Execute the current action's get_instructions() method."""
        action = self.current_action
        if not action:
            return REPLCommandResponse(
                output="ERROR: No current action",
                response="ERROR: No current action",
                status="error"
            )
        
        try:
            # Call the real action.get_instructions() method
            context = action.context_class()
    # ... (truncated)
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

[X] ERROR (line 353)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_parameters(self, args: str) -> Dict[str, Any]:
        """Parse --param value and --param "value with spaces" from command args."""
        params = {}
```

[X] ERROR (line 368)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_scope_from_string(self, scope_str: str) -> Optional[Scope]:
        """Parse scope JSON/dict string into Scope object."""
        if not scope_str:
```

[X] ERROR (line 379)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def get_stored_scope(self) -> Optional[Dict[str, Any]]:
        """Get scope parameters from behavior action state file."""
        state_file = self._get_state_file_path()
```

[X] ERROR (line 390)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def store_scope_parameters(self, scope: Scope) -> None:
        """Store scope parameters in behavior action state file."""
        state_file = self._get_state_file_path()
```

[X] ERROR (line 402)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _get_state_file_path(self) -> Path:
        """Get the path to behavior_action_state.json."""
        return self.workspace_directory / 'behavior_action_state.json'
```

[X] ERROR (line 372)
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
**meta.py** - 2 violation(s)

[X] ERROR (line 6)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class MetaCommand(REPLCommand):
    """Base for meta commands - provides access to help and status resources."""
    
```

[X] ERROR (line 91)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _execute_instructions(self) -> REPLCommandResponse:
        """Execute the current action's get_instructions() method."""
        action = self.current_action
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
**state.py** - 4 violation(s)

[X] ERROR (line 7)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class StateCommand(REPLCommand):
    """Base for state commands - provides access to behavior/action lookup."""
    
```

[X] ERROR (line 20)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def execute_instructions(self) -> REPLCommandResponse:
        """Execute the current action's get_instructions() method."""
        action = self.current_action
```

[X] ERROR (line 189)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _update_state_file(self, workspace_path: str) -> None:
        """Update behavior_action_state.json with working_directory."""
        state_file = self.session.workspace_directory / 'behavior_action_state.json'
```

[X] ERROR (line 179)
Useless comment: "# Update state file with working_directory" - delete it or improve the code instead

```python
            )
        
        # Update state file with working_directory
        self._update_state_file(workspace_path)
```

---

## stop_writing_useless_comments
**workflow.py** - 3 violation(s)

[X] ERROR (line 8)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class WorkflowCommand(REPLCommand):
    """Base for workflow commands - provides action phase/state properties."""
    
```

[X] ERROR (line 31)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def execute_instructions(self) -> REPLCommandResponse:
        """Execute the current action's get_instructions() method."""
        action = self.current_action
```

[X] ERROR (line 200)
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
**action_context.py** - 1 violation(s)

[i] INFO (line 31)
Function "from_dict" uses parameter name "cls" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

---

## use_domain_language
**cli_context_builder.py** - 1 violation(s)

[i] INFO (line 24)
Function "build_context" uses parameter name "cli_args" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

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

[i] INFO (line 352)
Function "parse_command_parameters" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

---

## use_domain_language
**build_scope.py** - 1 violation(s)

[i] INFO (line 16)
Function "from_context" uses parameter name "cls" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

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

[i] INFO (line 152)
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
**state.py** - 8 violation(s)

[i] INFO (line 102)
Function "takes_args" doesn't match domain terms. Use domain-specific language from specification: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 105)
Function "execute" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 137)
Function "takes_args" doesn't match domain terms. Use domain-specific language from specification: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 140)
Function "execute" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 167)
Function "takes_args" doesn't match domain terms. Use domain-specific language from specification: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 170)
Function "execute" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 206)
Function "takes_args" doesn't match domain terms. Use domain-specific language from specification: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 209)
Function "execute" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

---

## use_domain_language
**workflow.py** - 3 violation(s)

[i] INFO (line 79)
Function "execute" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 90)
Function "execute" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

[i] INFO (line 141)
Function "execute" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, action confirmation, action data collector, action executor, action help context, action instructions, action_confirmation, action_data_collector, action_executor, action_help_context...

---

Completed: 2025-12-24 02:32:58
Total violations: 108
Scanners executed: 30
