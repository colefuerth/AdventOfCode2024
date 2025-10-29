#!/usr/bin/python3

import sys
import pathlib
from copy import deepcopy
from typing import List, Dict, Optional, Union
from itertools import groupby, product
from functools import cache

# ------------------------------- PART 1 -----------------------------

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

#  ------------------------------ PART 2 -----------------------------

class SchematicNode:
    def __init__(self, left: Union['SchematicNode', str], operation: str, right: Union['SchematicNode', str]):
        self.operation = operation
        self.left = left
        self.right = right

    def __str__(self) -> str:
        if self.left is None and self.right is None:
            return self.operation
        return f"({str(self.left)} {self.operation} {str(self.right)})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, SchematicNode):
            return False
        return (self.operation == other.operation and
                (self.left == other.left and
                self.right == other.right) or
                (self.left == other.right and
                self.right == other.left))


def build_actual_schematic(gate: str, gates: Dict[str, List[str]]) -> Union[SchematicNode, str]:
    if gate[0] in "xy":
        return gate
    a, op, b = gates[gate]
    return SchematicNode(
        build_actual_schematic(a, gates),
        op,
        build_actual_schematic(b, gates)
    )

def get_all_gates_in_chain(gate: str, gates: Dict[str, List[str]]) -> List[str]:
    if gate[0] in "xy":
        return []
    a, _, b = gates[gate]
    return [gate] + get_all_gates_in_chain(a, gates) + get_all_gates_in_chain(b, gates)

@cache
def build_expected_schematic(bit: int, toplevel: bool = True) -> SchematicNode:
    if bit == 0:
        return SchematicNode(
            "x00",
            ("XOR" if toplevel else "AND"),
            "y00"
        )
    if bit == 1:
        return SchematicNode(
            SchematicNode("x01", "XOR", "y01"),
            ("XOR" if toplevel else "AND"),
            SchematicNode("x00", "AND", "y00")
        )
    return SchematicNode(
        SchematicNode(f"x{bit:02}","XOR",f"y{bit:02}"),
        "XOR",
        SchematicNode(
            SchematicNode(f"x{bit-1:02}", "AND", f"y{bit-1:02}"),
            "OR",
            SchematicNode(
                SchematicNode(f"x{bit-1:02}", "XOR", f"y{bit-1:02}"),
                "AND",
                build_expected_schematic(bit-1, False).right
            )
        )
    )

def part2(gates: Dict[str, List[str]]) -> str:
    swaps = []
    sys.setrecursionlimit(200) # genuinely faster than handling manually
    for bit in range(len([k for k in gates.keys() if k.startswith("z")])):
        if build_actual_schematic(f"z{bit:02}", gates) != build_expected_schematic(bit):
            potential_swaps = list(product(get_all_gates_in_chain(f"z{bit:02}", gates), gates.keys()))
            for a, b in potential_swaps:
                if a == b:
                    continue
                gates[a], gates[b] = gates[b], gates[a]
                try:
                    if build_actual_schematic(f"z{bit:02}", gates) == build_expected_schematic(bit):
                        swaps.append(a)
                        swaps.append(b)
                        break
                except RecursionError:
                    pass
                gates[a], gates[b] = gates[b], gates[a]
    return ",".join(sorted(swaps))

# ------------------------------------------------------------

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
    print("Part 2:", part2(deepcopy(gates)))
