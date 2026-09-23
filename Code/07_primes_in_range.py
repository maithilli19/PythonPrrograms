def get_primes_in_range(start: int, end: int) -> list:
    """Returns a list of prime numbers between start and end (inclusive)."""
    primes = []
    for num in range(max(2, start), end + 1):
        is_p = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_p = False
                break
        if is_p:
            primes.append(num)
    return primes

if __name__ == "__main__":
    s = int(input("Enter start: "))
    e = int(input("Enter end: "))
    print(f"Primes: {get_primes_in_range(s, e)}")