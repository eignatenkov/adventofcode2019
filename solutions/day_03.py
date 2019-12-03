"""
https://adventofcode.com/2019/day/3
"""


def compute_instruction_points(start_point, instruction):
    direction = instruction[0]
    length = int(instruction[1:]) + 1
    if direction == 'D':
        return [(start_point[0], start_point[1] - i) for i in range(1, length)]
    elif direction == 'U':
        return [(start_point[0], start_point[1] + i) for i in range(1, length)]
    elif direction == 'L':
        return [(start_point[0] - i, start_point[1]) for i in range(1, length)]
    else:
        return [(start_point[0] + i, start_point[1]) for i in range(1, length)]


def compute_path_points(instructions):
    path_points = [(0, 0)]
    current_point = (0, 0)
    for instruction in instructions:
        instruction_points = compute_instruction_points(current_point, instruction)
        path_points += instruction_points
        current_point = instruction_points[-1]
    return path_points


def find_closest_to_zero_intersection(path_one, path_two):
    return min((abs(p[0]) + abs(p[1])) for p in (set(path_one) & set(path_two)) if p != (0, 0))


def find_closest_intersection_by_paths(path_one, path_two):
    path_one = path_one[1:]
    path_two = path_two[1:]
    for min_length in range(len(path_one) + len(path_two) - 1):
        for index_one in range(max(0, min_length - len(path_two) + 1),
                               min(min_length + 1, len(path_one))):
            index_two = min_length - index_one
            if path_one[index_one] == path_two[index_two]:
                return min_length + 2


def solution(input_path):
    with open(input_path) as f:
        inst_one, inst_two = [line.strip().split(',') for line in f]
    path_one = compute_path_points(inst_one)
    path_two = compute_path_points(inst_two)
    return find_closest_to_zero_intersection(path_one, path_two), \
           find_closest_intersection_by_paths(path_one, path_two)


if __name__ == "__main__":
    print(solution("../data/day_03.txt"))
