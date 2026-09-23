def is_palindrome_number(n: int) -> bool:
    """Checks whether an integer is a palindrome."""
    if n < 0:
        return False
    original = n
    reversed_num = 0
    while n > 0:
        reversed_num = (reversed_num * 10) + (n % 10)
        n //= 10
    return original == reversed_num

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"{num} is palindrome: {is_palindrome_number(num)}")