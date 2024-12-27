#!/usr/bin/python3

import sys
import pathlib
from itertools import product
from collections import defaultdict
from typing import List, Set, Tuple, Dict


def part1(f: List[List[str]]) -> int:
    network = defaultdict(list)
    for a, b in f:
        network[a].append(b)
        network[b].append(a)
    interconnected = set()
    for a in network:
        if not a.startswith("t"):
            continue
        for b in network[a]:
            for c in network[b]:
                if a in network[c]:
                    interconnected.add(tuple(sorted([a, b, c])))
    return len(interconnected)


def find_next_largest_group(
    groups: Set[Tuple[str]], network: Dict[str, List[str]]
) -> Tuple[str]:
    next_groups = set()
    for node, group in product(network, groups):
        if node in group:
            continue
        nodegroup = network[node]
        if all(groupnode in nodegroup for groupnode in group):
            next_groups.add(tuple(sorted(list(group) + [node])))
    if not next_groups:
        return groups
    return find_next_largest_group(next_groups, network)


def part2(f: List[List[str]]) -> int:
    network = defaultdict(list)
    for a, b in f:
        network[a].append(b)
        network[b].append(a)
    group = list(find_next_largest_group({tuple(sorted(l)) for l in f}, network))[0]
    return ",".join(group)


if __name__ == "__main__":
    fname = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    fname = str(pathlib.Path(__file__).parent.resolve()) + f"/{fname}"
    f = [l.strip().split("-") for l in open(fname, "r").readlines() if l.strip()]

    print("Part 1:", part1(f))
    print("Part 2:", part2(f))
