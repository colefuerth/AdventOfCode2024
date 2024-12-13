#!/usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy
import re
from typing import List


def part1(f: List[str]) -> int:
    for ax, ay, bx, by, px, py in f:
        pass


def part2(f: List[str]) -> int:
    pass


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [
        list(map(int, machine))
        for machine in re.findall(
            r'Button A: X\+(\d+), Y\+(\d+)\s+Button B: X\+(\d+), Y\+(\d+)\s+Prize: X=(\d+), Y=(\d+)',
            '\n'.join(open(fname, 'r').readlines())
        )
    ]
    print(f)

    print('Part 1:', part1(deepcopy(f)))
    print('Part 2:', part2(deepcopy(f)))
