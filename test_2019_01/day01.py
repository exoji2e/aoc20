#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from main import run
from utils import *
def get_day(): return 1
def get_year(): return 2019

def p1(v):
    x = get_ints(v)
    S = 0
    for v in x:
        S += v//3 - 2 
    return S

def p2(v):
    x = get_ints(v)
    x = [int(l) for l in get_lines(v)]
    S = 0
    for v in x:
        while v > 0:
            v = v//3 - 2
            v = max(0, v)
            S += v
    return S


if __name__ == '__main__':
    cmds = [
        'run1',
        'run2',
        'print_stats',
        'run_samples',
         'submit1',
         'submit2',
    ]
    run(get_year(), get_day(), p1, p2, cmds, FILE=__file__)
