#!/usr/bin/python3

import re
import sys
import numpy as np
from copy import deepcopy
from typing import List

def verify_solution(ax, ay, bx, by, target_x, target_y, a_presses, b_presses) -> bool:
    return ax * a_presses + bx * b_presses == target_x and ay * a_presses + by * b_presses == target_y

def find_solution(ax, ay, bx, by, target_x, target_y) -> int:
    A = np.array([[ax, bx], [ay, by]])
    B = np.array([target_x, target_y])
    x = np.linalg.solve(A, B)
    x = np.rint(x).astype(int)
    if np.allclose(A @ x, B) and verify_solution(ax, ay, bx, by, target_x, target_y, x[0], x[1]):
        return 3 * x[0] + x[1]
    return 0

def part1(f: List[List[int]]) -> int:
    return sum(find_solution(*machine) for machine in f)

def part2(f: List[List[int]]) -> int:
    total_cost = 0
    for machine in f:
        machine[4] += 10000000000000
        machine[5] += 10000000000000
        total_cost += find_solution(*machine)
    return total_cost

if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else '/home/cole/AdventOfCode2024/day13/small.txt'
    f = [
        list(map(int, machine))
        for machine in re.findall(
            r'Button A: X\+(\d+), Y\+(\d+)\s+Button B: X\+(\d+), Y\+(\d+)\s+Prize: X=(\d+), Y=(\d+)',
            '\n'.join(open(fname, 'r').readlines())
        )
    ]

    print('Part 1:', part1(deepcopy(f)))
    print('Part 2:', part2(deepcopy(f)))
