# -*- coding: utf-8 -*-
"""Problem 4: Largest palindrome product

https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
from custom_timer import computation_time


def is_pal(text):
    """Check if input string is palindromic."""
    if list(text) == list(reversed(list(text))):
        return True
    return False


@computation_time
def solution(n):
    """Return the solution, for n-digit numbers.

    Here we check all possible multiplicative combinations.
    """
    largest_factor = (10 ** n) - 1
    smallest_factor = 10 ** (n - 1)
    largest_palindrome = 0
    for i in range(smallest_factor, largest_factor + 1):
        for j in range(smallest_factor, largest_factor + 1):
            if (i * j > largest_palindrome) and is_pal(str(i*j)):
                largest_palindrome = i * j
    return largest_palindrome


print(solution(3))
