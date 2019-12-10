"""
https://adventofcode.com/2019/day/10

test: (11, 13), 210 asteroids

solution: for every asteroid compute all angles to horizontal line other asteroids make with it and
count different angles.
"""
import numpy as np
from math import atan2, sin, cos
from collections import defaultdict


def normalize(point_a, point_b):
    x, y = point_b[0] - point_a[0], point_b[1] - point_a[1]
    length = np.sqrt(x**2 + y**2)
    return round(x / length, 5), round(y / length, 5), length


def count_visible_asteroids(asteroid, all_asteroids):
    return len({normalize(asteroid, a)[:2] for a in all_asteroids if a != asteroid})


def find_best_asteroid(asteroids):
    return max(((a, count_visible_asteroids(a, asteroids)) for a in asteroids), key=lambda x: x[1])


def atan_spec(y, x):
    temp = atan2(y, x)
    if temp < atan2(-1, 0):
        temp += 2 * atan2(0, -1)
    return temp


def restore_coordinates(angle, length, center):
    x = int(round(cos(angle) * length))
    y = int(round(sin(angle) * length))
    return x + center[0], y + center[1]


def group_by_visibility(center, asteroids):
    result = defaultdict(list)
    for a in asteroids:
        if a != center:
            cos, sin, length = normalize(center, a)
            angle = atan_spec(sin, cos)
            result[angle].append(length)
    for k in result.keys():
        result[k] = sorted(result[k])
    return result


def order_by_laser(aster_dict):
    killed_asteroids = []
    sorted_keys = sorted(aster_dict.keys())
    while aster_dict:
        for key in sorted_keys:
            if key in aster_dict:
                killed_asteroids.append((key, aster_dict[key][0]))
                if len(aster_dict[key]) == 1:
                    del aster_dict[key]
                else:
                    aster_dict[key] = aster_dict[key][1:]
    return killed_asteroids


def read_input(file):
    coords = []
    with open(file) as f:
        for (i, line) in enumerate(f):
            for j, point in enumerate(line):
                if point == '#':
                    coords.append((j, i))
    return coords


if __name__ == "__main__":
    asteroids = read_input("../data/day_10.txt")
    center, n_visible = find_best_asteroid(asteroids)
    print(center, n_visible)
    killed_order = order_by_laser(group_by_visibility(center, asteroids))
    print(restore_coordinates(*killed_order[199], center))
