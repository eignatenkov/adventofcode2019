"""
https://adventofcode.com/2019/day/14
"""
from collections import Counter
from math import ceil


def read_input(filename):
    rules = dict()
    with open(filename) as f:
        for line in f:
            left, right = line.strip().split(' => ')
            lefts = left.split(', ')
            right = right.split(' ')
            right_amount = int(right[0])
            right_name = right[1]
            lefts_clean = []
            for lmn in lefts:
                lmn_amount, lmn_name = lmn.split(' ')
                lmn_amount = int(lmn_amount)
                lefts_clean.append((lmn_name, lmn_amount))
            rules[right_name] = (right_amount, lefts_clean)
    return rules


def calc_ore_for_fuel(rules):
    source_counter = Counter({'FUEL': 1})
    while set(source_counter.keys()) != {'ORE'}:
        print(source_counter)
        sc_keys = set(source_counter.keys()) - {'ORE'}
        for key in sc_keys:
            value = source_counter[key]
            amount, sources = rules[key]
            multiplier = ceil(value / amount)
            for source in sources:
                source_counter[source[0]] += source[1] * multiplier
            del source_counter[key]
    return source_counter['ORE']


if __name__ == "__main__":
    rules = read_input("../data/day_14_test_0.txt")
    print(calc_ore_for_fuel(rules))
