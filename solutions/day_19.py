from solutions.day_05 import IntCode
from copy import copy


def check_row(y, x_start, x_end, program):
    real_start = -1
    real_end = -1
    x_cur = x_start
    for i in range(10):
        ic = IntCode(copy(program), input=[x_cur, y])
        if ic.get_next_output():
            real_start = x_cur
            break
        x_cur += 1
    x_cur = max(real_start, x_end)
    for i in range(10):
        ic = IntCode(copy(program), input=[x_cur, y])
        if not ic.get_next_output():
            break
        else:
            real_end = x_cur
            x_cur += 1
    return real_start, real_end


def square_fits(beam_stats, size=100):
    last_line = beam_stats[-1]
    if last_line[1] - last_line[0] + 1 >= size:
        first_line = len(beam_stats) - size
        if beam_stats[first_line][1] >= last_line[0] + size - 1:
            return last_line[0] * 10000 + first_line
    return None


if __name__ == "__main__":
    program = IntCode.read_program(("../data/day_19.txt"))
    beam_counter = 0
    for i in range(50):
        for j in range(50):
            ic = IntCode(copy(program), input=[i, j])
            if ic.get_next_output() == 1:
                beam_counter += 1
    print(beam_counter)

    beam_dots = []
    y_cur = 0
    while True:
        if beam_dots and beam_dots[-1]:
            x_start = max(beam_dots[-1][0], 0)
            x_end = max(beam_dots[-1][-1], 0)
        else:
            x_start = 0
            x_end = 0
        beam_dots.append(check_row(y_cur, x_start, x_end, program))
        if square_fits(beam_dots) is not None:
            print(square_fits(beam_dots))
            break
        y_cur += 1
