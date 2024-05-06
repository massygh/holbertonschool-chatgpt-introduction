#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a given number using recursion.

    Parameters:
    n (int): The number for which factorial is to be calculated.

    Returns:
    int: The factorial of the given number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Taking the input from command line argument
f = factorial(int(sys.argv[1]))

# Printing the result
print(f)