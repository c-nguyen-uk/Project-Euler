# -*- coding: utf-8 -*-
"""Problem 3: Largest prime factor

https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""
from custom_timer import computation_time


@computation_time
def solution(n):
    """Return the largest prime factor up to n."""
    i = 2
    while i <= int(n ** 0.5):  # Check up to floor(sqrt(n)) is sufficient
        if n % i:
            i += 1
        else:
            n = n//i
    return n


print(solution(600851475143))
