#!/usr/bin/python3

import sys
import pathlib
from typing import List
from copy import deepcopy


def part1(f: List[str]) -> int:
    pass


def part2(f: List[str]) -> int:
    pass


if __name__ == "__main__":
    fname = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    fname = str(pathlib.Path(__file__).parent.resolve()) + f"/{fname}"
    f = [l.strip() for l in open(fname, "r").readlines() if l.strip()]

    print("Part 1:", part1(deepcopy(f)))
    print("Part 2:", part2(deepcopy(f)))
