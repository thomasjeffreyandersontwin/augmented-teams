#!/usr/bin/env python3
"""
Test [FEATURE_NAME] - plain Python tests
No service dependencies
"""

from main import example_function  # UPDATE: Import your functions

def test_example():
    """Test example function"""
    result = example_function("arg")
    assert result == "expected", f"Expected 'expected', got '{result}'"
    print("✅ test_example passed")

# ADD: More test functions for each function in main.py

if __name__ == "__main__":
    test_example()
    # ADD: Call more tests here
    print("✅ All tests passed")
