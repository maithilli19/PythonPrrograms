import sys
import os
import importlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

mod = importlib.import_module("Code.12_reverse_string")
reverse_string = mod.reverse_string

def test_reverse_string():
    assert reverse_string("python") == "nohtyp"
    assert reverse_string("Hello World") == "dlroW olleH"
    assert reverse_string("a") == "a"
    assert reverse_string("") == ""

if __name__ == "__main__":
    test_reverse_string()
    print("All test cases passed.")