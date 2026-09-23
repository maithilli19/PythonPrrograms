import sys
import os
import importlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

mod = importlib.import_module("Code.01_even_odd")
is_even_or_odd = mod.is_even_or_odd

def test_is_even_or_odd():
    assert is_even_or_odd(4) == "Even"
    assert is_even_or_odd(7) == "Odd"
    assert is_even_or_odd(0) == "Even"
    assert is_even_or_odd(-2) == "Even"
    assert is_even_or_odd(-3) == "Odd"

if __name__ == "__main__":
    test_is_even_or_odd()
    print("All test cases passed.")