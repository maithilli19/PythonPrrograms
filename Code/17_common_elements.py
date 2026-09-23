def find_common_elements(lst1: list, lst2: list) -> list:
    """Returns a list of common elements between two lists without duplicates."""
    return list(set(lst1).intersection(set(lst2)))

if __name__ == "__main__":
    l1 = [1, 2, 3, 4]
    l2 = [3, 4, 5, 6]
    print(f"Common elements: {find_common_elements(l1, l2)}")