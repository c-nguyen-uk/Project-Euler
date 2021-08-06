# -*- coding: utf-8 -*-
"""Problem 1: Multiples of 3 and 5

https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or
5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Solver note: This problem can also be solved using arithmetic sums, but we
focus on a more code-centric solution here.
"""
from custom_timer import computation_time


def multiples(x, n):
    """Return a list of multiples of x, below n."""
    multiple_list = []
    for i in range(1, -(-n//x)):  # Implement the ceiling function
        multiple_list.append(i*x)
    return multiple_list


@computation_time
def solution():
    """Return the solution."""
    multiples_of_3_and_5 = set(multiples(3, 1000) + multiples(5, 1000))
    return sum(multiples_of_3_and_5)


print(solution())
