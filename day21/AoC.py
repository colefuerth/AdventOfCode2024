#!/usr/bin/python3

import sys
from functools import cache
from typing import List, Tuple
from itertools import product, pairwise


def add(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int]:
    return (a[0] + b[0], a[1] + b[1])


@cache
def find_in_cartesian_plane(char: str, f: Tuple[str]) -> Tuple[int, int]:
    return next(
        (x, y) for x, y in product(range(len(f)), range(len(f[0]))) if f[x][y] == char
    )


@cache
def move_from(a: str, b: str, d: Tuple[str]) -> int:
    ax, ay = find_in_cartesian_plane(a, d)
    bx, by = find_in_cartesian_plane(b, d)
    v, h = bx - ax, by - ay
    v = (("^" * -v) if v < 0 else "") + (("v" * v) if v > 0 else "")
    h = ((">" * h) if h > 0 else "") + (("<" * -h) if h < 0 else "")

    if by > ay and (bx, ay) != find_in_cartesian_plane(" ", d):
        return v + h + "A"
    if (ax, by) != find_in_cartesian_plane(" ", d):
        return h + v + "A"
    return v + h + "A"


@cache
def type_into_keypad(s: str, keypad: Tuple[str] = (" ^A", "<v>")) -> str:
    return "".join(move_from(a, b, keypad) for a, b in pairwise("A" + s))


@cache
def type_n_directional_robots_deep(n: int, s: str) -> str:
    if n == 0:
        return len(s)
    q = [(g + "A") for g in type_into_keypad(s).split("A")[:-1]]
    return sum(type_n_directional_robots_deep(n - 1, s) for s in q)


def part1(f: List[str]) -> int:
    return sum(
        int(l[:-1])
        * type_n_directional_robots_deep(
            2, type_into_keypad(l, keypad=("789", "456", "123", " 0A"))
        )
        for l in f
    )


def part2(f: List[str]) -> int:
    return sum(
        int(l[:-1])
        * type_n_directional_robots_deep(
            25, type_into_keypad(l, keypad=("789", "456", "123", " 0A"))
        )
        for l in f
    )


if __name__ == "__main__":
    fname = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    f = [l.strip() for l in open(fname, "r").readlines()]

    print("Part 1:", part1(f))
    print("Part 2:", part2(f))
