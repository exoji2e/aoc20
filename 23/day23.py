#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 23
def get_year(): return 2020

def move_fst(curr, mp):
    a = mp[curr]
    b = mp[a]
    c = mp[b]
    end = mp[c]
    dst = curr
    while dst in [curr, a, b, c]:
        dst -= 1
        if dst == 0:
            dst = len(mp)
        
    nxt = mp[dst]
    mp[curr] = end
    mp[dst] = a
    mp[c] = nxt
    return mp[curr], mp


def p1(v):
    q = [int(c) for c in v]
    mp = {}
    for i in range(len(q)):
        mp[q[i]] = q[(i+1)%len(q)]
    curr = q[0]
    for _ in range(100):
        curr, mp = move_fst(curr, mp)
    
    s = []
    c = 1
    for _ in range(len(mp) - 1):
        c = mp[c]
        s.append(c)

    return ''.join(map(str, s))


def p2(v):
    mp = {}
    q = [int(c) for c in v]
    while len(q) < 10**6:
        q.append(len(q) + 1)
    
    for i in range(len(q)):
        mp[q[i]] = q[(i+1)%10**6]
    c = q[0]

    for _ in range(10**7):
        c, mp = move_fst(c, mp)

    return mp[1]*mp[mp[1]]
        



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
