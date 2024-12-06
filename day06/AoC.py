#!/usr/bin/python3

import sys
from itertools import product
from copy import deepcopy
from typing import List, Tuple, Set


W = (0, -1)
E = (0, 1)
N = (-1, 0)
S = (1, 0)
TURNS = {
    N:E,
    E:S,
    S:W,
    W:N
}
def add(a: Tuple[int], b: Tuple[int]) -> Tuple[int]:
    return tuple(x + y for x, y in zip(a, b))
def is_valid_coord(coord: Tuple[int], ws: Tuple[str]):
    return 0 <= coord[0] < len(ws) and 0 <= coord[1] < len(ws[0])


def part1(f: List[str]) -> Set[Tuple[int, int]]:
    guard = None
    obstacles = set()
    visited = set()
    direction = N
    for x, y in product(range(len(f)), range(len(f[0]))):
        if f[x][y] == "^":
            guard = (x, y)
            visited.add(guard)
        elif f[x][y] == "#":
            obstacles.add((x, y))

    x, y = add(guard, direction)
    while is_valid_coord((x, y), f):
        while f[x][y] == "#":
            direction = TURNS[direction]
            x, y = add(guard, direction)
        guard = (x, y)
        visited.add(guard)
        x, y = add(guard, direction)
    return visited


def part2(f: List[str]) -> int:
    original_pos = None
    obstacles = set()
    loop_count = 0

    for x, y in product(range(len(f)), range(len(f[0]))):
        if f[x][y] == "^":
            original_pos = (x, y)
        elif f[x][y] == "#":
            obstacles.add((x, y))
    
    potential_new_obstacles = part1(f)
    potential_new_obstacles.remove(original_pos)

    for new_obstacle in potential_new_obstacles:
        obstacles.add(new_obstacle)

        guard = original_pos
        direction = N
        visited = set()
        visited.add((guard, direction))

        x, y = add(guard, direction)
        while is_valid_coord((x, y), f):
            while (x, y) in obstacles:
                direction = TURNS[direction]
                x, y = add(guard, direction)
            guard = (x, y)
            if (guard, direction) in visited:
                loop_count += 1
                break
            visited.add((guard, direction))
            x, y = add(guard, direction)
        
        obstacles.remove(new_obstacle)
    
    return loop_count


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [
        l.strip()
        for l in open(fname, 'r').readlines()
    ]

    print('Part 1:', len(part1(deepcopy(f))))
    print('Part 2:', part2(deepcopy(f)))
