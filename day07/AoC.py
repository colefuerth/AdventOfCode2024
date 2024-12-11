#!/usr/bin/python3

import sys
from itertools import product
from copy import deepcopy
from typing import List

def process_pair(result: int, coefficients: List[int], operators: List[str]) -> int:
    for p in product(operators, repeat=len(coefficients)-1):
        r = coefficients[0]
        for c, o in zip(coefficients[1:], p):
            if o == '*':
                r *= c
            elif o == '+':
                r += c
            else:
                r = int(str(r) + str(c))
        if result == r:
            return result
    return 0

def part1(f: List[List[int]]) -> int:
    return sum(process_pair(result, coefficients, ['+', '*']) for result, coefficients in f)

def part2(f: List[str]) -> int:
    return sum(process_pair(result, coefficients, ['+', '*', '']) for result, coefficients in f)

if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [
        [int(a), [int(x) for x in b.strip().split()]]
        for a, b in [l.strip().split(':') for l in open(fname, 'r').readlines()]
    ]

    print('Part 1:', part1(deepcopy(f)))
    print('Part 2:', part2(deepcopy(f)))
