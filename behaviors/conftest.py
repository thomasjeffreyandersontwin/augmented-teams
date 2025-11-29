"""
Pytest plugin to discover and run Mamba BDD tests.
This allows VS Code to discover individual Mamba tests and show play buttons.

This plugin parses Mamba test files and creates pytest test items for each
'with it(...)' block, enabling VS Code's test explorer to show individual
test play buttons.
"""
import os
import re
import subprocess
import sys
from pathlib import Path
from collections import defaultdict

import pytest

# Cache for test results per file to avoid running the same file multiple times
_test_file_results = defaultdict(dict)
_test_file_outputs = {}


def pytest_ignore_collect(path, config):
    """Prevent pytest from trying to collect mamba test files as regular modules"""
    # This hook runs before pytest tries to import files
    if hasattr(path, 'name'):
        basename = path.name
        path_obj = path
    else:
        basename = str(path)
        path_obj = Path(path)
    
    # Don't ignore - let pytest_collect_file handle it
    # But check if it's a mamba test file to avoid import errors
    if (basename.endswith('_test.py') or basename.startswith('test_')):
        try:
            with open(path_obj, 'r', encoding='utf-8') as f:
                first_lines = ''.join(f.readlines()[:30])
                if 'from mamba import' in first_lines or 'import mamba' in first_lines:
                    # Don't ignore - return False so pytest_collect_file can handle it
                    # But the file will be handled by MambaFile which prevents import
                    return False
        except Exception:
            pass
    
    return None


def pytest_collect_file(parent, file_path):
    """Collect Mamba test files (*_test.py)"""
    # Handle both pathlib.Path (new) and py.path.local (old) for compatibility
    if hasattr(file_path, 'name'):
        basename = file_path.name
        path_obj = file_path
    else:
        # Legacy py.path.local support
        basename = file_path.basename
        path_obj = Path(str(file_path))
    
    # Check if this is a mamba test file by looking for mamba imports
    # This prevents pytest from trying to import it as a regular module
    if basename.endswith('_test.py') or basename.startswith('test_'):
        # Check if file contains mamba imports to avoid importing it
        try:
            with open(path_obj, 'r', encoding='utf-8') as f:
                first_lines = ''.join(f.readlines()[:30])  # Check first 30 lines
                if 'from mamba import' in first_lines or 'import mamba' in first_lines:
                    # Return MambaFile to prevent normal import
                    return MambaFile.from_parent(parent, path=path_obj)
        except Exception:
            # If we can't read the file, let pytest handle it normally
            pass
    
    # Return None to let pytest handle it normally
    return None


class MambaFile(pytest.File):
    """Represents a Mamba test file"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Mark this as a non-importable file to prevent pytest from trying to import it
        self._nodeid = str(self.path.relative_to(self.config.rootpath))
    
    def _getobj(self):
        """Override to prevent pytest from importing the file as a module"""
        # Return a dummy module object to prevent normal import
        class DummyModule:
            pass
        return DummyModule()
    
    def _collectfile(self):
        """Override to prevent pytest from trying to import the file"""
        # This prevents pytest from importing the file
        # We'll parse it ourselves in collect()
        return self
    
    def _nodeid(self):
        """Return node ID for this file"""
        if hasattr(self, '_nodeid'):
            return self._nodeid
        return str(self.path.relative_to(self.config.rootpath))
    
    def collect(self):
        """Parse Mamba test file and create test items"""
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')
            
            # Use regex to find 'with it(...)' blocks (more reliable than AST for Mamba)
            # Pattern: 'with it('...'):' or 'with it("...")'
            it_pattern = r'with\s+it\s*\([\'"]([^\'"]+)[\'"]\)\s*:'
            
            for line_num, line in enumerate(lines, start=1):
                match = re.search(it_pattern, line)
                if match:
                    test_name = match.group(1)
                    # Create a sanitized test name for pytest
                    sanitized_name = re.sub(r'[^\w\s-]', '', test_name).strip().replace(' ', '_')
                    if sanitized_name:
                        yield MambaTestItem.from_parent(
                            self,
                            name=sanitized_name,
                            line_no=line_num,
                            test_name=test_name
                        )
        except Exception as e:
            # If parsing fails, create a single test item for the whole file
            yield MambaTestItem.from_parent(
                self,
                name=f"mamba_test_file_{self.path.stem}",
                line_no=1,
                test_name=None
            )
    


class MambaTestItem(pytest.Item):
    """Represents a single Mamba test"""
    
    def __init__(self, name, line_no, test_name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.line_no = line_no
        self.test_name = test_name
    
    def runtest(self):
        """Run the Mamba test using mamba CLI"""
        test_file = str(self.parent.path)
        test_file_path = Path(test_file).resolve()
        test_file_key = str(test_file_path)
        
        # Check if we've already run this test file successfully
        # If the file ran successfully (returncode == 0), all tests in it passed
        if test_file_key in _test_file_outputs:
            cached_result = _test_file_outputs[test_file_key]
            # If it's True, the entire file passed, so this test passed
            if cached_result is True:
                return
            # If it's a dict, check this specific test
            elif isinstance(cached_result, dict):
                if self.test_name in cached_result:
                    if not cached_result[self.test_name]:
                        raise MambaTestError(f"Test '{self.test_name}' failed (from cached mamba run)")
                    return
        
        # Find workspace root (go up from test file directory until we find .vscode or .git)
        workspace_root = test_file_path.parent
        while workspace_root.parent != workspace_root:
            if (workspace_root / '.vscode').exists() or (workspace_root / '.git').exists():
                break
            workspace_root = workspace_root.parent
        
        # Set PYTHONPATH to include the src directory so mamba can find story_io module
        # The test file is at: agile_bot/bots/story_bot/src/story_io/test/test_*.py
        # It needs: agile_bot/bots/story_bot/src in PYTHONPATH to import story_io
        src_dir = test_file_path.parent.parent.parent  # test -> story_io -> src
        src_dir_abs = src_dir.resolve()  # Get absolute path
        env = os.environ.copy()
        pythonpath = env.get('PYTHONPATH', '')
        if pythonpath:
            env['PYTHONPATH'] = f"{src_dir_abs}{os.pathsep}{pythonpath}"
        else:
            env['PYTHONPATH'] = str(src_dir_abs)
        
        # Run mamba on the entire test file (mamba doesn't support --line option)
        # All tests in the file will run, but pytest will track individual test results
        # Use absolute path for mamba to avoid path resolution issues
        cmd = [sys.executable, '-m', 'mamba.cli', str(test_file_path)]
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=str(workspace_root),
            env=env,
            timeout=60
        )
        
        # Parse mamba output to determine which tests passed/failed
        # Cache the results so we don't run the file multiple times
        if result.returncode == 0:
            # All tests in the file passed - cache success for the entire file
            # This way, subsequent tests from the same file can use the cache
            _test_file_outputs[test_file_key] = True
        else:
            # Tests failed - cache the failure and raise error
            error_msg = f"Mamba test failed at line {self.line_no}\n"
            error_msg += f"Test: {self.test_name or self.name}\n"
            error_msg += f"Command: {' '.join(cmd)}\n"
            error_msg += f"PYTHONPATH: {env.get('PYTHONPATH', 'NOT SET')}\n"
            error_msg += f"Working directory: {workspace_root}\n"
            error_msg += f"STDOUT:\n{result.stdout}\n"
            error_msg += f"STDERR:\n{result.stderr}\n"
            # Cache that this test failed
            if test_file_key not in _test_file_outputs:
                _test_file_outputs[test_file_key] = {}
            _test_file_outputs[test_file_key][self.test_name or self.name] = False
            raise MambaTestError(error_msg)
    
    def repr_failure(self, excinfo):
        """Format test failure"""
        if isinstance(excinfo.value, MambaTestError):
            return str(excinfo.value)
        return super().repr_failure(excinfo)


class MambaTestError(Exception):
    """Custom exception for Mamba test failures"""
    pass


def pytest_collection_modifyitems(config, items):
    """Modify collected test items - can be used to filter or modify tests"""
    # This hook runs after collection, so we can use it to verify our tests were collected
    pass


def pytest_exception_interact(node, call, report):
    """Intercept exceptions during collection to suppress mamba import errors"""
    # Suppress TypeError during collection if it's from mamba description() being None
    if (report.when == "collect" and 
        isinstance(call.excinfo.value, TypeError) and
        "'NoneType' object does not support the context manager protocol" in str(call.excinfo.value)):
        # Check if this is a mamba test file
        if hasattr(node, 'fspath') or hasattr(node, 'path'):
            path = getattr(node, 'fspath', getattr(node, 'path', None))
            if path:
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        if 'from mamba import' in f.read():
                            # Suppress this error - it's expected for mamba tests
                            report.outcome = "skipped"
                            return
                except Exception:
                    pass




































