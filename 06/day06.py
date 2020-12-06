#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 6
def get_year(): return 2020

def p1(v):
    lines = get_lines(v)
    chunks = v.split('\n\n')
    C = 0
    X = None
    for ch  in chunks:
        s = ''.join(x for x in ch.split())
        C += len(set(s))
    return C

def p2(v):
    chunks = v.split('\n\n')
    C = 0
    for ch  in chunks:
        V = [x.strip() for x in ch.split()]
        cnt = 0
        for v in V[0]:
            if all(v in L for L in V):
                cnt += 1
        C += cnt

    return C


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
