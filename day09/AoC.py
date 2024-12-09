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
    checksum = 0
    idx = 0
    i = 0
    while i < len(filetree):
        fill, empty = filetree[i]
        
        # process fill part first (ez)
        checksum += i * (ns(idx + fill - 1) // (ns(idx - 1) if idx > 1 else 1))
        idx += fill
        
        # last one only fills, dont bother with the empty or it double hits the last "fill"
        if i == len(filetree) - 1:
            break
        
        # fill 2 empty 2
        # first bite should be nn(1)
        # second bite should be nn(3) - nn(1)

        # process empty part next (hard)
        while empty > 0:
            bite = empty
            j = len(filetree) - 1
            if empty > filetree[j][0]:
                # set the bite size based on the last block
                # remove the last filetree node since it is being eaten
                bite = filetree.pop()[0]
            elif empty < filetree[j][0]:
                # take a bite out of the last filetree fill part
                filetree[j][0] -= bite
            else:
                # if they are the same, just remove the last fill in the filetree and process the whole bite
                filetree.pop()

            # execute the bite with the checksum
            checksum += j * (ns(idx + bite - 1) // (ns(idx - 1) if idx > 1 else 1))
            # update the empty space size with the new bite
            empty -= bite

        # increment to next node in filetree
        i += 1
    print()
    return checksum


def part2(f: str) -> int:
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


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = open(fname, 'r').readlines()[0].strip()

    print('Part 1:', part1(f))
    print('Part 2:', part2(f))
