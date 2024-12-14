#!/usr/bin/python3

import sys
from copy import deepcopy
import re
from typing import List, Tuple
from math import prod

def add(a: Tuple[int], b: Tuple[int]) -> Tuple[int]:
    return tuple(x + y for x, y in zip(a, b))

def part1(f: List[Tuple[int]]) -> int:
    seconds = 100
    bathroom_width = 101
    bathroom_height = 103
    # bathroom_width = 11
    # bathroom_height = 7
    quadrants = [0, 0, 0, 0]
    for px, py, vx, vy in f:
        x, y = add((px, py), (vx * seconds, vy * seconds))
        x, y = x % bathroom_width, y % bathroom_height
        if x in range(bathroom_width // 2) and \
           y in range(bathroom_height // 2):
            quadrants[0] += 1
        elif x in range(bathroom_width // 2 + 1, bathroom_width) and \
             y in range(bathroom_height // 2):
            quadrants[1] += 1
        elif x in range(bathroom_width // 2) and \
             y in range(bathroom_height // 2 + 1, bathroom_height):
            quadrants[2] += 1
        elif x in range(bathroom_width // 2 + 1, bathroom_width) and \
             y in range(bathroom_height // 2 + 1, bathroom_height):
            quadrants[3] += 1
    return prod(quadrants)


# I could automate this but honestly you probably want to see this tree lmao
def part2(f: List[Tuple[int]]) -> int:
    seconds = 100
    bathroom_width = 101
    bathroom_height = 103
    bathroom_base = [[' '] * bathroom_width for _ in range(bathroom_height)]
    with open("output.txt", "w") as file:
        for seconds in range(0, 10000):
            bathroom_floor = deepcopy(bathroom_base)
            for px, py, vx, vy in f:
                x, y = add((px, py), (vx * seconds, vy * seconds))
                x, y = x % bathroom_width, y % bathroom_height
                bathroom_floor[y][x] = 'O'
            file.write(f"\n\n\n\n{seconds}\n")
            file.writelines([''.join(line) + "\n" for line in bathroom_floor])
    return "just search output.txt for like 30 \"O\"'s in a row, there is a box drawn around the tree"


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = re.findall(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)', '\n'.join(open(fname, 'r').readlines()))
    f = [tuple(map(int, l)) for l in f]

    print('Part 1:', part1(deepcopy(f)))
    print('Part 2:', part2(deepcopy(f)))
