#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 12
def get_year(): return 2020

def p1(v):
    lines = get_lines(v)
    DIR = 0
    DRS = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    DMP = {'N': 3, 'S': 1, 'E': 0, 'W': 2}
    X, Y = 0, 0
    for ac in lines:
        op = ac[0]
        cnt = int(ac[1:])
        if op in 'NSWE':
            d = DMP[op]
            dx, dy = DRS[d]
            X, Y = X + cnt*dx, Y + cnt*dy
        if op == 'R':
            DIR = (DIR + cnt//90)%4
        if op == 'L':
            DIR = (DIR - cnt//90)%4
        if op == 'F':
            dx, dy = DRS[DIR]
            X, Y = X + cnt*dx, Y + cnt*dy
    
    return abs(X) + abs(Y)

def p2(v):
    lines = get_lines(v)
    chunks = v.split('\n\n')
    DIR = 0
    DRS = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    DMP = {'N': 3, 'S': 1, 'E': 0, 'W': 2}
    XR = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    YR = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    X, Y = 0, 0
    WP = (10, 1)
    for ac in lines:
        op = ac[0]
        cnt = int(ac[1:])
        if op in 'NSWE':
            d = DMP[op]
            dx, dy = DRS[d]
            WP = WP[0] + cnt*dx, WP[1] + cnt*dy
        if op == 'R':
            rot = -(cnt//90)%4
            x = WP[0]*XR[rot][0] + WP[1]*XR[rot][1]
            y = WP[0]*YR[rot][0] + WP[1]*YR[rot][1]
            WP = x, y

        if op == 'L':
            rot = (cnt//90)%4
            x = WP[0]*XR[rot][0] + WP[1]*XR[rot][1]
            y = WP[0]*YR[rot][0] + WP[1]*YR[rot][1]
            WP = x, y
        if op == 'F':
            X, Y = X + cnt*WP[0], Y + cnt*WP[1]
    
    return abs(X) + abs(Y)


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
