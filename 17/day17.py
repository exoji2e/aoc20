#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 17
def get_year(): return 2020

def ngs(c):
    if len(c) == 0: return [[]]
    out = []
    for k in ngs(c[1:]):
        out.append([c[0]-1] + k)
        out.append([c[0]] + k)
        out.append([c[0]+1] + k)
    return out

def update(world):
    world2 = set()
    C = Counter()
    for k in world:
        for k2 in map(tuple, ngs(k)):
            if k2 != k:
                C[k2] += 1
    for k, v in C.items():
        if v == 2 and k in world:
            world2.add(k)
        if v == 3:
            world2.add(k)
    return world2

def get_alive(inp):
    lines = get_lines(inp)
    world = set()
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '#':
                world.add((i, j))
    return world


def p1(v):
    alive = get_alive(v)
    world = set()
    for x, y in alive:
        world.add((x, y, 0))

    for i in range(6):
        world = update(world)

    return len(world)

def p2(v):
    alive = get_alive(v)
    world = set()
    for x, y in alive:
        world.add((x, y, 0, 0))

    for i in range(6):
        world = update(world)

    return len(world)


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
