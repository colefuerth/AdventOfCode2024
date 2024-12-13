#!/usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy
import re
from typing import List, Tuple, Set
from collections import defaultdict
from itertools import groupby

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

def group_farms(f: List[str]):
    # plots = {plotletter:[{plot_coords_set},{plot_fences_set}]}
    visited = set()
    def explore_area(coord: Tuple[int, int]) -> List[List[int]]:
        region = set()
        fences = set()
        queue = [coord]
        while queue:
            nq = []
            for plot in queue:
                visited.add(plot)
                region.add(plot)
                x, y = plot
                for direction in DIRS:
                    adj = add(plot, direction)
                    if not is_valid_coord(adj, f) or f[adj[0]][adj[1]] != f[x][y]:
                        fences.add((plot, direction))
                    elif adj not in visited and adj not in nq:
                        nq.append(adj)
            queue = nq
        return [f[coord[0]][coord[1]], region, fences]
    return [explore_area(coord) for coord in product(range(len(f)), range(len(f[0]))) if coord not in visited]


def part1(f: List[str]) -> int:
    return sum(len(p) * len(f) for _, p, f in group_farms(f))


def part2(f: List[str]) -> int:
    # perpendicular_dirs = {
    #     N: [E, W],
    #     S: [E, W],
    #     E: [N, S],
    #     W: [N, S]
    # }
    # visited = set()
    # def explore_fence(fence: Tuple[int, int], fences):
    #     queue = [fence]
    #     while queue:
    #         nq = []
    #         for f in queue:
    #             visited.add(f)
    #             region.add(f)
    #             x, y = f
    #             for direction in perpendicular_dirs[fence[1]]:
    #                 adj = add(f, direction)
    #                 if not is_valid_coord(adj, f) or f[adj[0]][adj[1]] != f[x][y]:
    #                     fences.add((f, direction))
    #                 elif adj not in visited and adj not in nq:
    #                     nq.append(adj)
    #         queue = nq
    cost = 0
    for _, plots, fences in group_farms(f):
        # group the fences by direction
        fences_by_direction = {d:[] for d in DIRS}
        for coord, direction in fences:
            fences_by_direction[direction].append(coord)
        number_of_fences = 0
        # for each direction, group them by x or y value
        # then, group them by sorting them and looking for contiguous patterns
        for direction, group in fences_by_direction.items():
            if direction in [N, S]:
                group_by_coords = groupby(sorted(group), lambda x: x[0])
                for key, latlon in group_by_coords:
                    number_of_fences += 1
                    latlon = list(latlon)
                    for a, b in zip(latlon, latlon[1:]):
                        if abs(a[1] - b[1]) != 1:
                            number_of_fences += 1
            else:
                group_by_coords = groupby(sorted(group, key=lambda x: x[1]), lambda x: x[1])
                for key, latlon in group_by_coords:
                    number_of_fences += 1
                    latlon = sorted(list(latlon))
                    for a, b in zip(latlon, latlon[1:]):
                        if abs(a[0] - b[0]) != 1:
                            number_of_fences += 1
        cost += number_of_fences * len(plots)
    return cost

if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else '/home/cole/AdventOfCode2024/day12/input.txt'
    f = [
        l.strip()
        for l in open(fname, 'r').readlines()
        if l.strip()
    ]

    print('Part 1:', part1(deepcopy(f)))
    print('Part 2:', part2(deepcopy(f)))
