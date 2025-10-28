#!/usr/bin/python3

import sys
import pathlib
from copy import deepcopy
from typing import List, Dict, Optional
from itertools import groupby, pairwise, combinations
from heapq import heappop, heappush, heapify
from random import getrandbits
from collections import defaultdict

def solve(
    register: str,
    known: Dict[str, int],
    gates: Dict[str, List[str]],
    dependency_tree: Optional[List[str]] = None,
) -> int:
    if register in known:
        return known[register]
    if dependency_tree is None:
        dependency_tree = []
    if register in dependency_tree:
        raise ValueError(f"Circular dependency detected: {register}")
    dependency_tree.append(register)
    a, operator, b = gates[register]
    a, b = solve(a, known, gates, dependency_tree), solve(
        b, known, gates, dependency_tree
    )
    c = 0
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
    z = {gate: solve(gate, known, gates)
         for gate in gates if gate.startswith("z")}
    b = "".join(str(z[zz]) for zz in sorted(z, reverse=True))
    return int(b, 2)

def build_gate_string(gate: str, known: Dict[str, int], gates: Dict[str, List[str]]) -> str:
    if gate in known:
        return gate
    if gate in ["AND", "OR", "XOR"]:
        return gate
    a, op, b = gates[gate]
    return f"({build_gate_string(a, known, gates)} {op} {build_gate_string(b, known, gates)})"

def part2(known: Dict[str, int], gates: Dict[str, List[str]]) -> str:
    # bitsize = len([g for g in gates if g.startswith("z")])
    # operation = lambda x, y: x & y  # AND
    z = {gate: build_gate_string(gate, known, gates)
         for gate in gates if gate.startswith("z")}
    print("\n".join(f"{zz}: {z[zz]}" for zz in sorted(z, reverse=True)))
    
    return ""

if __name__ == "__main__":
    fname = sys.argv[1] if len(sys.argv) > 1 else "small.txt"
    fname = str(pathlib.Path(__file__).parent.resolve()) + f"/{fname}"
    f = [l.strip() for l in open(fname, "r").readlines()]
    groups = [
        list(group) for is_blank, group in groupby(f, lambda x: not x) if not is_blank
    ]
    known = {key: int(value)
             for key, value in [l.split(": ") for l in groups[0]]}
    gates = {out: a.split(" ")
             for a, out in [l.split(" -> ") for l in groups[1]]}

    print("Part 1:", part1(deepcopy(known), deepcopy(gates)))
    print("Part 2:", part2(deepcopy(known), deepcopy(gates)))
