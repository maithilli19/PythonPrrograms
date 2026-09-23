def is_palindrome_string(text: str) -> bool:
    """Checks if a string is a palindrome (case-insensitive, ignores non-alphanumeric characters)."""
    clean_text = "".join(c.lower() for c in text if c.isalnum())
    return clean_text == clean_text[::-1]

if __name__ == "__main__":
    s = input("Enter string: ")
    print(f"Is palindrome: {is_palindrome_string(s)}")