def char_frequency(text: str) -> dict:
    """Counts the frequency of each character in a string."""
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq

if __name__ == "__main__":
    s = input("Enter string: ")
    print(f"Character Frequencies: {char_frequency(s)}")