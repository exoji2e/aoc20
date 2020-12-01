#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from main import run
from utils import *
def get_day(): return 1
def get_year(): return 2020

def p1(v):
    lines = get_lines(v)
    S = 0
    ints = [int(line) for line in lines]
    for i in range(len(ints)):
        for j in range(i+1, len(ints)):
            if ints[i] + ints[j] == 2020:
                return ints[i]*ints[j]


    return 0

def p2(v):
    lines = get_lines(v)
    S = 0
    ints = [int(line) for line in lines]
    for i in range(len(ints)):
        for j in range(i+1, len(ints)):
            for k in range(j+1, len(ints)):
                if ints[i] + ints[j] + ints[k] == 2020:
                    return ints[i]*ints[j]*ints[k]


if __name__ == '__main__':
    cmds = [
        'run1',
        'run2',
        'print_stats',
        'run_samples',
        # 'submit1',
        # 'submit2',
    ]
    run(get_year(), get_day(), p1, p2, cmds, FILE=__file__)
