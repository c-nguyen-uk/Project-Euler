# -*- coding: utf-8 -*-
"""Problem 67: Maximum path sum II

https://projecteuler.net/problem=67

By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt, a 15K text
file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not
possible to try every route to solve this problem, as there are 2^99
altogether! If you could check one trillion (10^12) routes every second
it would take over twenty billion years to check them all. There is an
efficient algorithm to solve it.
"""
from custom_timer import computation_time


def triangle_string():
    """Return the problem triangle, formatted, from triangle.txt."""
    with open("Problem67_triangle.txt") as triangle_txt:
        return triangle_txt.read().replace(" ", "").replace("\n", "")


PROBLEM_TRIANGLE = triangle_string()


def row(n):
    """Return the nth row of PROBLEM_TRIANGLE as a list."""
    return [int(PROBLEM_TRIANGLE[i: i + 2])
            for i in range(n*(n + 1), (n + 2)*(n + 1) - 1, 2)]


def problem_matrix():
    """Convert PROBLEM_TRIANGLE into a matrix.

    Calling problem_matrix()[i][j] returns the ith row, jth column entry.
    """
    matrix_list = []
    for i in range(100):
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
