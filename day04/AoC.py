#!/usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy
import re
from typing import List

def get_diagonals(f: List[str]) -> List[str]:
    ret = []
    for l in range(len(f)):
        sublist = []
        r = min(len(f[0]), len(f) - l)
        for x in range(0, r):
            sublist.append(f[l+x][x])
        ret.append(''.join(sublist))
    for l in range(1, len(f[0])):
        sublist = []
        r = min(len(f), len(f[0]) - l)
        for x in range(0, r):
            sublist.append(f[x][l + x])
        ret.append(''.join(sublist))
    return ret

def part1(f: List[str]) -> int:
    f += list(map(''.join, zip(*f)))
    f += get_diagonals(f)
    f += get_diagonals([list(reversed(l)) for l in f])
    return len(re.findall(r"XMAS|SAMX", " ".join(f)))

def part2(f: List[str]) -> int:
    pass


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [
        l.strip()
        for l in open(fname, 'r').readlines()
    ]

    print('Part 1:', part1(deepcopy(f)))
    print('Part 2:', part2(deepcopy(f)))