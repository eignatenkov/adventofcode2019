"""
https://adventofcode.com/2019/day/5
"""
from copy import copy


class IntCode:
    def __init__(self, program, input=None):
        self.program = program
        self.memory = []
        self.pointer = 0
        if isinstance(input, int):
            input = [input]
        self.input = (i for i in input) if input else None
        self.output = []
        self.relative_base = 0

    def _read(self, index):
        if index < len(self.program):
            return self.program[index]
        else:
            mem_index = index - len(self.program)
            if mem_index >= len(self.memory):
                self.memory += [0] * (mem_index - len(self.memory) + 1)
            return self.memory[mem_index]

    def _write(self, index, value):
        if index < len(self.program):
            self.program[index] = value
        else:
            mem_index = index - len(self.program)
            if mem_index >= len(self.memory):
                self.memory += [0] * (mem_index - len(self.memory) + 1)
            self.memory[mem_index] = value

    def _get_value(self, parameter, mode):
        if mode == 0:
            return self._read(parameter)
        elif mode == 1:
            return parameter
        elif mode == 2:
            return self._read(self.relative_base + parameter)
        else:
            raise Exception(f"unknown parameter mode {mode}")

    def _write_value(self, parameter, mode, value):
        if mode == 0:
            index = parameter
        elif mode == 2:
            index = self.relative_base + parameter
        self._write(index, value)

    def apply_instruction(self):
        instruction = str(self.program[self.pointer])
        opcode = int(instruction[-2:])
        parameter_modes = instruction[:-2]
        if opcode in [1, 2]:
            parameter_modes = parameter_modes.zfill(3)[::-1]
            a, b = [self._get_value(x, int(p)) for x, p in zip(self.program[self.pointer + 1: self.pointer + 3],
                                                               parameter_modes[:2])]
            result = a + b if opcode == 1 else a * b
            self._write_value(self.program[self.pointer + 3], int(parameter_modes[-1]), result)
            self.pointer += 4
        elif opcode in [3, 4]:
            if opcode == 3:
                parameter_mode = int(parameter_modes.zfill(1))
                self._write_value(self.program[self.pointer + 1], parameter_mode, next(self.input))
            else:
                parameter_mode = int(parameter_modes.zfill(1))
                parameter = self._get_value(self.program[self.pointer + 1], parameter_mode)
                self.output.append(parameter)
            self.pointer += 2
            if opcode == 4:
                return 100
        elif opcode in [5, 6]:
            parameter_modes = parameter_modes.zfill(2)[::-1]
            a, b = [self._get_value(x, int(p)) for x, p in zip(self.program[self.pointer + 1: self.pointer + 3],
                                                               parameter_modes[:2])]
            if opcode == 5 and a != 0 or opcode == 6 and a == 0:
                self.pointer = b
            else:
                self.pointer += 3
        elif opcode in [7, 8]:
            parameter_modes = parameter_modes.zfill(3)[::-1]
            a, b = [self._get_value(x, int(p)) for x, p in zip(self.program[self.pointer + 1: self.pointer + 3],
                                                               parameter_modes[:2])]
            result = 1 if opcode == 7 and a < b or opcode == 8 and a == b else 0
            self._write_value(self.program[self.pointer + 3], int(parameter_modes[-1]), result)
            self.pointer += 4
        elif opcode == 9:
            parameter_mode = int(parameter_modes.zfill(1))
            parameter = self._get_value(self.program[self.pointer + 1], parameter_mode)
            self.relative_base += parameter
            self.pointer += 2
        elif opcode == 99:
            self.pointer += 1
            return 200
        else:
            raise Exception(f"unknown code {opcode}")

    def apply_itself(self):
        while self.pointer < len(self.program):
            a = self.apply_instruction()
            if a == 200:
                return

    def get_next_output(self):
        while self.pointer < len(self.program):
            a = self.apply_instruction()
            if a == 100:
                return self.output[-1]


if __name__ == "__main__":
    with open("../data/day_05.txt") as f:
        program = [int(x) for x in f.readline().split(',')]
    ic = IntCode(copy(program), 1)
    ic.apply_itself()
    print(ic.output[-1])
    print('----------')
    ic = IntCode(copy(program), 5)
    ic.apply_itself()
    print(ic.output[-1])
