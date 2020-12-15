#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 15
def get_year(): return 2020

def get_no(ints, no):
    D = defaultdict(list)
    for i, x in enumerate(ints): D[x].append(i)
    for i in range(len(ints), no):
        last = ints[-1]
        if len(D[last]) == 1:
            now = 0
        else:
            now = D[last][-1] - D[last][-2]
        ints.append(now)
        D[now].append(i)
    return ints

def p1(v):
    ints = [int(x) for x in v.split(',')]
    return get_no(ints, 2020)[-1]

def p2(v):
    ints = [int(x) for x in v.split(',')]
    return get_no(ints, 30000000)[-1]


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
