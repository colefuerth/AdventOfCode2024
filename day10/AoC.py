#!/usr/bin/python3

import sys
from itertools import product
from copy import deepcopy
from typing import List, Tuple, Set

N = (-1, 0)
E = (0, 1)
S = (1, 0)
W = (0, -1)
DIRS = [N,E,S,W]

def add(a: Tuple[int], b: Tuple[int]) -> Tuple[int]:
    return tuple(x + y for x, y in zip(a, b))

def is_valid_coord(coord: Tuple[int], f: Tuple[str]):
    return 0 <= coord[0] < len(f) and 0 <= coord[1] < len(f[0])

def part1(f: List[List[int]]) -> int:
    trailheads = [(x, y) for x, y in product(range(len(f)), range(len(f[0]))) if f[x][y] == 0]
    def explore_trail(trail: Tuple[int, int]) -> Set[Tuple[int, int]]:
        x, y = trail
        if f[x][y] == 9:
            return {trail}
        found = set()
        for coord in [add(trail, d) for d in DIRS]:
            if is_valid_coord(coord, f) and f[coord[0]][coord[1]] - f[x][y] == 1:
                found.update(explore_trail(coord))
        return found
    return sum(len(explore_trail(trailhead)) for trailhead in trailheads)

def part2(f: List[List[int]]) -> int:
    trailheads = [(x, y) for x, y in product(range(len(f)), range(len(f[0]))) if f[x][y] == 0]
    def explore_trail(trail: Tuple[int, int]) -> int:
        x, y = trail
        if f[x][y] == 9:
            return 1
        return sum(explore_trail(coord) for coord in [add(trail, d) for d in DIRS] if is_valid_coord(coord, f) and f[coord[0]][coord[1]] - f[x][y] == 1)
    return sum(explore_trail(trailhead) for trailhead in trailheads)

if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [
        [int(c) for c in l.strip()]
        for l in open(fname, 'r').readlines()
    ]

    print('Part 1:', part1(deepcopy(f)))
    print('Part 2:', part2(deepcopy(f)))
