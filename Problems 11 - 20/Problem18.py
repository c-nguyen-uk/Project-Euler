# -*- coding: utf-8 -*-
"""Problem 18: Maximum path sum I

https://projecteuler.net/problem=18

By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below.

NOTE: As there are only 16384 routes, it is possible to solve this
problem by trying every route. However, Problem 67, is the same
challenge with a triangle containing one-hundred rows; it cannot be
solved by brute force, and requires a clever method!)
"""
from custom_timer import computation_time


PROBLEM_TRIANGLE = str("""
                            75
                          95 64
                        17 47 82
                      18 35 87 10
                    20 04 82 47 65
                  19 01 23 75 03 34
                88 02 77 73 07 63 67
              99 65 04 28 06 16 70 92
            41 41 26 56 83 40 80 70 33
          41 48 72 33 47 32 37 16 94 29
        53 71 44 65 25 43 91 52 97 51 14
      70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
  63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
""".replace(" ", "").replace("\n", ""))


def row(n):
    """Return the nth row of PROBLEM_TRIANGLE as a list."""
    return [int(PROBLEM_TRIANGLE[i: i + 2])
            for i in range(n*(n + 1), (n + 2)*(n + 1) - 1, 2)]


def problem_matrix():
    """Convert PROBLEM_TRIANGLE into a matrix.

    Calling problem_matrix()[i][j] returns the ith row, jth column entry.
    """
    matrix_list = []
    for i in range(15):
        matrix_list.append(row(i))
    return matrix_list


def adjacent_column_index_above(column_index, max_column_index):
    """Return a list of column indices which are adjacent in the above row."""
    if column_index == max_column_index:
        return [column_index - 1]  # Handle last column
    if not column_index:
        return [column_index]  # Handle the 0th column
    return [column_index, column_index - 1]


def row_addition(row_above, row_below):
    """Return a row where elements are the sum of the row and above element.

    In particular, the nth element of the returned row is the sum of the nth
    element in the given row and the adjacent element in the above row.  If
    there are two such adjacent elements, then the largest one is chosen.
    """
    returned_row = []
    max_column = len(row_below) - 1
    for column, row_element in enumerate(row_below):
        adjacent_elements_above = []
        for column_index in adjacent_column_index_above(column, max_column):
            adjacent_elements_above.append(row_above[column_index])
        max_adjacent = max(adjacent_elements_above)
        returned_row.append(row_element + max_adjacent)
    return returned_row


@computation_time
def solution():
    """Return the solution."""
    max_row = len(problem_matrix())
    row_above = problem_matrix()[0]
    for i in range(1, max_row):
        row_above = row_addition(row_above, problem_matrix()[i])
    return max(row_above)


print(solution())
