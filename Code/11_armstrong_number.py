def is_armstrong_number(n: int) -> bool:
    """Checks whether an integer is an Armstrong number."""
    if n < 0:
        return False
    digits = str(n)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == n

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"{num} is Armstrong: {is_armstrong_number(num)}")