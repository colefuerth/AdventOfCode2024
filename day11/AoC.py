#!/usr/bin/python3

import sys
from copy import deepcopy
from typing import List, Tuple
from functools import cache

@cache
def process_rock_turn(rock: str) -> Tuple[str]:
    if rock == '0':
        return ('1',)
    elif len(rock) % 2 == 0:
        return (rock[:len(rock) // 2], str(int(rock[len(rock) // 2:])))
    else:
        return (str(int(rock) * 2024),)

@cache
def rock_to_n_turns(rock: str, n: int) -> int:
    if n == 0:
        return 1
    return sum(rock_to_n_turns(r, n - 1) for r in process_rock_turn(rock))

def part1(f: List[str]) -> int:
    for _ in range(25):
        nf = []
        for rock in f:
            nf.extend(process_rock_turn(rock))
        f = nf
    return len(f)

def part2(f: List[str]) -> int:
    return sum(rock_to_n_turns(rock, 75) for rock in f)

if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = open(fname, 'r').readlines()[0].strip().split()

    print('Part 1:', part1(deepcopy(f)))
    print('Part 2:', part2(deepcopy(f)))
