#!/usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy
import re
from typing import List


def ns(n: int) -> int:
    return n*(n+1)//2


def part1(f: str) -> int:
    filetree = [[int(fill), int(empty)] for fill, empty in zip(f[::2], f[1::2])] + [[int(f[-1]), 0]]
    disk = []
    for i, (fill, empty) in enumerate(filetree):
        disk.extend([i] * fill)
        disk.extend(['.'] * empty)
    cs = 0
    for i, d in enumerate(disk):
        while d == '.':
            d = disk.pop()
        cs += i * d
    return cs


def part2(f: str) -> int:
    # create the disk of empty and full blocks
    disk = []
    for i, (fill, empty) in enumerate(zip(f[::2], f[1::2])):
        disk.append([int(i), int(fill)])
        disk.append(['.', int(empty)])
    disk.append([len(f) // 2, int(f[-1])])
    # iterate over the full blocks from largest to smallest
    for block in reversed(disk[::2]):
        size = block[1]
        # get the first block to the left of the current block that is large enough to contain it, if any
        empty = next(filter(lambda x: x[0] == '.' and x[1] >= size, disk[:disk.index(block)]), None)
        if empty is None:
            continue
        # if a better empty block is found, shuffle the block into it and adjust filesystem for the new block
        i = disk.index(empty)
        if empty[1] > size:
            empty[1] -= size
        else:
            disk.pop(i)
        disk.insert(i, block[::])
        block[0] = '.'
    # calculate the checksum of the disk (scuffed but idc)
    cs = 0
    idx = 0
    for x, size in disk:
        if x == '.':
            idx += size
        else:
            for _ in range(size):
                cs += idx * x
                idx += 1
    return cs

if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = open(fname, 'r').readlines()[0].strip()

    print('Part 1:', part1(f))
    print('Part 2:', part2(f))
