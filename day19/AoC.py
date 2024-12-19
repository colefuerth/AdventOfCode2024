#!/usr/bin/python3

import sys
from typing import Tuple
from functools import cache


@cache
def construct(remaining: str, blocks: Tuple[str]) -> int:
    if not remaining:
        return 1
    return sum(
        construct(remaining[len(block):], blocks)
        for block in blocks
        if remaining.startswith(block)
    )


def part1(materials: Tuple[str], blankets: Tuple[str]) -> int:
    return sum(construct(blanket, materials) > 0 for blanket in blankets)


def part2(materials: Tuple[str], blankets: Tuple[str]) -> int:
    return sum(construct(blanket, materials) for blanket in blankets)


if __name__ == "__main__":
    fname = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    f = [l.strip() for l in open(fname, "r").readlines()]
    materials = tuple(f[0].split(", "))
    blankets = tuple(f[2:])

    print("Part 1:", part1(materials, blankets))
    print("Part 2:", part2(materials, blankets))
