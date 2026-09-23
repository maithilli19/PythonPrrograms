import sys
import os
import importlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

mod = importlib.import_module("Code.14_char_frequency")
char_frequency = mod.char_frequency

def test_char_frequency():
    assert char_frequency("apple") == {'a': 1, 'p': 2, 'l': 1, 'e': 1}
    assert char_frequency("aba") == {'a': 2, 'b': 1}

if __name__ == "__main__":
    test_char_frequency()
    print("All test cases passed.")