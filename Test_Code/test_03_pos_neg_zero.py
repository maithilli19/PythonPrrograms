import sys
import os
import importlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

mod = importlib.import_module("Code.03_pos_neg_zero")
check_sign = mod.check_sign

def test_check_sign():
    assert check_sign(15) == "Positive"
    assert check_sign(-9) == "Negative"
    assert check_sign(0) == "Zero"

if __name__ == "__main__":
    test_check_sign()
    print("All test cases passed.")