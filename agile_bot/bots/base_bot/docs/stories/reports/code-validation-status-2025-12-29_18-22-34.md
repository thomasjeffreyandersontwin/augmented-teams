# Validation Status - code
Started: 2025-12-29 18:22:34
Files: 275


## Cross-File Duplication Analysis
Scanning 4 changed file(s) against 275 total files...
Extracted 179 changed blocks, 4205 reference blocks
Starting 752,695 pairwise comparisons...
Comparing: 3% (27,115/752,695) - 0 violations - ETA: 267s  
Comparing: 6% (48,507/752,695) - 0 violations - ETA: 290s  
Comparing: 8% (66,146/752,695) - 0 violations - ETA: 311s  
Comparing: 10% (80,472/752,695) - 0 violations - ETA: 334s  
Comparing: 13% (103,422/752,695) - 0 violations - ETA: 313s  
Comparing: 16% (122,940/752,695) - 0 violations - ETA: 307s  
Comparing: 19% (143,184/752,695) - 0 violations - ETA: 298s  
Comparing: 22% (169,674/752,695) - 0 violations - ETA: 274s  
Comparing: 25% (189,467/752,695) - 0 violations - ETA: 267s  
Comparing: 27% (203,536/752,695) - 0 violations - ETA: 269s  
Comparing: 29% (223,733/752,695) - 0 violations - ETA: 260s  
Comparing: 31% (238,673/752,695) - 0 violations - ETA: 258s  
Comparing: 33% (252,429/752,695) - 0 violations - ETA: 257s  
Comparing: 35% (269,263/752,695) - 0 violations - ETA: 251s  
Comparing: 37% (281,900/752,695) - 0 violations - ETA: 250s  
Comparing: 38% (293,072/752,695) - 0 violations - ETA: 250s  
Comparing: 40% (307,519/752,695) - 0 violations - ETA: 246s  
Comparing: 42% (319,329/752,695) - 0 violations - ETA: 244s  
Comparing: 43% (330,502/752,695) - 0 violations - ETA: 242s  
Comparing: 45% (342,832/752,695) - 0 violations - ETA: 239s  
Comparing: 46% (353,250/752,695) - 0 violations - ETA: 237s  
Comparing: 48% (362,859/752,695) - 0 violations - ETA: 236s  
Comparing: 49% (373,656/752,695) - 0 violations - ETA: 233s  
Comparing: 50% (383,626/752,695) - 0 violations - ETA: 230s  
Comparing: 52% (393,026/752,695) - 0 violations - ETA: 228s  
Comparing: 55% (416,806/752,695) - 0 violations - ETA: 209s  
Comparing: 59% (444,149/752,695) - 0 violations - ETA: 187s  
Comparing: 61% (464,809/752,695) - 0 violations - ETA: 173s  
Comparing: 64% (483,030/752,695) - 0 violations - ETA: 161s  
Comparing: 68% (513,152/752,695) - 0 violations - ETA: 140s  
Comparing: 71% (541,897/752,695) - 0 violations - ETA: 120s  
Comparing: 75% (570,709/752,695) - 0 violations - ETA: 102s  
Comparing: 79% (599,358/752,695) - 0 violations - ETA: 84s  
Comparing: 83% (631,979/752,695) - 0 violations - ETA: 64s  
Comparing: 87% (656,125/752,695) - 0 violations - ETA: 51s  
Comparing: 90% (678,545/752,695) - 0 violations - ETA: 39s  
Comparing: 93% (706,355/752,695) - 0 violations - ETA: 24s  
Comparing: 98% (737,642/752,695) - 0 violations - ETA: 7s  
Complete: 740230 comparisons, 0 violations

## keep_functions_small_focused
**cursor_api.py** - 2 violation(s)

[!] WARNING (line 39)
Function "starts_session" is 28 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return self._session_id
    
    def starts_session(self, instructions: str) -> APIResponse:
        headers = self._builds_headers()
        payload = {
            'instructions': instructions,
            'mode': 'headless'
        }
        
        try:
            response = requests.post(
                f'{self.base_url}/sessions',
                headers=headers,
                json=payload,
                timeout=30
            )
            
            if response.status_code == 401:
                raise NonRecoverableError('Invalid API key - authentication failed')
            
            if response.status_code == 429:
                raise RecoverableError('Rate limited - please retry')
            
            if response.status_code >= 500:
                raise RecoverableError(f'Server error: {response.status_code}')
            
            response.raise_for_status()
            data = response.json()
            
            self._session_id = data.get('session_id')
            return APIResponse(
                status='running',
                message='Session started',
                session_id=self._session_id,
                progress=data.get('progress', '')
            )
            
        except requests.exceptions.ConnectionError as e:
            raise RecoverableError(f'Connection failed: {e}')
        except requests.exceptions.Timeout as e:
            raise RecoverableError(f'Request timed out: {e}')
    
```

[!] WARNING (line 79)
Function "sends_instruction" is 22 lines - should be under 20 lines (extract complex logic to helper functions)

```python
            raise RecoverableError(f'Request timed out: {e}')
    
    def sends_instruction(self, instruction: str) -> APIResponse:
        if not self._session_id:
            raise NonRecoverableError('No active session - call starts_session first')
        
        headers = self._builds_headers()
        payload = {
            'instruction': instruction
        }
        
        try:
            response = requests.post(
                f'{self.base_url}/sessions/{self._session_id}/messages',
                headers=headers,
                json=payload,
                timeout=60
            )
            
            if response.status_code == 401:
                raise NonRecoverableError('Invalid API key')
            
            if response.status_code >= 500:
                raise RecoverableError(f'Server error: {response.status_code}')
            
            response.raise_for_status()
            data = response.json()
            
            return self._parses_response(data)
            
        except requests.exceptions.ConnectionError as e:
            raise RecoverableError(f'Connection failed: {e}')
        except requests.exceptions.Timeout as e:
            raise RecoverableError(f'Request timed out: {e}')
    
```

---

## never_swallow_exceptions
**cursor_api.py** - 1 violation(s)

[X] ERROR (line 145)
Except block only contains pass at line 145 - exceptions must be logged or rethrown, never swallowed

```python
                timeout=10
            )
        except requests.exceptions.RequestException:
            pass
        
```

---

## provide_meaningful_context
**cursor_api.py** - 3 violation(s)

[!] WARNING (line 60)
Line 60 contains magic number - replace with named constant

```python
            
            if response.status_code >= 500:
                raise RecoverableError(f'Server error: {response.status_code}')
```

[!] WARNING (line 93)
Line 93 contains magic number - replace with named constant

```python
                json=payload,
                timeout=60
            )
```

[!] WARNING (line 99)
Line 99 contains magic number - replace with named constant

```python
            
            if response.status_code >= 500:
                raise RecoverableError(f'Server error: {response.status_code}')
```

---

## simplify_control_flow
**headless_session.py** - 1 violation(s)

[!] WARNING (line 151)
Function "_executes_with_recovery" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return final
    
    def _executes_with_recovery(self, instructions: str, context_loaded: bool) -> ExecutionResult:
        while self._error_recovery.can_retry():
            try:
                return self._executes_with_api(instructions, context_loaded)
            except RecoverableError as e:
                self._error_recovery.increment_attempt()
                self.log.appends_response(f'Recoverable error: {e}. Attempt {self._error_recovery.current_attempts}')
                
                if self._error_recovery.can_retry():
                    self._error_recovery.wait_before_retry(duration=2.0)
                    if self._api:
                        self._api.terminates_session()
                else:
    # ... (truncated)
```

---

Completed: 2025-12-29 18:29:00
Total violations: 7
Scanners executed: 30
