import sys
import os
import importlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

mod = importlib.import_module("Code.17_common_elements")
find_common_elements = mod.find_common_elements

def test_find_common_elements():
    assert sorted(find_common_elements([1, 2, 3], [2, 3, 4])) == [2, 3]
    assert find_common_elements([1, 2], [3, 4]) == []

if __name__ == "__main__":
    test_find_common_elements()
    print("All test cases passed.")