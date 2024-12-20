#!/usr/bin/python3

import sys
from itertools import product, combinations
from copy import deepcopy
from typing import List, Tuple, Dict

N = (-1, 0)
E = (0, 1)
S = (1, 0)
W = (0, -1)
DIRS = [N, E, S, W]


def add(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int]:
    return (a[0] + b[0], a[1] + b[1])


def find_in_cartesian_plane(f: List[List[any]], key: callable):
    return [(x, y) for x, y in product(range(len(f)), range(len(f[0]))) if key(f[x][y])]


def create_heatmap_from(source: Tuple[int, int], f: List[List[str]]) -> Dict[Tuple[int, int], int]:
    heatmap = {source: 0}
    queue = [source]
    while queue:
        pos = queue.pop(0)
        for d in DIRS:
            npos = add(pos, d)
            if f[npos[0]][npos[1]] != "#" and npos not in heatmap:
                heatmap[npos] = heatmap[pos] + 1
                queue.append(npos)
    return heatmap


def part1(f: List[List[str]]) -> int:
    START = find_in_cartesian_plane(f, lambda x: x == "S")[0]
    END = find_in_cartesian_plane(f, lambda x: x == "E")[0]
    TARGET_SAVINGS = 100

    hs = create_heatmap_from(START, f)
    he = create_heatmap_from(END, f)
    result = 0

    for x, y in [
        (x, y)
        for x, y in product(range(1, len(f) - 1), range(1, len(f[0]) - 1))
        if f[x][y] == "#"
    ]:
        adj = [(x + dx, y + dy) for dx, dy in DIRS if f[x + dx][y + dy] != "#"]
        if len(adj) >= 2:
            for a, b in combinations(adj, 2):
                if hs[END] - min(hs[a] + he[b], he[a] + hs[b]) + 2 >= TARGET_SAVINGS:
                    result += 1
    return result


def part2(f: List[List[str]]) -> int:
    START = find_in_cartesian_plane(f, lambda x: x == "S")[0]
    END = find_in_cartesian_plane(f, lambda x: x == "E")[0]
    MAX_CHEAT_TIME = 20
    TARGET_SAVINGS = 100

    hs = create_heatmap_from(START, f)
    he = create_heatmap_from(END, f)
    result = 0

    for a, b in combinations(
        [
            (x, y)
            for x, y in product(range(1, len(f) - 1), range(1, len(f[0]) - 1))
            if f[x][y] != "#"
        ],
        2,
    ):
        distance = abs(a[0] - b[0]) + abs(a[1] - b[1])
        if distance > MAX_CHEAT_TIME:
            continue
        if hs[END] - (min(hs[a] + he[b], he[a] + hs[b]) + distance) >= TARGET_SAVINGS:
            result += 1
    return result


if __name__ == "__main__":
    fname = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    f = [l.strip() for l in open(fname, "r").readlines() if l.strip() != ""]

    print("Part 1:", part1(deepcopy(f)))
    print("Part 2:", part2(deepcopy(f)))
