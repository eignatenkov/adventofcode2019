"""
https://adventofcode.com/2019/day/22
"""
from tqdm import trange


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


def process_command(stack, command, value):
    if command == 1:
        return reverse_stack(stack)
    elif command == 2:
        return cut(stack, value)
    else:
        return deal_with_increment(stack, value)


def apply_commands_to_stack(stack, commands):
    for command in commands:
        stack = process_command(stack, *command)
    return stack


def apply_commands_to_position(position, size, commands):
    for command in commands:
        if command[0] == 1:
            position = size - 1 - position
        elif command[0] == 2:
            position = (position - command[1]) % size
        else:
            position = (position * command[1]) % size
    return position


def residual_div(a, b, mod):
    while True:
        if a % b == 0:
            return int(a / b)
        else:
            a += mod


def rewind_from_position(position, size, commands):
    for command in commands[::-1]:
        if command[0] == 1:
            position == size - 1 - position
        elif command[0] == 2:
            position = (position + command[1]) % size
        else:
            position = residual_div(position, command[1], size)
    return position


def compute_orbit(position, size, commands, limit=None):
    orbit = [position]
    current_place = position
    while True:
        if limit and len(orbit) == limit:
            return orbit
        current_place = apply_commands_to_position(current_place, size, commands)
        if orbit[0] == current_place:
            return orbit
        else:
            orbit.append(current_place)


if __name__ == "__main__":
    commands = read_input("../data/day_22.txt")
    init_stack = list(range(10007))
    new_stack = apply_commands_to_stack(init_stack, commands)
    print(new_stack.index(2019))
    big_stack_size = 119315717514047
    cur_pos = 2020
    for i in trange(101741582076661):
        cur_pos = rewind_from_position(cur_pos, big_stack_size, commands)
        if cur_pos == 2020:
            print(i)
            break
    # the_orbit = compute_orbit(2020, big_stack_size, commands, limit=100)
    # print(the_orbit)
