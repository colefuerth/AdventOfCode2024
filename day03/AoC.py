#!/usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy
import re
from typing import List


def part1(f: List[str]) -> int:
    return sum(
        int(a) * int(b)
        for a, b in re.findall(r"mul\((\d\d?\d?),(\d\d?\d?)\)", ''.join(f))
    )


def part2(f: List[str]) -> int:
    ret = 0
    enabled = True
    for a, b, do, dont in re.findall(r"mul\((\d\d?\d?),(\d\d?\d?)\)|(do\(\))|(don't\(\))", ''.join(f)):
        if do:
            enabled = True
        elif dont:
            enabled = False
        elif enabled:
            ret += int(a) * int(b)
    return ret


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [
        l.strip("\n")
        for l in open(fname, 'r').readlines()
    ]

    print('Part 1:', part1(deepcopy(f)))
    print('Part 2:', part2(deepcopy(f)))