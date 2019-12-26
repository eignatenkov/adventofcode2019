import pytest

from solutions.day_22 import apply_commands_to_position, apply_commands_to_stack, compute_orbit, read_input, \
    residual_div, rewind_from_position


def test_apply_commands_to_position():
    assert apply_commands_to_position(0, 10, [(1, 0)]) == 9
    assert apply_commands_to_position(0, 10, [(2, 3)]) == 7
    assert apply_commands_to_position(9, 10, [(2, 3)]) == 6
    assert apply_commands_to_position(0, 10, [(1, 0), (2, 3)]) == 6
    assert apply_commands_to_position(4, 10007, [(3, 4)]) == 16
    assert apply_commands_to_position(0, 10007, [(3, 4)]) == 0


def test_position_vs_stack():
    test_commands = [[(3, 7), (1, 0), (1, 0)], [(2, 6), (3, 7), (1, 0)], [(3, 7), (3, 9), (2, -2)],
                     [(1, 0), (2, -2), (3, 7), (2, 8), (2, -4), (3, 7), (2, 3), (3, 9), (3, 3), (2, -1)]]
    init_stack = list(range(10))
    for commands in test_commands:
        stack_after = apply_commands_to_stack(init_stack, commands)
        for i in range(10):
            assert stack_after.index(i) == apply_commands_to_position(i, 10, commands)


def test_compute_orbit():
    commands = [(3, 7), (1, 0), (1, 0)]
    assert set(compute_orbit(1, 10, commands)) == {1, 3, 9, 7}
    assert set(compute_orbit(0, 10, commands)) == {0}
    assert set(compute_orbit(5, 10, commands)) == {5}
    assert set(compute_orbit(2, 10, commands)) == {2, 4, 6, 8}


def test_big():
    commands = read_input("../data/day_22.txt")
    init_stack = list(range(10007))
    stack_after = apply_commands_to_stack(init_stack, commands)
    for i in range(10007):
        assert (i, stack_after.index(i)) == (i, apply_commands_to_position(i, 10007, commands))


def test_residual_div():
    assert residual_div(2, 3, 10) == 4
    assert residual_div(0, 3, 17) == 0


def test_rewind():
    commands = [(3, 7), (1, 0), (1, 0)]
    new_stack = [0, 3, 6, 9, 2, 5, 8, 1, 4, 7]
    for i in range(10):
        assert rewind_from_position(i, 10, commands) == new_stack[i]
