def remove_duplicates(lst: list) -> list:
    """Removes duplicate elements while preserving order."""
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

if __name__ == "__main__":
    sample = [1, 2, 2, 3, 4, 4, 5]
    print(f"Without duplicates: {remove_duplicates(sample)}")