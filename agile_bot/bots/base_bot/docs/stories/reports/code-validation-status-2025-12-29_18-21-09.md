# Validation Status - code
Started: 2025-12-29 18:21:09
Files: 275


## Cross-File Duplication Analysis
Scanning 4 changed file(s) against 275 total files...
Extracted 179 changed blocks, 4205 reference blocks
Starting 752,695 pairwise comparisons...
Comparing: 3% (26,460/752,695) - 0 violations - ETA: 274s  
Comparing: 6% (48,677/752,695) - 0 violations - ETA: 289s  
Comparing: 8% (67,351/752,695) - 0 violations - ETA: 305s  
Comparing: 11% (83,961/752,695) - 0 violations - ETA: 318s  
Comparing: 14% (109,431/752,695) - 0 violations - ETA: 293s  
Comparing: 16% (127,866/752,695) - 0 violations - ETA: 293s  
Comparing: 20% (150,872/752,695) - 0 violations - ETA: 279s  
Comparing: 23% (176,488/752,695) - 0 violations - ETA: 261s  
Comparing: 25% (193,746/752,695) - 0 violations - ETA: 259s  
Comparing: 28% (211,514/752,695) - 0 violations - ETA: 255s  
Comparing: 30% (229,832/752,695) - 0 violations - ETA: 250s  
Comparing: 32% (242,971/752,695) - 0 violations - ETA: 251s  
Comparing: 34% (256,662/752,695) - 0 violations - ETA: 251s  
Comparing: 36% (272,259/752,695) - 0 violations - ETA: 247s  
Comparing: 37% (284,102/752,695) - 0 violations - ETA: 247s  
Comparing: 39% (296,943/752,695) - 0 violations - ETA: 245s  
Comparing: 41% (310,675/752,695) - 0 violations - ETA: 241s  
Comparing: 42% (321,299/752,695) - 0 violations - ETA: 241s  
Comparing: 44% (331,382/752,695) - 0 violations - ETA: 241s  
Comparing: 45% (343,170/752,695) - 0 violations - ETA: 238s  
Comparing: 46% (353,370/752,695) - 0 violations - ETA: 237s  
Comparing: 48% (363,320/752,695) - 0 violations - ETA: 235s  
Comparing: 49% (373,763/752,695) - 0 violations - ETA: 233s  
Comparing: 50% (383,211/752,695) - 0 violations - ETA: 231s  
Comparing: 52% (391,939/752,695) - 0 violations - ETA: 230s  
Comparing: 54% (413,566/752,695) - 0 violations - ETA: 213s  
Comparing: 58% (441,018/752,695) - 0 violations - ETA: 190s  
Comparing: 61% (463,664/752,695) - 0 violations - ETA: 174s  
Comparing: 64% (483,297/752,695) - 0 violations - ETA: 161s  
Comparing: 68% (513,250/752,695) - 0 violations - ETA: 139s  
Comparing: 71% (539,721/752,695) - 0 violations - ETA: 122s  
Comparing: 75% (567,323/752,695) - 0 violations - ETA: 104s  
Comparing: 78% (591,074/752,695) - 0 violations - ETA: 90s  
Comparing: 83% (624,737/752,695) - 0 violations - ETA: 69s  
Comparing: 86% (651,484/752,695) - 0 violations - ETA: 54s  
Comparing: 89% (671,658/752,695) - 0 violations - ETA: 43s  
Comparing: 92% (696,912/752,695) - 0 violations - ETA: 29s  
Comparing: 95% (719,696/752,695) - 0 violations - ETA: 17s  
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

## use_domain_language
**cli_executor.py** - 18 violation(s)

[i] INFO (line 15)
Class "CliExecutor" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 17)
Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 17)
Function "__init__" uses parameter name "cli_instance" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 20)
Function "execute_and_output" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 20)
Function "execute_and_output" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 20)
Function "execute_and_output" uses parameter name "cli_args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 32)
Function "_log_execution_info" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 32)
Function "_log_execution_info" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 32)
Function "_log_execution_info" uses parameter name "cli_args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 38)
Function "_execute_headless" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 38)
Function "_execute_headless" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 82)
Function "_format_headless_result" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 102)
Function "_execute_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 102)
Function "_execute_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 102)
Function "_execute_command" uses parameter name "cli_args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 114)
Function "_handle_working_dir_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 114)
Function "_handle_working_dir_command" uses parameter name "cli_args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 133)
Function "_output_result" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

## use_domain_language
**cli_parameter_parser.py** - 24 violation(s)

[i] INFO (line 9)
Function "parse_arguments" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 9)
Function "parse_arguments" uses parameter name "description" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 18)
Function "_build_remaining_args" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 18)
Function "_build_remaining_args" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 18)
Function "_build_remaining_args" uses parameter name "unknown" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 36)
Function "_create_argument_parser" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 36)
Function "_create_argument_parser" uses parameter name "description" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 55)
Function "_relocate_file_path_from_action" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 55)
Function "_relocate_file_path_from_action" uses parameter name "unknown" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 62)
Function "_build_params_from_args" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 62)
Function "_build_params_from_args" uses parameter name "unrecognized_flags" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 84)
Function "_looks_like_file_path" uses parameter name "arg" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 89)
Function "_looks_like_directory_path" uses parameter name "arg" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 96)
Function "_append_to_param" uses parameter name "key" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 105)
Function "_parse_key_value_arg" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 105)
Function "_parse_key_value_arg" uses parameter name "arg" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 105)
Function "_parse_key_value_arg" uses parameter name "arg_list" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 147)
Function "_parse_file_path_arg" uses parameter name "arg" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 155)
Function "_parse_context_arg" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 155)
Function "_parse_context_arg" uses parameter name "arg" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 164)
Function "_process_unrecognized_flags" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 164)
Function "_process_unrecognized_flags" uses parameter name "unrecognized_flags" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 183)
Function "_process_context_args" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 183)
Function "_process_context_args" uses parameter name "context_args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

## use_domain_language
**cursor_api.py** - 14 violation(s)

[i] INFO (line 18)
Class "APIResponse" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 28)
Class "CursorHeadlessAPI" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 30)
Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 30)
Function "__init__" uses parameter name "api_key" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 30)
Function "__init__" uses parameter name "base_url" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 36)
Function "session_id" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 39)
Function "starts_session" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 39)
Function "starts_session" uses parameter name "instructions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 79)
Function "sends_instruction" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 79)
Function "sends_instruction" uses parameter name "instruction" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 112)
Function "polls_session_status" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 133)
Function "terminates_session" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 150)
Function "_builds_headers" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 157)
Function "_parses_response" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

## use_domain_language
**headless_session.py** - 16 violation(s)

[i] INFO (line 17)
Class "HeadlessSession" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 19)
Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 27)
Function "invokes" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 27)
Function "invokes" uses parameter name "message" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 47)
Function "invokes_operation" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 47)
Function "invokes_operation" uses parameter name "operation" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 119)
Function "_loads_context" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 124)
Function "_prepares_instructions" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 124)
Function "_prepares_instructions" uses parameter name "message" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 124)
Function "_prepares_instructions" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 151)
Function "_executes_with_recovery" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 151)
Function "_executes_with_recovery" uses parameter name "instructions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 151)
Function "_executes_with_recovery" uses parameter name "context_loaded" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 168)
Function "_executes_with_api" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 168)
Function "_executes_with_api" uses parameter name "instructions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 168)
Function "_executes_with_api" uses parameter name "context_loaded" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

Completed: 2025-12-29 18:27:41
Total violations: 79
Scanners executed: 30
