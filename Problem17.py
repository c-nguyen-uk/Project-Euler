# -*- coding: utf-8 -*-
"""
Problem 17: Number letter counts
https://projecteuler.net/problem=17

If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred
and forty-two) contains 23 letters and 115 (one hundred and fifteen)
contains 20 letters. The use of "and" when writing out numbers is in
compliance with British usage.
"""
import timeit

# This problem can also be solved by hand.
# We focus on a more code-centric solution here.


# The below are dictionaries of all relevant digits.

units = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
         "6": "six", "7": "seven", "8": "eight", "9": "nine"}
elevens = {"11": "eleven", "12": "twelve", "13": "thirteen", "14": "fourteen",
            "15": "fifteen", "16": "sixteen", "17": "seventeen",
            "18": "eighteen", "19": "nineteen"}
tens = {"20": "twenty", "30": "thirty", "40": "forty", "50": "fifty",
        "60": "sixty", "70": "seventy", "80": "eighty", "90": "ninety"}

# This function converts any integer from 1 to 1000 into text.
# This can be generalised for greater ranges using similar logic. It is
# possible to refactor this code to avoid repeated logic, but one needs
# to be careful to deal with any indexing issues.

def number_to_text(n):
    n = str(n)
    word = ""
    if len(n) == 1:  # Does 1-9
        word += units[n[-1]]
    if len(n) == 2:
        if n[-2] == "1" and n[-1] == "0":  # Does 10
            word += "ten"
        elif n[-2] == "1" and n[-1] != "0":  # Does 11-19
            word += elevens[n[-2:]]
        if n[-2] != "1" and n[-1] != "0":  # Does 21-99 not ending in 0
            word += tens[n[-2] + "0"] + "-" + units[n[-1]]
        elif n[-2] != "1" and n[-1] == "0":  # Does 20-90 ending in 0
            word += tens[n[-2:]]
    if len(n) == 3:
        if n[-2] == "0" and n[-1] == "0":  # Does 100-900 ending in 00
            word += units[n[-3]] + " hundred"
        elif n[-2] != "0" or n[-3] != "0":
            word += units[n[0]] + " hundred and "
            if n[-2] == "1" and n[-1] != "0":  # Does 101-999 ending in 11-19
                word += elevens[n[-2:]]
            elif n[-2] == "1" and n[-1] == "0":  # Does 101-999 ending in 10
                word += "ten"
            if n[-2] != "1" and n[-2] != "0" and n[-1] != "0":
                word += tens[n[-2] + "0"] + "-" + units[n[-1]]
            elif n[-2] != "1" and n[-2] != "0" and n[-1] == "0":
                word += tens[n[-2:]]
            elif n[-2] != "1" and n[-2] == "0":
                word += units[n[-1]]
    if len(n) == 4:
        word += "one thousand"
    return word.title()

# Printing the solution and ensuring that it completes within 1 minute.

start = timeit.default_timer()
print(sum([len(number_to_text(i).replace(" ", "").replace("-", ""))
           for i in range(1, 1001)]))
stop = timeit.default_timer()
print("Time:", stop - start)
