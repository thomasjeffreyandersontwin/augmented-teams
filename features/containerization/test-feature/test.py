#!/usr/bin/env python3
"""
Test test-feature - plain Python tests
Tests the actual functions from main.py
"""

from main import hello, add_numbers

def test_hello_world():
    """Test hello with World"""
    result = hello("World")
    assert result == "Hello World!", f"Expected 'Hello World!', got '{result}'"
    print("✅ test_hello_world passed")

def test_hello_custom():
    """Test hello with custom name"""
    result = hello("Alice")
    assert result == "Hello Alice!", f"Expected 'Hello Alice!', got '{result}'"
    print("✅ test_hello_custom passed")

def test_add_numbers():
    """Test add_numbers function"""
    result = add_numbers(2, 3)
    assert result == 5, f"Expected 5, got {result}"
    print("✅ test_add_numbers passed")

if __name__ == "__main__":
    test_hello_world()
    test_hello_custom()
    test_add_numbers()
    print("✅ All tests passed")
