"""
https://adventofcode.com/2019/day/13
"""

from solutions.day_05 import IntCode

arcade = IntCode()
arcade.read_program_from_file("../data/day_13.txt")
arcade.apply_itself()
print(sum(x == 2 for x in arcade.output[2::3]))