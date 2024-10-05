def factorial(n: int) -> int:
    """Calculate the factorial of a number."""
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

# Main block to test the function
if __name__ == "__main__":
    num = 5
    print(f"The factorial of {num} is {factorial(num)}.")
