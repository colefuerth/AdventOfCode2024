#!/usr/bin/python3

import sys
import re
from typing import List


def run_program(f: List[int]) -> List[int]:
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
                stdout.append(combo_operand(operand) % 8)
            case 6: # bdv
                b = a // (2 ** combo_operand(operand))
            case 7: # cdv
                c = a // (2 ** combo_operand(operand))
        ip += 2
    return stdout


def part1(f: List[int]) -> str:
    return ','.join(map(str, run_program(f)))


def part2(f: List[int]) -> int:
    # each output of the program is functionally a scrambled base 8 number
    program = f[3:]

    # base 8, so find the first spot where we reach that length of program output
    a = sum(7 * 8**i for i in range(len(program) - 1)) + 1

    while True:
        result = run_program([a] + f[1:])
        if result == program:
            return a

        # for each position right to left, increment it until we see the correct guy
        for i in range(len(result) - 1, -1, -1):
            if result[i] != program[i]:
                a += 8 ** i
                break


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [int(x) for x in re.findall(r'\d+', '\n'.join(open(fname, 'r').readlines()))]

    print('Part 1:', part1(f))
    print('Part 2:', part2(f))
