"""
https://adventofcode.com/2019/day/15
"""
from solutions.day_05 import IntCode
from random import choice


class Robot(IntCode):
    def __init__(self):
        super().__init__(self)

    def move(self, direction):
        self._set_input(direction)
        return self.get_next_output()


def one_move(current_point, direction):
    if direction == 1:
        return current_point[0], current_point[1] + 1
    elif direction == 2:
        return current_point[0], current_point[1] - 1
    elif direction == 3:
        return current_point[0] - 1, current_point[1]
    else:
        return current_point[0] + 1, current_point[1]


def available_directions(maze_map, point):
    smart_choices = [d for d in range(1, 5) if one_move(point, d) not in maze_map]
    if smart_choices:
        return smart_choices
    else:
        return [d for d in range(1, 5) if maze_map.get(one_move(point, d), 1) != 0]


def print_map(explored_map):
    mapping = {
        0: '#',
        1: '.',
        2: '!',
        3: 'S',
        4: '*'
    }
    map_keys = set(explored_map.keys())
    min_x = min(map_keys, key=lambda x: x[0])[0]
    max_x = max(map_keys, key=lambda x: x[0])[0]
    min_y = min(map_keys, key=lambda x: x[1])[1]
    max_y = max(map_keys, key=lambda x: x[1])[1]
    printed_map = [['?']*(max_x - min_x + 1) for _ in range(max_y - min_y +1)]
    for point, color in explored_map.items():
        printed_map[point[1] - min_y][point[0] - min_x] = mapping[color]

    for row in printed_map:
        print(''.join(row))


def explore(robot, n_iterations=1000):
    explored_map = dict()
    current_point = (0, 0)
    explored_map[current_point] = 3
    for i in range(n_iterations):
        ad = available_directions(explored_map, current_point)
        if not ad:
            print(current_point)
            explored_map[current_point] = 4
            print_map(explored_map)
        direction = choice(ad)
        point_type = robot.move(direction)
        checked_point = one_move(current_point, direction)
        # print(current_point, checked_point, point_type)
        if checked_point not in explored_map:
            explored_map[checked_point] = point_type
        if point_type == 2:
            return explored_map
        if point_type == 1:
            current_point = checked_point

    return explored_map


if __name__ == "__main__":
    robot = Robot()
    robot.read_program_from_file("../data/day_15.txt")
    exp_map = explore(robot, 10000)
    print_map(exp_map)
