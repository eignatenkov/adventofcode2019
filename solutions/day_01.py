"""
Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module,
take its mass, divide by three, round down, and subtract 2.

For example:

For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
For a mass of 1969, the fuel required is 654.
For a mass of 100756, the fuel required is 33583.
The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel
needed for the mass of each module (your puzzle input), then add together all the fuel values.

What is the sum of the fuel requirements for all of the modules on your spacecraft?
"""


def find_fuel_for_module(module_mass):
    return max(module_mass // 3 - 2, 0)


assert find_fuel_for_module(12) == 2
assert find_fuel_for_module(14) == 2
assert find_fuel_for_module(1969) == 654
assert find_fuel_for_module(100756) == 33583


def find_total_fuel_for_module(module_mass):
    total_fuel = 0
    current_weight = module_mass
    while True:
        new_fuel = find_fuel_for_module(current_weight)
        if new_fuel == 0:
            return total_fuel
        else:
            total_fuel += new_fuel
            current_weight = new_fuel


assert find_total_fuel_for_module(14) == 2
assert find_total_fuel_for_module(1969) == 966
assert find_total_fuel_for_module(100756) == 50346


def solution(input_file, function):
    total_fuel = 0
    with open(input_file) as f:
        for line in f:
            total_fuel += function(int(line))
    return total_fuel


if __name__ == "__main__":
    print(solution("../data/day_01.txt", find_fuel_for_module))
    print(solution("../data/day_01.txt", find_total_fuel_for_module))

