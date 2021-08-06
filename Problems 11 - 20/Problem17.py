# -*- coding: utf-8 -*-
"""Problem 17: Number letter counts

https://projecteuler.net/problem=17

If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens.  For example, 342 (three hundred
and forty-two) contains 23 letters and 115 (one hundred and fifteen)
contains 20 letters.  The use of "and" when writing out numbers is in
compliance with British usage.

Solver note:: This problem can also be solved by hand, but we focus on
a more code-centric solution here.
"""
from custom_timer import computation_time


UNITS = {
    "1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
    "6": "six", "7": "seven", "8": "eight", "9": "nine"
    }
ELEVENTEENS = {
    "11": "eleven", "12": "twelve", "13": "thirteen", "14": "fourteen",
    "15": "fifteen", "16": "sixteen", "17": "seventeen",
    "18": "eighteen", "19": "nineteen"
    }
TENS = {
    "20": "twenty", "30": "thirty", "40": "forty", "50": "fifty",
    "60": "sixty", "70": "seventy", "80": "eighty", "90": "ninety"
        }


def number_to_text(n):
    """Convert an integer in [1, 1000] into a string.

    Note that this can be generalised to greater ranges using similar logic,
    and that it is possible to refactor this code to avoid repetition, but
    care needs to be taken with indexing issues.
    """
    n = str(n)
    word = ""
    if len(n) == 1:  # Do 1-9
        word += UNITS[n[-1]]
    if len(n) == 2:
        if n[-2] == "1" and n[-1] == "0":  # Do 10
            word += "ten"
        elif n[-2] == "1" and n[-1] != "0":  # Do 11-19
            word += ELEVENTEENS[n[-2:]]
        if n[-2] != "1" and n[-1] != "0":  # Do 21-99, not ending in 0
            word += TENS[n[-2] + "0"] + "-" + UNITS[n[-1]]
        elif n[-2] != "1" and n[-1] == "0":  # Do 20-90, ending in 0
            word += TENS[n[-2:]]
    if len(n) == 3:
        if n[-2] == "0" and n[-1] == "0":  # Do 100-900, ending in 00
            word += UNITS[n[-3]] + " hundred"
        elif n[-2] != "0" or n[-3] != "0":
            word += UNITS[n[0]] + " hundred and "
            if n[-2] == "1" and n[-1] != "0":  # Do 101-999, ending in 11-19
                word += ELEVENTEENS[n[-2:]]
            elif n[-2] == "1" and n[-1] == "0":  # Do 101-999, ending in 10
                word += "ten"
            if n[-2] != "1" and n[-2] != "0" and n[-1] != "0":
                word += TENS[n[-2] + "0"] + "-" + UNITS[n[-1]]
            elif n[-2] != "1" and n[-2] != "0" and n[-1] == "0":
                word += TENS[n[-2:]]
            elif n[-2] != "1" and n[-2] == "0":
                word += UNITS[n[-1]]
    if len(n) == 4:
        word += "one thousand"
    return word.title()


@computation_time
def solution():
    """Return the solution."""
    return sum([len(number_to_text(i).replace(" ", "").replace("-", ""))
                for i in range(1, 1001)])


print(solution())
