"""
https://adventofcode.com/2019/day/7
"""

from solutions.day_05 import IntCode
from copy import copy
from itertools import permutations


def one_loop(program, initial_input, phases):
    current_input = initial_input
    for p in phases:
        ic = IntCode(copy(program), [p, current_input])
        current_input = ic.get_next_output()
    return current_input


def loop_accus(program, phases):
    accus = [IntCode(copy(program)) for _ in phases]
    current_input = 0
    for (acc, p) in zip(accus, phases):
        acc.input = (x for x in [p, current_input])
        current_input = acc.get_next_output()
    result = copy(current_input)
    while True:
        for index, acc in enumerate(accus):
            try:
                acc.input = (x for x in [current_input])
                ci = acc.get_next_output()
                if ci is None:
                    return result
                elif index == len(phases) - 1:
                    result = ci
                current_input = ci
            except:
                return result


if __name__ == "__main__":
    with open('../data/day_07.txt') as f:
        program = [int(x) for x in f.readline().strip().split(',')]

    results = [one_loop(copy(program), 0, perm) for perm in permutations(range(5))]
    print(max(results))

    results = [loop_accus(copy(program), perm) for perm in permutations(range(5, 10))]
    print(max(results))
