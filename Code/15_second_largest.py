def find_second_largest(numbers: list):
    """Returns the second largest unique element in a list."""
    unique_nums = list(set(numbers))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort()
    return unique_nums[-2]

if __name__ == "__main__":
    lst = [10, 20, 4, 45, 99, 99]
    print(f"Second largest: {find_second_largest(lst)}")