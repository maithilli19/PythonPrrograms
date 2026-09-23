def check_sign(num: float) -> str:
    """Determines whether a number is Positive, Negative, or Zero."""
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

if __name__ == "__main__":
    val = float(input("Enter a number: "))
    print(f"The number is {check_sign(val)}.")