def generate_fibonacci(n: int) -> list:
    """Generates the first n numbers of the Fibonacci series."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    series = [0, 1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series

if __name__ == "__main__":
    terms = int(input("Enter number of terms: "))
    print(f"Fibonacci series: {generate_fibonacci(terms)}")