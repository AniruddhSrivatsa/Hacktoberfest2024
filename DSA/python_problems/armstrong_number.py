"""
Problem Statement:
A number is called an Armstrong number if the sum of its digits, each raised to the power of the number of digits, equals the number itself.

Your task is to implement a function `is_armstrong(n)` that checks if a given number `n` is an Armstrong number using a while loop.

Constraints:
- n is a non-negative integer.

Example:
Input: n = 153
Output: True (since 1^3 + 5^3 + 3^3 = 153)
"""

def is_armstrong(n: int) -> bool:
    """
    This function checks whether a number `n` is an Armstrong number using a while loop.
    
    Steps:
    1. Calculate the number of digits in `n`.
    2. Extract each digit of `n` using a while loop.
    3. Calculate the sum of each digit raised to the power of the number of digits.
    4. Return True if the sum equals the original number, otherwise return False.
    """
    
    # Step 1: Save the original number and find the number of digits
    original_number = n
    num_digits = 0
    temp = n
    
    # Count the number of digits using a while loop
    while temp > 0:
        temp //= 10
        num_digits += 1
    
    # Step 2: Calculate the Armstrong sum
    armstrong_sum = 0
    temp = n  # Reset temp to n to use in the next while loop
    
    while temp > 0:
        digit = temp % 10  # Extract the last digit
        armstrong_sum += digit ** num_digits  # Add the digit raised to the power of num_digits
        temp //= 10  # Remove the last digit from temp
    
    # Step 3: Check if the sum of powered digits equals the original number
    return armstrong_sum == original_number

# Main block to test the function
if __name__ == "__main__":
    # Example input
    n = 153
    
    # Call the function and print the result
    if is_armstrong(n):
        print(f"{n} is an Armstrong number.")
    else:
        print(f"{n} is NOT an Armstrong number.")
