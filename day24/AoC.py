#!/usr/bin/python3

import sys
import pathlib
from copy import deepcopy
from typing import List, Dict
from itertools import groupby


def solve(register: str, known: Dict[str, int], gates: Dict[str, List[str]]) -> int:
    if register in known:
        return known[register]
    a, operator, b = gates[register]
    a, b = solve(a, known, gates), solve(b, known, gates)
    match operator:
        case "AND":
            c = a & b
        case "OR":
            c = a | b
        case "XOR":
            c = a ^ b
    known[register] = c
    return c


def part1(known: Dict[str, int], gates: Dict[str, List[str]]) -> int:
    z = {gate: solve(gate, known, gates) for gate in gates if gate.startswith("z")}
    b = "".join(str(z[zz]) for zz in sorted(z, reverse=True))
    return int(b, 2)


def part2(known: Dict[str, int], gates: Dict[str, List[str]]) -> int:
    pass


if __name__ == "__main__":
    fname = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    fname = str(pathlib.Path(__file__).parent.resolve()) + f"/{fname}"
    f = [l.strip() for l in open(fname, "r").readlines()]
    groups = [
        list(group) for is_blank, group in groupby(f, lambda x: not x) if not is_blank
    ]
    known = {key: int(value) for key, value in [l.split(": ") for l in groups[0]]}
    gates = {out: a.split(" ") for a, out in [l.split(" -> ") for l in groups[1]]}

    print("Part 1:", part1(deepcopy(known), deepcopy(gates)))
    print("Part 2:", part2(deepcopy(known), deepcopy(gates)))
