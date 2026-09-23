import sys
import os
import importlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

mod = importlib.import_module("Code.13_palindrome_string")
is_palindrome_string = mod.is_palindrome_string

def test_is_palindrome_string():
    assert is_palindrome_string("madam") is True
    assert is_palindrome_string("A man a plan a canal Panama") is True
    assert is_palindrome_string("hello") is False

if __name__ == "__main__":
    test_is_palindrome_string()
    print("All test cases passed.")