# -*- coding: utf-8 -*-
"""Problem 9: Special Pythagorean triplet

https://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which, a^2 + b^2 = c^2.

For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which
a + b + c = 1000.
Find the product abc.
"""
from custom_timer import computation_time


def pythagorean_sum(n):
    """Return Pythagorean triples which sum to n, using brute force."""
    for a in range(1, n):
        for b in range(1, n):
            c = (a**2 + b**2)**0.5
            if str(c)[-2] == ".":  # Check if c ends in .00
                if a + b + int(c) == n:
                    return a, b, int(c)


@computation_time
def solution():
    """Return the solution."""
    a, b, c = pythagorean_sum(1000)
    return a*b*c


print(solution())
