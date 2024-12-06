#!/usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy
import re
from typing import List, Tuple, Dict


W = (0, -1)    # left
E = (0, 1)     # right
N = (-1, 0)    # up
S = (1, 0)     # down
NW = (-1, -1)  # top left
NE = (-1, 1)   # top right
SW = (1, -1)   # bottom left
SE = (1, 1)     # bottom right
DIRECTIONS = (N, E, S, W, NE, NW, SE, SW)


def add(a: Tuple[int], b: Tuple[int]) -> Tuple[int]:
    return tuple(x + y for x, y in zip(a, b))


def is_valid_coord(coord: Tuple[int], ws: Tuple[str]):
    return 0 <= coord[0] < len(ws) and 0 <= coord[1] < len(ws[0])


def find_xmas_from(pos: Tuple[int, int], char: str, ws: Tuple[str], dir: Tuple[int, int] = None) -> int:
    if char == '':
        return 1
    if not is_valid_coord(pos, ws) or ws[pos[0]][pos[1]] != char[0]:
        return 0
    if dir is None:
        ret = 0
        for d in DIRECTIONS:
            ret += find_xmas_from(add(pos, d), char[1:], ws, d)
        return ret
    return find_xmas_from(add(pos, dir), char[1:], ws, dir)


def part1(f: List[str]) -> int:
    return sum(
        find_xmas_from((x, y), 'XMAS', f)
        for x, y in product(range(len(f)), range(len(f[0])))
    )


def part2(f: List[str]) -> int:
    ret = 0
    for c in product(range(1, len(f) - 1), range(1, len(f[0]) - 1)):
        if f[c[0]][c[1]] == 'A':
            corners = [[f[c[0] + NE[0]][c[1] + NE[1]], f[c[0] + SW[0]][c[1] + SW[1]]], [f[c[0] + NW[0]][c[1] + NW[1]], f[c[0] + SE[0]][c[1] + SE[1]]]]
            ret += all(pair.count('S') == 1 and pair.count('M') == 1 for pair in corners)
    return ret


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [
        l.strip()
        for l in open(fname, 'r').readlines()
    ]

    print('Part 1:', part1(deepcopy(f)))
    print('Part 2:', part2(deepcopy(f)))
