#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples
from utils import *
def get_day(): return 2
def get_year(): return 2020

def p1(v):
    lines = get_lines(v)
    S = 0
    for line in lines:
        lo, hi, c, ps = multi_split(line, ' :-')
        lo, hi = map(int, [lo, hi])
        cnt = ps.count(c)
        if lo <= cnt <= hi:
            S += 1
    return S

def p2(v):
    lines = get_lines(v)
    S = 0
    for line in lines:
        lo, hi, c, ps = multi_split(line, ' :-')
        lo, hi = map(int, [lo, hi])
        ok1 = ps[lo-1] == c
        ok2 = ps[hi-1] == c
        if (ok1 and not ok2) or (not ok1 and ok2):
            S += 1
    return S


if __name__ == '__main__':
    cmds = [
        'run1',
        'run2',
        # 'print_stats',
        # 'submit1',
        # 'submit2',
    ]
    #run_samples(p1, p2, cmds, __file__)
    run(get_year(), get_day(), p1, p2, cmds, FILE=__file__)
