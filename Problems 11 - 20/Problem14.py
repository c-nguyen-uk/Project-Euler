# -*- coding: utf-8 -*-
"""Problem 14: Longest Collatz sequence

https://projecteuler.net/problem=14

The following iterative sequence is defined for the set of positive
integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz
Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one
million.
"""
from custom_timer import computation_time


def collatz_seq(n):
    """Return the length of the Collatz chain starting with n."""
    chain_length = 1
    if n == 1:
        return chain_length
    while n != 1:
        if n % 2:
            # Since n is odd, then 3n+1 is even, so we can add 2 to
            # chain_length and instead compute the next element of the chain
            # using an input of (3n+1)/2.
            chain_length += 2
            n = (3*n + 1)//2
        else:
            chain_length += 1
            n = n//2
    return chain_length


@computation_time
def solution(k):
    """Return the solution, for the starting number under k.

    Note that since collatz_seq(n) = collatz_seq(n/2) + 1, for even n, we
    don't need to compute any chains below k/2.
    """
    longest_chain_start_number = 1
    for i in range(k//2 + 1, k):
        if collatz_seq(i) > collatz_seq(longest_chain_start_number):
            longest_chain_start_number = i
    return longest_chain_start_number


print(solution(1000000))
