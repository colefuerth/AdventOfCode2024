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
    new_room_map = {'#':'##', 'O':'[]', '.':'..', '@':'@.'}
    room = [list(''.join([new_room_map[pos] for pos in line])) for line in room]
    robot = next((x, y) for x, y in product(range(len(room)), range(len(room[0]))) if room[x][y] == '@')

    def check_move_vertical(pos: Tuple[int, int], direction: Tuple[int, int]) -> bool:
        x, y = pos
        if room[x][y] == '.':
            return True
        if room[x][y] == '#':
            return False
        lbox, rbox = (pos, add(pos, E)) if room[x][y] == '[' else (add(pos, W), pos)
        lbox2, rbox2 = add(lbox, direction), add(rbox, direction)
        if room[lbox2[0]][lbox2[1]] == '[':
            return check_move_vertical(lbox2, direction)
        return check_move_vertical(lbox2, direction) and check_move_vertical(rbox2, direction)

    def apply_move_vertical(pos: Tuple[int, int], direction: Tuple[int, int]) -> None:
        x, y = pos
        if room[x][y] == '.':
            return
        lbox, rbox = (pos, add(pos, E)) if room[x][y] == '[' else (add(pos, W), pos)
        lbox2, rbox2 = add(lbox, direction), add(rbox, direction)
        if room[lbox2[0]][lbox2[1]] == '[':
            apply_move_vertical(lbox2, direction)
        else:
            apply_move_vertical(lbox2, direction)
            apply_move_vertical(rbox2, direction)
        room[lbox[0]][lbox[1]], room[lbox2[0]][lbox2[1]] = room[lbox2[0]][lbox2[1]], room[lbox[0]][lbox[1]]
        room[rbox[0]][rbox[1]], room[rbox2[0]][rbox2[1]] = room[rbox2[0]][rbox2[1]], room[rbox[0]][rbox[1]]

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
        if room[x][y] in '[]' and check_move_vertical(pos, direction):
            apply_move_vertical(pos, direction)
            return npos
        return pos

    for move in ''.join(moves):
        robot = apply_move(robot, direction_to_coord[move])

    return sum(100 * x + y for x, y in product(range(len(room)), range(len(room[0]))) if room[x][y] == '[')


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    room, moves = open(fname).read().split('\n\n')
    # Convert to lists of strings, removing any empty lines
    room = [list(line) for line in room.splitlines() if line]
    moves = [line for line in moves.splitlines() if line]

    print('Part 1:', part1(deepcopy(room), deepcopy(moves)))
    print('Part 2:', part2(deepcopy(room), deepcopy(moves)))
