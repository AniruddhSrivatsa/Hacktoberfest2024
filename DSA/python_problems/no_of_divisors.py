"""
Problem Statement:
Given an integer `n`, the task is to count the number of divisors of `n`.
A divisor of a number is any number that divides `n` perfectly (i.e., without leaving a remainder).

Your task is to implement a function `count_divisors(n)` that returns the total count of divisors of the given integer `n`.

Constraints:
- 1 <= n <= 10^6

The approach should be efficient with a time complexity better than O(n), aiming for O(sqrt(n)).

Example:
Input: n = 36
Output: 9
Explanation: The divisors of 36 are 1, 2, 3, 4, 6, 9, 12, 18, 36. Total 9 divisors.
"""

def count_divisors(n: int) -> int:
    """
    Function to count the number of divisors of a given integer n.
    
    The logic behind the efficiency:
    - Any divisor 'i' less than or equal to sqrt(n) will have a corresponding divisor n // i.
    - Thus, by iterating only up to sqrt(n), we can find both i and n//i simultaneously.
    """
    count = 0  # Initialize count of divisors
    
    # Loop through all numbers from 1 to sqrt(n)
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:  # If i divides n perfectly
            count += 1  # i is a divisor
            
            # If i is not equal to n // i, then n // i is also a distinct divisor
            if i != n // i:
                count += 1  # n // i is another divisor
    
    return count  # Return the total count of divisors

# Main block to test the function
if __name__ == "__main__":
    num = 36  # Example number
    # Output the number of divisors of the number 'num'
    print(f"The number of divisors of {num} is:", count_divisors(num))
