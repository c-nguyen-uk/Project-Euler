# -*- coding: utf-8 -*-
"""
Problem 4: Largest palindrome product
https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import timeit

# Checks if a string is palindromic.

def is_pal(text):
    if list(text) == list(reversed(list(text))):
        return True
    else:
        return False

# This function returns the largest palindrome made from two n-digit
# numbers by checking all possible multiplicative combinations.

def largest_palindrome_product(n):
    largest_factor = (10 ** n) - 1
    smallest_factor = 10 ** (n-1)
    largest_palindrome = 0
    for i in range(smallest_factor, largest_factor + 1):
        for j in range(smallest_factor, largest_factor + 1):
            if i * j > largest_palindrome and is_pal(str(i*j)) == True:
                largest_palindrome = i * j
    return largest_palindrome

# Prints the solution and ensures that it completes within 1 minute.

start = timeit.default_timer()
print(largest_palindrome_product(3))
stop = timeit.default_timer()
print("Time:", stop - start)
