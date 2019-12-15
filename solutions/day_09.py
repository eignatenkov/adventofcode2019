"""
https://adventofcode.com/2019/day/9
"""

from solutions.day_05 import IntCode
from copy import copy


if __name__ == "__main__":
    ic = IntCode()
    ic.read_program_from_file("../data/day_09.txt")
    ic.apply_itself(1)
    ic.read_program_from_file("../data/day_09.txt")
    ic.apply_itself(2)
    print(ic.output)
