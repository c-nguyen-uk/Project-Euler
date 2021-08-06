# -*- coding: utf-8 -*-
"""Single decorator function to be called in all Project Euler solutions."""
import timeit


def computation_time(solution_function):
    """Decorate a Project Euler solution with the computation time taken."""
    def wrapper(*args):
        start = timeit.default_timer()
        solution = solution_function(*args)
        stop = timeit.default_timer()
        time_taken = round(stop - start, 3)
        return f"Solution: {solution}\nTime: {time_taken} seconds"
    return wrapper
