import sys
import os
import importlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

mod = importlib.import_module("Code.07_primes_in_range")
get_primes_in_range = mod.get_primes_in_range

def test_get_primes_in_range():
    assert get_primes_in_range(1, 10) == [2, 3, 5, 7]
    assert get_primes_in_range(10, 20) == [11, 13, 17, 19]
    assert get_primes_in_range(24, 28) == []

if __name__ == "__main__":
    test_get_primes_in_range()
    print("All test cases passed.")