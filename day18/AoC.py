#!/usr/bin/python3

import sys
from typing import List, Tuple

N = (-1, 0)
E = (0, 1)
S = (1, 0)
W = (0, -1)
DIRS = [N, E, S, W]


def add(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int]:
    return (a[0] + b[0], a[1] + b[1])


def is_valid_coord(coord: Tuple[int], f: Tuple[str]):
    return 0 <= coord[0] < len(f) and 0 <= coord[1] < len(f[0])


def create_grid(f: List[List[int]]) -> List[List[str]]:
    max_x = max(f, key=lambda x: x[0])[0] + 1
    max_y = max(f, key=lambda x: x[1])[1] + 1
    grid = [(["."] * max_y) for _ in range(max_x)]
    for x, y in f[: (12 if len(f) == 25 else 1024)]:
        grid[x][y] = "#"
    return grid


def find_exit(grid: List[List[str]]) -> int:
    START = (0, 0)
    END = (len(grid) - 1, len(grid[0]) - 1)

    visited = set()
    queue = [[START]]
    while queue:
        nq = []
        for q in queue:
            pos = q[-1]
            if pos == END:
                return q
            for d in DIRS:
                npos = add(pos, d)
                if (
                    is_valid_coord(npos, grid)
                    and grid[npos[0]][npos[1]] != "#"
                    and npos not in visited
                ):
                    visited.add(npos)
                    nq.append(q + [npos])
        queue = nq
    return []


def part1(f: List[str]) -> int:
    grid = create_grid(f)
    return len(find_exit(grid))


def part2(f: List[str]) -> int:
    grid = create_grid(f)
    last_path = find_exit(grid)
    for bx, by in f[(12 if len(f) == 25 else 1024) :]:
        grid[bx][by] = "#"
        if (bx, by) in last_path:
            last_path = find_exit(grid)
            if not last_path:
                return f"{bx},{by}"


if __name__ == "__main__":
    fname = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    f = [[int(x) for x in l.strip().split(",")] for l in open(fname, "r").readlines()]

    print("Part 1:", part1(f))
    print("Part 2:", part2(f))
