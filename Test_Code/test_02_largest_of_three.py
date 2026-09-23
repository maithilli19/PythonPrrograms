import sys
import os
import importlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

largest_module = importlib.import_module("Code.02_largest_of_three")
find_largest = largest_module.find_largest

def test_find_largest():
    assert find_largest(10, 20, 30) == 30
    assert find_largest(50, 20, 30) == 50
    assert find_largest(10, 80, 30) == 80
    assert find_largest(-5, -2, -10) == -2
    assert find_largest(7, 7, 3) == 7

if __name__ == "__main__":
    test_find_largest()
    print("All test cases passed.")