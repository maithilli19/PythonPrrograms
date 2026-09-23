def is_even_or_odd(number: int) -> str:
    """Returns 'Even' if number is even, otherwise 'Odd'."""
    if number % 2 == 0:
        return "Even"
    return "Odd"

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"The number is {is_even_or_odd(num)}.")