def reverse_number(n: int) -> int:
    """Reverse the digits of a number."""
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return reversed_num

if __name__ == "__main__":
    num = 12345
    print(f"The reverse of {num} is {reverse_number(num)}.")
