# -*- coding: utf-8 -*-
"""
Problem 6: Sum square difference
https://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385.
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025.
Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""
import timeit

# We use well-known mathematical formulae here for optimisation.
# A purely code-centric solution without maths is trivial to do.

# This function returns the sum of the squares of the first n naturals.
def sum_of_squares(n):
    return int((n*(n+1)*(2*n+1))/6)

# This function returns the square of the sum of the first n naturals.
def square_of_sum(n):
    return int(((n*(n+1))/2)**2)


# This prints the solution and the time to completion.
start = timeit.default_timer()
print(square_of_sum(100) - sum_of_squares(100))
stop = timeit.default_timer()
print("Time:", stop - start)
