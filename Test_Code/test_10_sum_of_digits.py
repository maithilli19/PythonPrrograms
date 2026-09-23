import sys
import os
import importlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

mod = importlib.import_module("Code.10_sum_of_digits")
sum_of_digits = mod.sum_of_digits

def test_sum_of_digits():
    assert sum_of_digits(123) == 6
    assert sum_of_digits(999) == 27
    assert sum_of_digits(-45) == 9
    assert sum_of_digits(0) == 0

if __name__ == "__main__":
    test_sum_of_digits()
    print("All test cases passed.")