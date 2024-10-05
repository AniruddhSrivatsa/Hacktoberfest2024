def fibonacci(n: int) -> None:
    """Generate Fibonacci sequence up to n terms."""
    a, b = 0, 1
    count = 0
    while count < n:
        print(a, end=" ")
        a, b = b, a + b
        count += 1
    print()

# Main block to test the function
if __name__ == "__main__":
    terms = 10
    print(f"Fibonacci sequence up to {terms} terms:")
    fibonacci(terms)
