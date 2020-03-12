# -*- coding: utf-8 -*-
"""
Problem 9: Special Pythagorean triplet
https://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which, a^2 + b^2 = c^2.

For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which
a + b + c = 1000.
Find the product abc.
"""
import timeit

# This brute force function returns Pythaogrean triples which sum to n.
# A more efficient algorithm can be found via parametrisation.

def pythagorean_sum(n):
    for a in range(1,n):
        for b in range(1, n):
            c = (a**2 + b**2)**0.5
            if str(c)[-2] == ".":
                if a + b + int(c) == n:
                    return a, b, int(c)

a, b, c = pythagorean_sum(1000)

# Printing the solution and ensuring that it completes within 1 minute.

start = timeit.default_timer()
print(a*b*c)
stop = timeit.default_timer()
print('Time:', stop - start)
