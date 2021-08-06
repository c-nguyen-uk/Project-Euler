# -*- coding: utf-8 -*-
"""Problem 10: Summation of primes

https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
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


def primes_below(n):
    """Return a list of all primes below n."""
    prime_list = []
    for i in range(n):
        if is_prime(i):
            prime_list.append(i)
    return prime_list


@computation_time
def solution(n):
    """Return the solution, for primes below n."""
    return sum(primes_below(n))


print(solution(2000000))
