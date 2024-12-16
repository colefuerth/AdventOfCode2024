#!/usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy
import re
from typing import List, Tuple

N = (-1, 0)
E = (0, 1)
S = (1, 0)
W = (0, -1)
direction_to_coord = {'^': N, '>': E, 'v': S, '<': W}

def add(a: Tuple[int], b: Tuple[int]) -> Tuple[int]:
    return tuple(x + y for x, y in zip(a, b))

def is_valid_coord(coord: Tuple[int], f: Tuple[str]):
    return 0 <= coord[0] < len(f) and 0 <= coord[1] < len(f[0])


def part1(room: List[List[str]], moves: List[str]) -> int:
    moves = [direction_to_coord[move] for move in ''.join(moves)]
    robot = next((x, y) for x, y in product(range(len(room)), range(len(room[0]))) if room[x][y] == '@')

    def apply_move(pos: Tuple[int, int], direction: Tuple[int, int]) -> Tuple[int, int]:
        x, y = pos
        npos = add(pos, direction)
        if room[x][y] == '.':
            return npos
        if room[x][y] in '@O':
            j, k = npos
            if apply_move(npos, direction) == npos:
                return pos
            room[x][y], room[j][k] = room[j][k], room[x][y]
            return npos
        return pos
    for move in moves:
        robot = apply_move(robot, move)
    return sum(100 * x + y for x, y in product(range(len(room)), range(len(room[0]))) if room[x][y] == 'O')

def part2(room: List[List[str]], moves: List[str]) -> int:
    moves = [direction_to_coord[move] for move in ''.join(moves)]
    robot = next((x, y) for x, y in product(range(len(room)), range(len(room[0]))) if room[x][y] == '@')

    def apply_move(pos: Tuple[int, int], direction: Tuple[int, int]) -> Tuple[int, int]:
        x, y = pos
        npos = add(pos, direction)
        if room[x][y] == '.':
            return npos
        if room[x][y] == '@' or (room[x][y] in '[]' and direction in [E,W]):
            j, k = npos
            if apply_move(npos, direction) == npos:
                return pos
            room[x][y], room[j][k] = room[j][k], room[x][y]
            return npos
        if room[x][y] in '[]':
            lbox, rbox = (pos, add(pos, E)) if room[x][y] == '[' else (add(pos, W), pos)
            lbox2, rbox2 = add(lbox, direction), add(rbox, direction)
            if apply_move(lbox2, direction) == lbox2 or apply_move(rbox2, direction) == rbox2:
                # TODO: this needs to be broken out into a check_move and an apply_move so recursive checks can be run before applying a move
        return pos
    for move in moves:
        robot = apply_move(robot, move)
    return sum(100 * x + y for x, y in product(range(len(room)), range(len(room[0]))) if room[x][y] == 'O')


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    room, moves = open(fname).read().split('\n\n')
    # Convert to lists of strings, removing any empty lines
    room = [list(line) for line in room.splitlines() if line]
    moves = [line for line in moves.splitlines() if line]

    print('Part 1:', part1(deepcopy(room), deepcopy(moves)))
    print('Part 2:', part2(deepcopy(room), deepcopy(moves)))
