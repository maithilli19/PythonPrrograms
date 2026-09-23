def word_frequency(sentence: str) -> dict:
    """Counts the frequency of words in a sentence."""
    words = sentence.lower().split()
    freq = {}
    for word in words:
        clean_word = "".join(c for c in word if c.isalnum())
        if clean_word:
            freq[clean_word] = freq.get(clean_word, 0) + 1
    return freq

if __name__ == "__main__":
    text = "Hello world hello python world"
    print(f"Word frequency: {word_frequency(text)}")