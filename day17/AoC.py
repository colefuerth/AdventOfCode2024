#!/usr/bin/python3

import sys
from itertools import count
from copy import deepcopy
import re
from typing import List


def part1(f: List[int]) -> int:
    a, b, c = f[:3]
    ip = 0
    program = f[3:]
    stdout = []
    def combo_operand(operand: int) -> int:
        match operand:
            case 0 | 1 | 2 | 3:
                return operand
            case 4:
                return a
            case 5:
                return b
            case 6:
                return c
    while ip < len(program):
        opcode, operand = program[ip], program[ip + 1]
        match opcode:
            case 0: # adv
                a = a // (2 ** combo_operand(operand))
            case 1: # bxl
                b = b ^ operand
            case 2: # bst
                b = combo_operand(operand) % 8
            case 3: # jnz
                if a != 0:
                    ip = operand
                    continue
            case 4: # bxc
                b = b ^ c
            case 5: # out
                stdout.append(str(combo_operand(operand) % 8))
            case 6: # bdv
                b = a // (2 ** combo_operand(operand))
            case 7: # cdv
                c = a // (2 ** combo_operand(operand))
        ip += 2
    return ','.join(stdout)

def part2(f: List[int]) -> int:
    program = f[3:]
    for i in range(1000):
        result = part1([i] + f[1:])
        print(f'{i}: {result}')
        if result == program:
            return i


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [int(x) for x in re.findall(r'\d+', '\n'.join(open(fname, 'r').readlines()))]

    print('Part 1:', part1(deepcopy(f)))
    print('Part 2:', part2(deepcopy(f)))
