import pytest
from solutions.day_03 import compute_instruction_points, compute_path_points, \
    find_closest_to_zero_intersection, find_closest_intersection_by_paths


def test_compute_instruction_points():
    assert compute_instruction_points([0, 0], 'R2') == [(1, 0), (2, 0)]


def test_compute_path_points():
    assert compute_path_points(['R1', 'U1']) == [(0, 0), (1, 0), (1, 1)]


def test_find_closest_to_zero_intersection():
    instructions_one = "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(',')
    instructions_two = "U62,R66,U55,R34,D71,R55,D58,R83".split(',')
    assert find_closest_to_zero_intersection(compute_path_points(instructions_one),
                                             compute_path_points(instructions_two)) == 159
    instructions_three = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(',')
    instructions_four = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(',')
    assert find_closest_to_zero_intersection(compute_path_points(instructions_three),
                                             compute_path_points(instructions_four)) == 135


def test_find_closest_intersection_by_paths():
    inst_one = "R8,U5,L5,D3".split(',')
    inst_two = "U7,R6,D4,L4".split(',')
    path_one = compute_path_points(inst_one)
    path_two = compute_path_points(inst_two)
    assert find_closest_intersection_by_paths(path_one, path_two) == 30
    instructions_one = "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(',')
    instructions_two = "U62,R66,U55,R34,D71,R55,D58,R83".split(',')
    assert find_closest_intersection_by_paths(compute_path_points(instructions_one),
                                              compute_path_points(instructions_two)) == 610
    instructions_three = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(',')
    instructions_four = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(',')
    assert find_closest_intersection_by_paths(compute_path_points(instructions_three),
                                              compute_path_points(instructions_four)) == 410
