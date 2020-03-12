# -*- coding: utf-8 -*-
"""
Problem 7: 10001st prime
https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import timeit

# This simple function checks that p is prime (slow for large p).

def is_prime(p):
    if p < 2 or isinstance(p, int) == False:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    for i in range(3, p-1 , 2):
        if p % i == 0:
            return False
    return True

# This funciton returns a list of the first n primes.

def nth_prime(n):
    if n == 1:
        return 2
    prime_list = [2, 3]
    i = prime_list[-1]
    while len(prime_list) < n:
        if is_prime(i+2) == True:
            prime_list.append(i+2)
            i += 2
        else:
            i += 2
    return prime_list[-1]

# Printing the solution and ensuring that it completes within 1 minute.

start = timeit.default_timer()
print(nth_prime(10001))
stop = timeit.default_timer()
print('Time:', stop - start)
