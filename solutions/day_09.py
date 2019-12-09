"""
https://adventofcode.com/2019/day/9
"""

from solutions.day_05 import IntCode
from copy import copy


if __name__ == "__main__":
    with open("../data/day_09.txt") as f:
        program = [int(i) for i in f.readline().strip().split(',')]

    ic = IntCode(copy(program), 1)
    ic.apply_itself()
    print(ic.output)

    ic = IntCode(copy(program), 2)
    ic.apply_itself()
    print(ic.output)
