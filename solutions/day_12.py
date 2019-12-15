"""
https://adventofcode.com/2019/day/12
"""
from typing import List
from itertools import combinations


def cmp(a, b):
    if a > b:
        return -1
    elif a < b:
        return 1
    else:
        return 0


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def sum_abs(self):
        return abs(self.x) + abs(self.y) + abs(self.z)


class Moon:
    def __init__(self, position: Point, velocity: Point = Point(0, 0, 0)):
        self.position = position
        self.velocity = velocity

    def __eq__(self, other):
        return self.position == other.position and self.velocity == other.velocity

    def __hash__(self):
        return hash(f"{self.position.x}{self.position.y}{self.position.z}{self.velocity.x}{self.velocity.y}{self.velocity.z}")

    def apply_gravity(self, other):
        change = Point(cmp(self.position.x, other.position.x),
                       cmp(self.position.y, other.position.y),
                       cmp(self.position.z, other.position.z))
        self.velocity = self.velocity + change

    def apply_velocity(self):
        self.position = self.position + self.velocity

    def total_energy(self):
        return self.position.sum_abs() * self.velocity.sum_abs()


class MoonSystem:
    def __init__(self, moons: List[Moon] = None):
        self.moons = moons if moons else []

    def from_file(self, filename):
        with open(filename) as f:
            for line in f:
                coords = [int(x[2:]) for x in line.strip(' \n<>').split(', ')]
                self.moons.append(Moon(position=Point(*coords)))

    def apply_gravity(self):
        for moon_one, moon_two in combinations(self.moons, 2):
            moon_one.apply_gravity(moon_two)
            moon_two.apply_gravity(moon_one)

    def apply_velocity(self):
        for moon in self.moons:
            moon.apply_velocity()

    def simulate(self):
        self.apply_gravity()
        self.apply_velocity()

    def total_energy(self):
        return sum(moon.total_energy() for moon in self.moons)

    def track_states(self):
        moon_states = [{moon} for moon in self.moons]
        moon_cycles = [0 for _ in self.moons]
        counter = 0
        while True:
            self.simulate()
            counter += 1
            for (i, moon) in enumerate(self.moons):
                if moon not in moon_states[i]:
                    moon_states[i].add(moon)
                else:
                    moon_cycles[i] = counter
                    if all(x != 0 for x in moon_cycles):
                        return moon_cycles


if __name__ == "__main__":
    moons = MoonSystem()
    moons.from_file("../data/day_12.txt")
    for _ in range(1000):
        moons.simulate()
    print(moons.total_energy())
    moons = MoonSystem()
    moons.from_file("../data/day_12_test.txt")
    print(moons.track_states())
