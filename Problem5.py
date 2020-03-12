# -*- coding: utf-8 -*-
"""
Problem 5: Smallest multiple
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the number
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?
"""
import timeit

# This problem can also be solved by using lowest common multiple.
# We focus on a more code-centric solution here.


# This simple function returns n!.

def factorial(n):
    product = 1
    for i in range(1, n+1):
        product *= i
    return product

# This function checks if x is divisible by all naturals up to n.

def is_divisible(x, n):
    for i in range(1, n + 1):
        if x % i == 0:
            pass
        else:
            return False
    return True

# This function returns the smallest number divisible by all naturals
# to n, with some steps being saved on by going in steps of n.

def smallest_number_divisible(n):
    for i in range(n, factorial(n)+1, n):
        if is_divisible(i, n) == True:
            return i

# Printing the solution and ensuring that it completes within 1 minute.

start = timeit.default_timer()
print(smallest_number_divisible(20))
stop = timeit.default_timer()
print('Time:', stop - start)
