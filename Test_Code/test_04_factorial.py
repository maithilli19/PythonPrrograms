import sys
import os
import importlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

mod = importlib.import_module("Code.04_factorial")
calculate_factorial = mod.calculate_factorial

def test_calculate_factorial():
    assert calculate_factorial(0) == 1
    assert calculate_factorial(1) == 1
    assert calculate_factorial(5) == 120
    assert calculate_factorial(7) == 5040

if __name__ == "__main__":
    test_calculate_factorial()
    print("All test cases passed.")