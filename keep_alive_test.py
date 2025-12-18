#!/usr/bin/env python3
"""Simple keep-alive test - prints 'continue' every 5 seconds"""
import time
from datetime import datetime

print(f"[{datetime.now()}] Starting keep-alive test - printing 'continue' every 5 seconds")
print(f"[{datetime.now()}] Press Ctrl+C to stop\n")

iteration = 0
try:
    while True:
        iteration += 1
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Iteration {iteration}: continue")
        time.sleep(5)
except KeyboardInterrupt:
    print(f"\n[{datetime.now()}] Stopped after {iteration} iterations")















