# -*- coding: utf-8 -*-
"""Problem 20: Factorial digit sum

https://projecteuler.net/problem=20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is
3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
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


@computation_time
def solution(n):
    """Return the solution, for n!."""
    return sum([int(i) for i in list(str(factorial(n)))])


print(solution(100))
