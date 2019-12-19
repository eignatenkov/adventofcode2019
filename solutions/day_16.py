"""
https://adventofcode.com/2019/day/16
"""
import numpy as np


def string_to_array(string_of_digits):
    return np.array(list(map(int, list(string_of_digits)))).astype(np.int8)


def read_input(file_path, repeat=1):
    with open(file_path) as f:
        return string_to_array(repeat * f.read().strip())


def spread_pattern_to_size(pattern, size):
    multiplier = np.ceil((size + 1)/ pattern.size).astype('int')
    return np.tile(pattern, multiplier)[1:size + 1]


def apply_pattern(input_array, base_pattern=np.array([0, 1, 0, -1]).astype(np.int8)):
    ia_size = input_array.size
    result = np.zeros(ia_size)
    for i in range(ia_size):
        current_pattern = np.repeat(base_pattern, i + 1)
        spread_pattern = spread_pattern_to_size(current_pattern, ia_size)
        # print(spread_pattern, input_array, input_array.dot(spread_pattern))
        result[i] = np.abs(input_array.dot(spread_pattern)) % 10
    return result


if __name__ == "__main__":

    input_array = read_input("../data/day_16.txt")
    for _ in range(100):
        input_array = apply_pattern(input_array)
    print(''.join(map(str, input_array[:8].astype('int'))))

    offset = 5976697 # first 7 digits of the input
    second_input = read_input("../data/day_16.txt", repeat=10000)[offset:]
    for i in range(100):
        second_input = np.flip(np.cumsum(np.flip(second_input))) % 10
    print(''.join(map(str, second_input[:8])))
