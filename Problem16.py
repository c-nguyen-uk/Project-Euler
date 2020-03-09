# -*- coding: utf-8 -*-
"""
Problem 16: Power digit sum
https://projecteuler.net/problem=16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""
import timeit

# This simple function returns the digit sum of any integer.

def digit_sum(n):
    digits = [int(i) for i in str(n)]
    return sum(digits)

# Printing the solution and ensuring that it completes within 1 minute.

start = timeit.default_timer()
print(digit_sum(2**1000))
stop = timeit.default_timer()
print('Time:', stop - start)