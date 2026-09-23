import sys
import os
import importlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

mod = importlib.import_module("Code.11_armstrong_number")
is_armstrong_number = mod.is_armstrong_number

def test_is_armstrong_number():
    assert is_armstrong_number(153) is True
    assert is_armstrong_number(9474) is True
    assert is_armstrong_number(123) is False
    assert is_armstrong_number(-153) is False

if __name__ == "__main__":
    test_is_armstrong_number()
    print("All test cases passed.")