# -*- coding: utf-8 -*-
"""Problem 16: Power digit sum

https://projecteuler.net/problem=16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""
from custom_timer import computation_time


@computation_time
def solution(n):
    """Return the solution, for an integer n."""
    digits = [int(i) for i in str(n)]
    return sum(digits)


print(solution(2**1000))
