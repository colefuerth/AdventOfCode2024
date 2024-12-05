#!/usr/bin/python3

import sys
from itertools import combinations
from copy import deepcopy
import re
from typing import List


def part1(f: List[str]) -> int:
    return sum(
        all( 1 <= abs(x) <= 3 for x in l) and
        (  all( x > 0 for x in l) or all( x < 0 for x in l ) )
        for l in [[a - b for a, b in zip(l[:-1], l[1:])] for l in f] # convert f elements to first differences between them
    )


def part2(f: List[str]) -> int:
    # yes I know this is way less efficient than it could be but it reuses most of the part 1 code and I am feeling lazy
    # it is also a lot more complex to not brute force this and this is still techically linear time
    # n^2 if you increase the length of each individual input but those are all small which makes this linear really (im coping)
    return sum(
        any(
            all( 1 <= abs(x) <= 3 for x in l) and                       # first differences scale represent rate of change
            ( all( x > 0 for x in l) or all( x < 0 for x in l ) )       # first differences sign represent direction of change
            for l in comb                                               # check all possible combinations of each test group
        )
        for comb in [[[a - b for a, b in zip(l[:-1], l[1:])] for l in ([line] + list(combinations(line, len(line) - 1)))] for line in f]    # convert f elements to first differences between them, for each possible test that could work for each line
    )


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [
        [int(i) for i in l.strip().split()]
        for l in open(fname, 'r').readlines()
    ]

    print('Part 1:', part1(deepcopy(f)))
    print('Part 2:', part2(deepcopy(f)))
