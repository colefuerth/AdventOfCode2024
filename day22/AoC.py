#!/usr/bin/python3

import sys
import pathlib
import numpy as np
from typing import List
from collections import defaultdict


PRUNE = 16777216


def part1(f: List[int]) -> int:
    sn = np.array(f)
    for _ in range(2000):
        sn = ((sn * 64) ^ sn) % PRUNE
        sn = (np.floor_divide(sn, 32) ^ sn) % PRUNE
        sn = ((sn * 2048) ^ sn) % PRUNE
    return sum(sn)


def part2(f: List[int]) -> int:
    # generate the price history from the first 2001 secret numbers
    sn = np.array(f)
    history = [sn % 10]
    for _ in range(2000):
        sn = ((sn * 64) ^ sn) % PRUNE
        sn = (np.floor_divide(sn, 32) ^ sn) % PRUNE
        sn = ((sn * 2048) ^ sn) % PRUNE
        history.append(sn % 10)
    # transpose the price history to be per vendor, and calculate the first differences
    prices = np.array(history).T
    dx = np.diff(prices)
    # for each vendor, cache the possible bananas bought from the first occurence of each sequence
    sequences = [{} for _ in range(len(prices))]
    for d, p, s in zip(dx, prices, sequences):
        for i in range(len(d) - 3):
            slice = tuple(d[i : i + 4])
            if slice not in s:
                s[slice] = p[i + 4]
    # using the sequences cache, figure out which sequence is most profitable
    # start by flattening the sequences into one dict, then find the max banana count
    total_per_sequences = defaultdict(int)
    for sequence in sequences:
        for s, p in sequence.items():
            total_per_sequences[s] += p
    return max(total_per_sequences.values())


if __name__ == "__main__":
    fname = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    fname = str(pathlib.Path(__file__).parent.resolve()) + f"/{fname}"
    f = [int(l.strip()) for l in open(fname, "r").readlines() if l.strip()]

    print("Part 1:", part1(f))
    print("Part 2:", part2(f))
