#!/usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy
import re
from typing import Tuple, List
from collections import defaultdict

BEFORE=0
AFTER=1

def create_ordering_lookup(ordering):
    """Create a data structure for representing the ordering rules
    
    Each key maps to the rules for that number
    Each value contains a BEFORE and AFTER Tuple, relative to its key (items in before are items the key must come before)

    Args:
        ordering (_type_): _description_
    """
    d = defaultdict(lambda x: [[],[]])
    for before, after in ordering:
        d[before][BEFORE].append(after)
        d[after][AFTER].append(before)

def check_update_against_rules(update, rules) -> bool:
    for before, after in rules:
        if not (before in update and after in update):
            continue
        if update.index(before) > update.index(after):
            return False
    return True

def part1(rules: Tuple[Tuple[int, int]], updates: List[List[int]]) -> int:
    return sum (update[len(update) // 2] for update in updates if check_update_against_rules(update, rules))

def fix_update_against_rules(update, rules) -> bool:
    for before, after in rules:
        if not (before in update and after in update):
            continue
        before, after = update.index(before), update.index(after)
        if before > after:
            update[before], update[after] = update[after], update[before]
            return fix_update_against_rules(update, rules)
    return update

def part2(rules: Tuple[Tuple[int, int]], updates: List[List[int]]) -> int:
    updates = [fix_update_against_rules(update, rules) for update in updates if not check_update_against_rules(update, rules)]
    return sum(update[len(update) // 2] for update in updates)

if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [
        l.strip()
        for l in open(fname, 'r').readlines()
    ]
    
    ordering = tuple(tuple(int(i) for i in entry.split("|")) for entry in f[:f.index("")])
    updates = [[int(i) for i in entry.split(",")] for entry in f[f.index("") + 1:]]

    print('Part 1:', part1(ordering, updates))
    print('Part 2:', part2(ordering, updates))
