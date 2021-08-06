# -*- coding: utf-8 -*-
"""Problem 6: Sum square difference

https://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385.
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025.
Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.

Solver note: We use well-known mathematical formulae here for
optimisation, but a purely code-centric solution without maths is
trivial to do.
"""
from custom_timer import computation_time


def sum_of_squares(n):
    """Return the sum of the squares of the first n naturals."""
    return int((n*(n+1)*(2*n+1))/6)


def square_of_sum(n):
    """Return the square of the sum of the first n naturals."""
    return int(((n*(n+1))/2)**2)


@computation_time
def solution(n):
    """Return the solution, for the first n naturals."""
    return square_of_sum(n) - sum_of_squares(n)


print(solution(100))
