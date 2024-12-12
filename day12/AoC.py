#!/usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy
import re
from typing import List, Tuple
from collections import defaultdict

N = (-1, 0)
E = (0, 1)
S = (1, 0)
W = (0, -1)
DIRS = [N,E,S,W]

def add(a: Tuple[int], b: Tuple[int]) -> Tuple[int]:
    return tuple(x + y for x, y in zip(a, b))

def is_valid_coord(coord: Tuple[int], f: Tuple[str]):
    return 0 <= coord[0] < len(f) and 0 <= coord[1] < len(f[0])

# fence tuples will be (plot, direction) from now on
# def get_fence_tuple(plot: Tuple[int, int], direction: Tuple[int, int]) -> int:
#     b = add(plot, direction)
#     return (min(plot, b), max(plot, b))

def part1(f: List[str]) -> int:
    # plots = {plotletter:[{plot_coords_set},{plot_fences_set}]}
    plots = defaultdict(lambda x: [set(), set()])
    queue = [(len(f) // 2, len(f[0]) // 2)]
    visited = set()
    while queue:
        nq = []
        for plot in queue:
            visited.add(plot)
            plots[f[x][y]][0].add(plot)
            x, y = plot
            for direction in DIRS:
                adj = add(plot, direction)
                if not is_valid_coord(adj, f) or f[adj[0]][adj[1]] != f[x][y]:
                    plots[f[x][y]][1].add((plot, direction))
                if is_valid_coord(adj, f) and adj not in visited:
                    nq.append(adj)
    return sum(len(p) * len(f) for p, f in plots.values())
        

def part2(f: List[str]) -> int:
    return 0


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [
        l.strip()
        for l in open(fname, 'r').readlines()
        if l.strip()
    ]

    print('Part 1:', part1(deepcopy(f)))
    print('Part 2:', part2(deepcopy(f)))
