#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 9
def get_year(): return 2020

def has_pair(t, S):
    for i in range(len(S)):
        for j in range(i+1, len(S)):
            if S[i] + S[j] == t:
                return True
    return False
def p1(v):
    lines = get_lines(v)
    chunks = v.split('\n\n')
    nos = [int(l) for l in lines]
    sz = 25
    items = deque(nos[:sz])
    invalid = set()
    for i in range(sz, len(nos)):
        if not has_pair(nos[i], items):
            return nos[i]
        items.popleft()
        items.append(nos[i])

    return -1

def p2(v):
    invalid = p1(v)
    if invalid == -1: return -1
    nos = [int(l) for l in get_lines(v)]
    pre = [0]
    for i in nos:
        pre.append(pre[-1] + i)
    for i in range(len(nos)):
        for j in range(i+2,len(pre)):
            V = pre[j] - pre[i]
            if V > invalid: break
            if pre[j] - pre[i] == invalid:
                items = nos[i:j]
                return min(items) + max(items)
    return -1


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
