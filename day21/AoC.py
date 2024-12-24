#!/usr/bin/python3

import re
import sys
from copy import deepcopy
from typing import List, Tuple
from itertools import product, pairwise
from functools import cache

N = (-1, 0)
E = (0, 1)
S = (1, 0)
W = (0, -1)
DIRS = [N, E, S, W]


def add(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int]:
    return (a[0] + b[0], a[1] + b[1])

@cache
def find_in_cartesian_plane(char: str, f: Tuple[str]):
    return next((x, y) for x, y in product(range(len(f)), range(len(f[0]))) if f[x][y] == char)

# this guy is the problem
# sometimes we are at the > arrow and go to < instead of v first when we dont need to
# we need to create a check first to see if doing the optimal layout is valid and if not then pick the correct
@cache
def move_from(a: str, b: str, d: Tuple[str]) -> int:
    a = find_in_cartesian_plane(a, d)
    b = find_in_cartesian_plane(b, d)
    v, h = b[0] - a[0], b[1] - a[1]
    return (('>' * h) if h > 0 else '') \
         + (('^' * -v) if v < 0 else '') \
         + (('v' * v) if v > 0 else '') \
         + (('<' * -h) if h < 0 else '') \
         + 'A'

# @cache
def type_into_keypad(s: str, keypad: Tuple[str] = (" ^A", "<v>")) -> str:
    return ''.join(move_from(a, b, keypad) for a, b in pairwise('A' + s))
    # res = []
    # for a, b in zip('A' + s, s):
    #     res.append(move_from(a, b, keypad))
    # return ''.join(res)


def part1(f: List[str]) -> int:
    # return sum(int(l[:-1]) * len(type_into_keypad(type_into_keypad(type_into_keypad(l, keypad=("789", "456", "123", " 0A"))))) for l in f)
    print(type_into_keypad(type_into_keypad(type_into_keypad("379A", keypad=("789", "456", "123", " 0A")))))
    print(type_into_keypad(type_into_keypad("379A", keypad=("789", "456", "123", " 0A"))))
    print(type_into_keypad("379A", keypad=("789", "456", "123", " 0A")))
    print("379A")
    s = 0
    for l in f:
        x = int(l[:-1])
        l = len(type_into_keypad(type_into_keypad(type_into_keypad(l, keypad=("789", "456", "123", " 0A")))))
        print(f'{l} * {x}')
        s += x * l

def part2(f: List[str]) -> int:
    pass


if __name__ == "__main__":
    fname = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    f = [l.strip() for l in open(fname, "r").readlines()]

    print("Part 1:", part1(deepcopy(f)))
    print("Part 2:", part2(deepcopy(f)))
