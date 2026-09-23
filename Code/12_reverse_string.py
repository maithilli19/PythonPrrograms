def reverse_string(text: str) -> str:
    """Reverses a string without using slicing [::-1]."""
    reversed_str = ""
    for char in text:
        reversed_str = char + reversed_str
    return reversed_str

if __name__ == "__main__":
    s = input("Enter string: ")
    print(f"Reversed: {reverse_string(s)}")