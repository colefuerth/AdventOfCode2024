#!/usr/bin/python3

import sys
from itertools import product
from copy import deepcopy
from typing import List, Tuple, Sequence
from multiprocessing import Pool, cpu_count
from tqdm import tqdm

def process_pair(args: Tuple[Tuple[int, List[int]], Sequence[str]]) -> int:
    """
    Process a single result-coefficients pair with given operators and return the result if found.
    
    Args:
        args: Tuple containing:
            - pair: Tuple[int, List[int]] - The result and coefficients to process
            - operators: Sequence[str] - List of operators to use in combinations
    """
    pair, operators = args
    result, coefficients = pair
    
    for p in product(operators, repeat=len(coefficients)-1):
        r = coefficients[0]
        for c, o in zip(coefficients[1:], p):
            r = eval(f'{r}{o}{c}')
        if result == r:
            return result
    return 0

def process_with_multiprocessing(f: List[List[int]], operators: Sequence[str], part: int) -> int:
    """Generic multiprocessing function that can be used by both parts."""
    args = [(pair, operators) for pair in f]
    total_items = len(args)
    
    with Pool(processes=cpu_count()) as pool:
        with tqdm(total=total_items, desc=f'Part {part}') as pbar:
            results = []
            for result in pool.imap(process_pair, args):
                results.append(result)
                pbar.update()
            
            return sum(results)

def part1(f: List[List[int]]) -> int:
    return process_with_multiprocessing(f, ['+', '*'], 1)

def part2(f: List[str]) -> int:
    return process_with_multiprocessing(f, ['+', '*', ''], 2)

if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [
        [int(a), [int(x) for x in b.strip().split()]]
        for a, b in [l.strip().split(':') for l in open(fname, 'r').readlines()]
    ]

    print('Part 1:', part1(deepcopy(f)))
    print('Part 2:', part2(deepcopy(f)))
