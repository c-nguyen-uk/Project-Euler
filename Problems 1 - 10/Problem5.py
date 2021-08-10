# -*- coding: utf-8 -*-
"""Problem 5: Smallest multiple

https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the number
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?

Solver note: This problem can also be solved by using lowest common
multiple, but we focus on a more code-centric solution here.
"""
from custom_timer import computation_time


def factorial(n):
    """Return n!."""
    if not n:
        return 1
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product


def is_divisible(x, n):
    """Check if x is divisible by all natural numbers up to n."""
    for i in range(1, n + 1):
        if x % i:
            return False
    return True


@computation_time
def solution(n):
    """Return the solution, for all numbers from 1 to n."""
    for i in range(n, factorial(n) + 1, n):  # Save computation with n steps
        if is_divisible(i, n):
            return i


print(solution(20))
