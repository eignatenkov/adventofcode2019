"""
You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had
written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
How many different passwords within the range given in your puzzle input meet these criteria?

Your puzzle input is 240920-789857.
"""
from collections import Counter


def is_good(number):
    return int(''.join(sorted(str(number)))) == number and len(set(str(number))) < len(list(str(number)))


def is_supergood(number):
    ns = str(number)
    if int(''.join(sorted(ns))) != number:
        return False
    else:
        digits_counter = Counter()
        for d in ns:
            digits_counter[d] += 1
        return any(v == 2 for v in digits_counter.values())


if __name__ == "__main__":
    counter = 0
    supergood_counter = 0
    for i in range(240920, 789857 + 1):
        if is_good(i):
            counter += 1
            if is_supergood(i):
                supergood_counter += 1
    print(counter, supergood_counter)
