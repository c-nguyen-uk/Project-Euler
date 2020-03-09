# -*- coding: utf-8 -*-
"""
Problem 14: Longest Collatz sequence
https://projecteuler.net/problem=14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import timeit

# This function returns the length of a Collatz sequence starting with n.
# Note also that if n is odd, then 3n+1 is even, so we can add 2 to the count
# and instead compute the next element of the chain using (3n+1)/2.

def collatz_seq(n):
    count = 1
    if n == 1:
        return count
    while n != 1:
        if n % 2 == 0:
            count += 1
            n = n//2
        else:
            count += 2
            n = (3*n + 1)//2
    return count

# This function returns the starting number under k with the longest sequence. 
# Note that since collatz_seq(n) = collatz_seq(n/2) + 1, for even n, we don't
# need to compute any chains below k/2.

def longest_collatz_number(k):
    long_start_number = 1
    for i in range(k//2 + 1, k):
        if collatz_seq(i) > collatz_seq(long_start_number):
            long_start_number = i
    return long_start_number

# Printing the solution and ensuring that it completes within 1 minute.

start = timeit.default_timer()
print(longest_collatz_number(1000000))
stop = timeit.default_timer()
print('Time:', stop - start)