# -*- coding: utf-8 -*-
"""Problem 15: Lattice paths

https://projecteuler.net/problem=15

Starting in the top left corner of a 2×2 grid, and only being able to
move to the right and down, there are exactly 6 routes to the bottom
right corner.

How many such routes are there through a 20×20 grid?
"""
from custom_timer import computation_time


def factorial(k):
    """Return k!."""
    if not k:
        return 1
    product = 1
    for i in range(1, k + 1):
        product *= i
    return product


@computation_time
def solution(m, n):
    """Return the solution, for routes through a general m x n grid.

    Combinatorics is used - to see why this works, note that for an
    m x n grid we must travel to the right m times, and down n times,
    no matter what route we take.  There are (m + n)! ways to arrange
    (m + n) different items.  However, in our case, m of the items are
    right, and n of the items are down, so we need to remove these m!
    and n! repetitions from our count.
    """
    return factorial(m + n)//(factorial(m) * factorial(n))


print(solution(20, 20))
