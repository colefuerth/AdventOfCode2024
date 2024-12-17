#!/usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy
import re
from typing import List, Tuple
from heapq import heappush, heappop

N = (-1, 0)
E = (0, 1)
S = (1, 0)
W = (0, -1)
DIRS = [N,E,S,W]

def add(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int]:
    return (a[0] + b[0], a[1] + b[1])
def sub(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int]:
    return (a[0] - b[0], a[1] - b[1])

# a and b must be 2 apart in the queue
def is_right_turn(a: Tuple[int, int], b: Tuple[int, int]) -> bool:
    return abs(a[0] - b[0]) == 1 and abs(a[1] - b[1]) == 1

def find_in_cartesian_plane(f: List[List[any]], key: callable):
    return next((x, y) for x, y in product(range(len(f)), range(len(f[0]))) if key(f[x][y]))

scorecache = {}
def calculate_score(queue: List[Tuple[int, int]]) -> int:
    if len(queue) < 3:
        return 0
    if len(queue) == 3:
        return len(queue) - 1 \
            + sum(is_right_turn(a, b) for a, b in zip(queue, queue[2:])) * 1000 \
            + (1000 if sub(queue[1], queue[0]) != E else 0)
    tq = tuple(queue)
    if tq in scorecache:
        return scorecache[tq]
    score = calculate_score(queue[:-1]) + 1 + is_right_turn(queue[-1], queue[-3]) * 1000
    scorecache[tq] = score
    return score

def part1(f: List[str]) -> int:
    START = find_in_cartesian_plane(f, lambda x: x == 'S')
    END = find_in_cartesian_plane(f, lambda x: x == 'E')
    
    history = set()
    queue = [(0, [START])]  # (score, state) for heap
    while queue:
        score, q = heappop(queue)
        pos = q[-1]

        if pos == END:
            return score
        for d in DIRS:
            npos = add(pos, d)
            if f[npos[0]][npos[1]] != '#' and (len(q) < 2 or npos != q[-2]) and npos not in history:
                history.add(npos)
                nq = q[:] + [npos]
                minscore = calculate_score(nq)
                heappush(queue, (minscore, nq))
    return 0

def part2(f: List[str]) -> int:
    START = find_in_cartesian_plane(f, lambda x: x == 'S')
    END = find_in_cartesian_plane(f, lambda x: x == 'E')
    
    history = {}
    queue = [(0, [START])]  # (score, state) for heap
    optimal_paths = []
    while queue:
        score, q = heappop(queue)
        pos = q[-1]
        if END in history and history[END] < score:
            continue
        if pos == END:
            optimal_paths.append(q)
        for d in DIRS:
            npos = add(pos, d)
            if f[npos[0]][npos[1]] != '#' and (len(q) < 2 or npos != q[-2]):
                nq = q[:] + [npos]
                minscore = calculate_score(nq)
                flag = False
                if npos not in history or history[npos] >= minscore:
                    flag = True
                    history[npos] = minscore
                if pos not in history or history[pos] >= score:
                    flag = True
                    history[pos] = score
                if flag:
                    heappush(queue, (minscore, nq))
    optimal_spots = set()
    for path in optimal_paths:
        optimal_spots.update(path)
    return len(optimal_spots)


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [
        l.strip()
        for l in open(fname, 'r').readlines()
    ]

    print('Part 1:', part1(deepcopy(f)))
    print('Part 2:', part2(deepcopy(f)))

# import cProfile
# import pstats
# from line_profiler import LineProfiler

# # Modify your main section:
# if __name__ == '__main__':
#     fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
#     f = [
#         l.strip()
#         for l in open(fname, 'r').readlines()
#     ]

#     # cProfile for overall function timing
#     profiler = cProfile.Profile()
#     profiler.enable()
#     result = part2(deepcopy(f))
#     profiler.disable()
#     stats = pstats.Stats(profiler).sort_stats('cumtime')
#     stats.print_stats(20)  # Show top 20 time-consuming functions

#     # Line profiler for detailed line-by-line analysis
#     lp = LineProfiler()
#     lp.add_function(part2)
#     lp.add_function(calculate_score)
#     lp_wrapper = lp(part2)
#     lp_wrapper(deepcopy(f))
#     lp.print_stats()

#     # print('Part 1:', result)
#     print('Part 2:', result)