#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 24
def get_year(): return 2020

def flip(active):
    neigh = Counter()
    N = [(1, 1), (-1, 1), (1, -1), (-1, -1), (0, 2), (0, -2)]
    for r, c in active:
        for dr, dc in N:
            neigh[r+dr, c+dc] += 1
    new = set()
    for k, v in neigh.items():
        if k in active:
            if 1 <= v <= 2:
                new.add(k)
        else:
            if v == 2:
                new.add(k)
    return new

def parse(inp):
    lines = get_lines(inp)
    flipped = set()
    for line in lines:
        path = parse_tile(line)
        r, c = 0, 0
        for dr, dc in path:
            r += dr
            c += dc
        T = r, c
        if T in flipped:
            flipped.remove(T)
        else:
            flipped.add(T)
    return flipped


def p1(v):
    return len(parse(v))


def p2(v):
    a = parse(v)
    for i in range(100):
        a = flip(a)
    return len(a)


def parse_tile(tile):
    i = 0
    path = []
    D = {'se': (1, 1), 'sw' : (1, -1), 'ne': (-1, 1), 'nw' : (-1, -1)}
    while i < len(tile):
        if tile[i] == 'e':
            path.append((0, 2))
            i += 1
            continue
        if tile[i] == 'w':
            path.append((0, -2))
            i += 1
            continue
        path.append(D[tile[i:i+2]])
        i += 2
    return path

        


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
