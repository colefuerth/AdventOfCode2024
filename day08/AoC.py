#!/usr/bin/python3

import sys
from itertools import product, permutations
from copy import deepcopy
import re
from typing import List, Tuple
from collections import defaultdict


def add(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int, int]:
    return (a[0] + b[0], a[1] + b[1])
def sub(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int, int]:
    return (a[0] - b[0], a[1] - b[1])
def is_valid_coord(coord: Tuple[int, int], f: List[str]):
    return 0 <= coord[0] < len(f) and 0 <= coord[1] < len(f[0])


def part1(f: List[str]) -> int:
    antennas = defaultdict(list)
    for x, y in product(range(len(f)), range(len(f[0]))):
        if f[x][y] != '.':
            antennas[f[x][y]].append((x, y))
    antinodes = set()
    for positions in antennas.values():
        for a, b in permutations(positions, r=2):
            antinode = add(a, sub(a, b))
            if is_valid_coord(antinode, f):
                antinodes.add(antinode)
    return len(antinodes)


def part2(f: List[str]) -> int:
    antennas = defaultdict(list)
    for x, y in product(range(len(f)), range(len(f[0]))):
        if f[x][y] != '.':
            antennas[f[x][y]].append((x, y))
    antinodes = set()
    for positions in antennas.values():
        for a, b in permutations(positions, r=2):
            diff = sub(a, b)
            while is_valid_coord(a, f):
                antinodes.add(a)
                a = add(a, diff)
    return len(antinodes)


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [l.strip() for l in open(fname, 'r').readlines()]

    print('Part 1:', part1(deepcopy(f)))
    print('Part 2:', part2(deepcopy(f)))
