"""
https://adventofcode.com/2019/day/11
"""

from solutions.day_05 import IntCode
import numpy as np


if __name__ == "__main__":
    robot = IntCode()
    robot.read_program_from_file("../data/day_11.txt")
    painted_points = set()
    white_points = set()
    current_point = (0, 0)
    current_direction = np.pi / 2
    counter = 0
    while True:
        inp = int(current_point in white_points)
        try:
            robot._set_input(inp)
            # print(f"passed input {inp}")
            to_color = robot.get_next_output()
            # print(f"painting this point into color {to_color}")
            direction = robot.get_next_output()
            # print(f"moving in the direction {direction}")
            painted_points.add(current_point)
            if to_color:
                white_points.add(current_point)
            else:
                if current_point in white_points:
                    white_points.remove(current_point)
            current_direction += np.pi / 2 if not direction else - np.pi / 2
            current_point = (current_point[0] + int(round(np.cos(current_direction))),
                             current_point[1] + int(round(np.sin(current_direction))))
            # print(f"coming into the point {current_point}")
            counter += 1
            if 10000 <= counter <= 10020:
                print(current_point)
        except StopIteration:
            break
    print(len(painted_points))

