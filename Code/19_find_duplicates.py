def find_duplicates(lst: list) -> list:
    """Returns a list of duplicate elements from an input list."""
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

if __name__ == "__main__":
    arr = [1, 2, 3, 2, 4, 5, 1]
    print(f"Duplicates: {find_duplicates(arr)}")