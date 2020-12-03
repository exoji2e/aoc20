#!/usr/bin/python3
import sys, time, datetime, argparse
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 3
def get_year(): return 2020

def p1(v):
    lines = get_lines(v)
    grid = [[ch == '#' for ch in line] for line in lines]
    return count(grid, 1, 3)

def count(grid, dr, dc):
    S = 0
    for i in range(1, len(grid)):
        r = dr*i
        c = dc*i
        if r < len(grid):
            if grid[r][c%len(grid[r])]:
                S += 1
    return S


def p2(v):
    lines = get_lines(v)
    grid = [[ch == '#' for ch in line] for line in lines]
    D = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    p = 1
    for dr, dc in D:
        pp = count(grid, dr, dc)
        p *= pp
    return p

if __name__ == '__main__':
    """
    cmds = [
        'run1', 'run2',
        #'print_stats',
        #'submit1',
        #'submit2']
    """
    cmds = get_commands()
    print('Commands:', cmds)
    if 'run_samples' in cmds or 'samples_only' in cmds:
        run_samples(p1, p2, cmds, __file__)
    if 'samples_only' not in cmds:
        run(get_year(), get_day(), p1, p2, cmds, FILE=__file__)
