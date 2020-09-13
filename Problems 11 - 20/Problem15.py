# -*- coding: utf-8 -*-
"""
Problem 15: Lattice paths
https://projecteuler.net/problem=15

Starting in the top left corner of a 2×2 grid, and only being able to
move to the right and down, there are exactly 6 routes to the bottom
right corner.

How many such routes are there through a 20×20 grid?
"""
import timeit

# This function returns n!.
def factorial(k):
    product = 1
    for i in range(1, k + 1):
        product *= i
    return product

# This function uses combinatorics to return the number of routes
# through a general m x n grid.
#
# To see why this is true, note that for an m x n grid we must travel
# to the right m times, and down n times, no matter what route we take.
# There are (m + n)! ways to arrange (m + n) different items.  However,
# in our case, m of the items are right, and n of the items are down,
# so we need to remove these m! and n! repetitions from our count.
def routes(m, n):
    return factorial(m + n)//(factorial(m) * factorial(n))

# This prints the solution and the time to completion.
start = timeit.default_timer()
print(routes(20, 20))
stop = timeit.default_timer()
print("Time:", stop - start)
