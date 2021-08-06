# -*- coding: utf-8 -*-
"""Problem 7: 10001st prime

https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
see that the 6th prime is 13.

What is the 10 001st prime number?
"""
from custom_timer import computation_time


def is_prime(n):
    """Check primality of p."""
    if n < 2 or not isinstance(n, int):
        return False
    i = 2
    while i*i <= n:
        if not n % i:
            return False
        i += 1
    return True


@computation_time
def solution(n):
    """Return the solution, for the nth prime."""
    if n == 1:
        return 2
    prime_list = [2, 3]
    i = prime_list[-1]
    while len(prime_list) < n:
        if is_prime(i + 2):
            prime_list.append(i + 2)
        i += 2
    return prime_list[-1]


print(solution(10001))
