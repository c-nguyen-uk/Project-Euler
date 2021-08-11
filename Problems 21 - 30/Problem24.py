# -*- coding: utf-8 -*-
"""Problem 24: Lexicographic permutations

https://projecteuler.net/problem=24

A permutation is an ordered arrangement of objects. For example, 3124
is one possible permutation of the digits 1, 2, 3 and 4. If all of the
permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

Solver note: We use a similar approach to hand-conversions between
numbers in different bases, except we use factorials instead of
exponentials.  In the example, the 4th lexicographic permutation is the
3rd element of a list of all lexicographic permutations, and can be
found by looking at the factorial coefficients of 1(2!) + 1(1!) + 0(0!),
where the coefficient indicates the index to use (and remove) from the
0-indexed lexicographically ordered list of digits available, i.e. pick
the 1st index, then the 1st index, then the 0th index, to return 120.
"""
from custom_timer import computation_time


def factorial(n):
    """Return n!."""
    if not n:
        return 1
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod


def factorial_coefficients(n, digits_list):
    """Return a list of coefficients for the nth lexicographic permutation."""
    factorial_coefficients_list = []
    for i in range(len(digits_list) - 1, -1, -1):
        coefficient = 0
        while coefficient*factorial(i) < n:
            coefficient += 1
        factorial_coefficients_list.append(coefficient - 1)
        n -= (coefficient - 1)*factorial(i)
    return factorial_coefficients_list


@computation_time
def solution(n, digits_list):
    """Return the solution, for the nth lexicographic permutation."""
    solution_digits = []
    factorial_coefficients_list = factorial_coefficients(n, digits_list)
    for coefficient in factorial_coefficients_list:
        solution_digits.append(str(digits_list.pop(coefficient)))
    return int("".join(solution_digits))


print(solution(1000000, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
