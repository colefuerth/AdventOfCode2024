#!/usr/bin/python3

import sys
from copy import deepcopy
from typing import List
from collections import Counter


def part1(f: List[List[int]]) -> int:
    return sum(abs(a - b) for a, b in zip(*[sorted(l) for l in zip(*f)]))


def part2(f: List[str]) -> int:
    arr, hist = zip(*f)
    hist = Counter(hist)
    return sum(a * hist[a] for a in arr)


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [
        list(map(int, l.strip().split()))
        for l in open(fname, 'r').readlines()
    ]

    print('Part 1:', part1(deepcopy(f)))
    print('Part 2:', part2(deepcopy(f)))