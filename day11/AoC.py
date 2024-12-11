#!/usr/bin/python3

import sys
from copy import deepcopy
from typing import List


def part1(f: List[str]) -> int:
    for _ in range(25):
        nf = []
        for rock in f:
            if rock == '0':
                nf.append('1')
            elif len(rock) % 2 == 0:
                nf.append(rock[:len(rock) // 2])
                nf.append(str(int(rock[len(rock) // 2:])))
            else:
                nf.append(str(int(rock) * 2024))
        f = nf
    return len(f)


def part2(f: List[str]) -> int:
    pass

if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = open(fname, 'r').readlines()[0].strip().split()

    print('Part 1:', part1(deepcopy(f)))
    print('Part 2:', part2(deepcopy(f)))
