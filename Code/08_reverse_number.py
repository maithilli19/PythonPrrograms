def reverse_number(n: int) -> int:
    """Reverses the digits of an integer while keeping its sign."""
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_num = 0
    while n > 0:
        reversed_num = (reversed_num * 10) + (n % 10)
        n //= 10
    return sign * reversed_num

if __name__ == "__main__":
    num = int(input("Enter an integer: "))
    print(f"Reversed: {reverse_number(num)}")