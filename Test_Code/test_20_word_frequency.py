import sys
import os
import importlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

mod = importlib.import_module("Code.20_word_frequency")
word_frequency = mod.word_frequency

def test_word_frequency():
    assert word_frequency("Hello world hello") == {"hello": 2, "world": 1}
    assert word_frequency("Python is great. Python is fast!") == {
        "python": 2, "is": 2, "great": 1, "fast": 1
    }

if __name__ == "__main__":
    test_word_frequency()
    print("All test cases passed.")