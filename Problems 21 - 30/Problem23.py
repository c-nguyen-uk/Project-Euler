# -*- coding: utf-8 -*-
"""Problem 23: Non-abundant sums

https://projecteuler.net/problem=23

A perfect number is a number for which the sum of its proper divisors
is exactly equal to the number. For example, the sum of the proper
divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28
is a perfect number.

A number n is called deficient if the sum of its proper divisors is
less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
smallest number that can be written as the sum of two abundant
numbers is 24. By mathematical analysis, it can be shown that all
integers greater than 28123 can be written as the sum of two abundant
numbers. However, this upper limit cannot be reduced any further by
analysis even though it is known that the greatest number that cannot
be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers.
"""
from custom_timer import computation_time


def proper_divisors_sum(n):
    """Return the sum of proper divisors of n."""
    return sum([i for i in range(1, n) if not n % i])


def is_abundant(n):
    """Check if a given number is an abundant number."""
    if proper_divisors_sum(n) > n:
        return True
    return False


def is_expressible_as_sum(n, list_of_nums):
    """Check if n can be formed as a sum of two elements in list_of_nums."""
    set_of_nums = set(list_of_nums)  # Allow fast lookup algorithm usage
    for num in set_of_nums:
        num_to_lookup = n - num
        if num_to_lookup in set_of_nums:
            return True
    return False


@computation_time
def solution():
    """Return the solution."""
    abundant_list = [i for i in range(1, 28124) if is_abundant(i)]
    solution_list = [i for i in range(1, 28124)
                     if not is_expressible_as_sum(i, abundant_list)]
    return sum(solution_list)


print(solution())
