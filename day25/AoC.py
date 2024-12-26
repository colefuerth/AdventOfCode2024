#!/usr/bin/python3

import sys
from typing import List
from itertools import product, groupby


def part1(keys: List[List[str]], locks: List[List[str]]) -> int:
    return sum(
        all((a == "." or b == ".") for a, b in zip(key, lock))
        for key, lock in product(keys, locks)
    )


def part2(keys: List[List[str]], locks: List[List[str]]) -> int:
    pass


if __name__ == "__main__":
    fname = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    f = [l.strip() for l in open(fname, "r").readlines()]
    groups = [
        list(group) for is_blank, group in groupby(f, lambda x: not x) if not is_blank
    ]
    keys, locks = [], []
    for group in groups:
        if group[0] == "#####":
            locks.append("".join(group[1:-1]))
        else:
            keys.append("".join(group[1:-1]))

    print("Part 1:", part1(keys, locks))
    print("Part 2:", part2(keys, locks))
