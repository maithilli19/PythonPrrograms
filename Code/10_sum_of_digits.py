def sum_of_digits(n: int) -> int:
    """Calculates the sum of digits of an integer."""
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"Sum of digits: {sum_of_digits(num)}")