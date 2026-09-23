import sys
import os
import importlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

mod = importlib.import_module("Code.15_second_largest")
find_second_largest = mod.find_second_largest

def test_find_second_largest():
    assert find_second_largest([10, 20, 4, 45, 99]) == 45
    assert find_second_largest([10, 10, 10]) is None
    assert find_second_largest([5]) is None
    assert find_second_largest([-10, -20, -3]) == -10

if __name__ == "__main__":
    test_find_second_largest()
    print("All test cases passed.")