# Validation Status - code
Started: 2025-12-29 00:24:28
Files: 265

## avoid_excessive_guards
**repl_session.py** - 1 violation(s)

[!] WARNING (line 1110)
Line 1110: Variable truthiness check detected (if not args:). Assume variable exists - let code fail fast if missing.

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

## avoid_unnecessary_parameter_passing
**render_action.py** - 2 violation(s)

[!] WARNING (line 50)
Instance property "self._render_specs" is extracted to variable "render_specs" and passed to internal method "_execute_synchronizers". Access via self._render_specs directly instead.

[!] WARNING (line 84)
Instance property "self._render_specs" is extracted to variable "render_specs" and passed to internal method "_execute_synchronizers". Access via self._render_specs directly instead.

---

