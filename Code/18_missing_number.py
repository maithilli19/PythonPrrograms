def find_missing_number(nums: list, n: int) -> int:
    """Finds the missing number in a range from 1 to n."""
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

if __name__ == "__main__":
    arr = [1, 2, 4, 5, 6]
    print(f"Missing number: {find_missing_number(arr, 6)}")