# -*- coding: utf-8 -*-
"""
Problem 3: Largest prime factor
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""
import timeit

# This function returns the largest prime factor up to n. Note that
# it only needs to check up to the floor of the square root of n.

def largest_prime_factor(n):
    i = 2
    while i <= int(n ** 0.5):
        if n % i != 0:
            i += 1
        else:
            n = n//i
    return n

# Prints the solution and ensures that it completes within 1 minute.

start = timeit.default_timer()
print(largest_prime_factor(600851475143))
stop = timeit.default_timer()
print("Time:", stop - start)
