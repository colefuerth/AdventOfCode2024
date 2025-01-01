#!/usr/bin/python3

import sys
import pathlib
from copy import deepcopy
from typing import List, Dict
from itertools import groupby, pairwise, combinations


def solve(
    register: str,
    known: Dict[str, int],
    gates: Dict[str, List[str]],
    dependency_tree: List[str] = None,
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
    x = "".join(str(known[x]) for x in sorted(known, reverse=True) if x.startswith("x"))
    y = "".join(str(known[x]) for x in sorted(known, reverse=True) if x.startswith("y"))
    z = bin(int(x, 2) + int(y, 2))[2:]

    def similarity_score(a: str, b: str) -> int:
        return sum(i == j for i, j in zip(a, b))

    cz = {
        gate: solve(gate, deepcopy(known), gates)
        for gate in gates
        if gate.startswith("z")
    }
    swaps = []
    while cz != z:
        scores_this_round = []
        for a, b in combinations(gates, 2):
            gates[a], gates[b] = gates[b], gates[a]
            try:
                cz = {
                    gate: solve(gate, deepcopy(known), gates)
                    for gate in gates
                    if gate.startswith("z")
                }
                cz = "".join(str(cz[zz]) for zz in sorted(cz, reverse=True))
                scores_this_round.append([similarity_score(z, cz), (a, b)])
            except ValueError:
                pass
            gates[a], gates[b] = gates[b], gates[a]
        a, b = max(scores_this_round, key=lambda x: x[0])[1]
        gates[a], gates[b] = gates[b], gates[a]
        swaps.append(a)
        swaps.append(b)
    return ",".join(sorted(swaps))


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
