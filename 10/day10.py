#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 10
def get_year(): return 2020

def p1(v):
    lines = get_lines(v)
    S = [0] + lazy_ints(lines)
    
    S.sort()

    o = 0
    t = 1
    for i in range(len(S) - 1):
        if S[i] == S[i+1] - 1:
            o += 1
        if S[i] == S[i+1] - 3:
            t += 1
    return o*t

def p2(inp):
    lines = get_lines(inp)
    S = lazy_ints(lines)
    
    S.sort()
    DP = [0]*(max(S) + 1)
    DP[0] = 1
    for v in S:
        v1, v2, v3 = DP[v-1], 0 if v == 1 else DP[v-2], 0 if v < 3 else DP[v-3]
        DP[v] = v1 + v2 + v3

    return DP[-1]


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
