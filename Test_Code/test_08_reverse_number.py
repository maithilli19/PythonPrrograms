import sys
import os
import importlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

mod = importlib.import_module("Code.08_reverse_number")
reverse_number = mod.reverse_number

def test_reverse_number():
    assert reverse_number(1234) == 4321
    assert reverse_number(1000) == 1
    assert reverse_number(-567) == -765
    assert reverse_number(0) == 0

if __name__ == "__main__":
    test_reverse_number()
    print("All test cases passed.")