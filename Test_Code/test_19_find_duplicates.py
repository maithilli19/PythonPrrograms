import sys
import os
import importlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

mod = importlib.import_module("Code.19_find_duplicates")
find_duplicates = mod.find_duplicates

def test_find_duplicates():
    assert sorted(find_duplicates([1, 2, 3, 2, 4, 5, 1])) == [1, 2]
    assert find_duplicates([1, 2, 3]) == []

if __name__ == "__main__":
    test_find_duplicates()
    print("All test cases passed.")