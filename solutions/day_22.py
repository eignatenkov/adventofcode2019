"""
https://adventofcode.com/2019/day/22
"""


def read_input(file_path):
    commands = []
    with open(file_path) as f:
        for line in f:
            line = line.strip()
            if line.startswith('cut'):
                value = int(line.split(' ')[-1])
                command = (2, value)
            else:
                line_split = line.split(' ')
                if line_split[1] == 'into':
                    command = (1, 0)
                else:
                    command = (3, int(line_split[-1]))
            commands.append((command))
    return commands


def reverse_stack(stack):
    return stack[::-1]


def cut(stack, n):
    return stack[n:] + stack[:n]


def deal_with_increment(stack, increment):
    new_stack = [0] * len(stack)
    position = 0
    for card in stack:
        new_stack[position] = card
        position = (position + increment) % len(stack)
    return new_stack


if __name__ == "__main__":
    commands = read_input("../data/day_22.txt")
    print(commands)
    test_stack = list(range(10))
    print(cut(test_stack, -4))
    print(reverse_stack(test_stack))
    print(deal_with_increment(test_stack, 3))
