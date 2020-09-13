# -*- coding: utf-8 -*-
"""
Problem 10: Summation of primes
https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import timeit

# This function is faster than the naive primality tester in Problem 7.
# Taken from:
# rookieslab.com/posts/fastest-way-to-check-if-a-number-is-prime-or-not
# This has speed O(sqrt(n)) since we only check up to sqrt(n).
def is_prime(n):
    if n < 2 or isinstance(n, int) == False:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

# This function returns a list of all primes below n.
def primes_below(n):
    primes = []
    for i in range(n):
        if is_prime(i) == True:
            primes.append(i)
    return primes

# This prints the solution and the time to completion.
start = timeit.default_timer()
print(sum(primes_below(2000000)))
stop = timeit.default_timer()
print("Time:", stop - start)
