# -*- coding: utf-8 -*-
"""Problem 22: Names scores

https://projecteuler.net/problem=22

Using names.txt, a 46K text file containing over five-thousand first
names, begin by sorting it into alphabetical order. Then working out
the alphabetical value for each name, multiply this value by its
alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the
list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
from custom_timer import computation_time


def names_list():
    """Return the list of names, sorted, from names.txt."""
    with open("Problem22_names.txt") as names_txt:
        names = names_txt.read().replace('"', '').split(",")
        return sorted(names)


def alphabetical_value(word):
    """Return the alphabetical value of a word."""
    value = 0
    for letter in word:
        value += ord(letter.lower()) - 96  # Lowercase letters are 97 to 122
    return value


@computation_time
def solution():
    """Return the solution."""
    total_name_score = 0
    names = names_list()
    for position, name in enumerate(names):
        total_name_score += (position + 1) * alphabetical_value(name)
    return total_name_score


print(solution())
