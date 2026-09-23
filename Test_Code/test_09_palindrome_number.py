import sys
import os
import importlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

mod = importlib.import_module("Code.09_palindrome_number")
is_palindrome_number = mod.is_palindrome_number

def test_is_palindrome_number():
    assert is_palindrome_number(121) is True
    assert is_palindrome_number(123) is False
    assert is_palindrome_number(-121) is False
    assert is_palindrome_number(7) is True

if __name__ == "__main__":
    test_is_palindrome_number()
    print("All test cases passed.")