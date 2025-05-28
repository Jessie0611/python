# The factorial of a number is the product of all positive integers less than or equal to that number. It’s written with an exclamation mark: n!=n×(n−1)×(n−2)×…×1
# The factorial of a number n is n * (n-1) * (n-2) * ... * 1.  If n is 0 or 1, the function returns 1. This is the base case.
# Defines a function factorial(n):  It uses recursion to calculate the factorial.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Test the function
number = 5  # Calls the function with number = 5:
result = factorial(number)
# factorial(5) returns 5 * 4 * 3 * 2 * 1 = 120.
print(f"The factorial of {number} is {result}")

# Test the function
number = 4  # Calls the function with number = 10:
result = factorial(number)
print(f"The factorial of {number} is {result}")  # The factorial of 4 is 24

# Where Is Factorial Used? Math: Especially in combinatorics (e.g., calculating how many ways you can arrange things).
# Probability: In formulas like permutations and combinations. Computer science: In recursive algorithms and problem-solving techniques.
