"""
https://adventofcode.com/2019/day/6
"""
from collections import defaultdict


def read_input(filename):
    children_dict = defaultdict(set)
    with open(filename) as f:
        for line in f:
            parent, child = line.strip().split(')')
            children_dict[parent].add(child)
    return children_dict


def children_to_parent(children_dict):
    parent_dict = dict()
    for k, v in children_dict.items():
        if k not in parent_dict:
            parent_dict[k] = None
        for item in v:
            parent_dict[item] = k
    return parent_dict


def length_to_root(parent_dict, key):
    length = 0
    current_key = key
    while True:
        if parent_dict[current_key]:
            length += 1
            current_key = parent_dict[current_key]
        else:
            return length


def path_to_root(parent_dict, key):
    path = []
    current_key = key
    while current_key in parent_dict:
        path.append(current_key)
        current_key = parent_dict[current_key]
    return path


def count_all_length(parent_dict):
    total = 0
    for k in parent_dict.keys():
        total += length_to_root(parent_dict, k)
    return total


def distance(parent_dict, a, b):
    a_path = path_to_root(parent_dict, a)
    b_path = path_to_root(parent_dict, b)
    b_set = set(b_path)
    for i, planet in enumerate(a_path):
        if planet in b_set:
            return i + b_path.index(planet)


if __name__ == '__main__':
    cd = read_input('../data/day_06.txt')
    pd = children_to_parent(cd)
    print(count_all_length(pd))
    me_object = pd['YOU']
    santa_object = pd['SAN']
    print(distance(pd, me_object, santa_object))
