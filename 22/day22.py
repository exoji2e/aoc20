#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 22
def get_year(): return 2020

def rec(p1, p2):
    seen = set()
    while p1 and p2:
        T = tuple(p1), tuple(p2)
        if T in seen:
            return p1, []
        seen.add(T)
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        win1 = c1 > c2
        if c1 <= len(p1) and c2 <= len(p2):
            v1 = p1[:c1]
            v2 = p2[:c2]
            v1, v2 = rec(v1, v2)
            if v1:
                win1 = True
            else:
                win1 = False
        if win1:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)
    return p1, p2


def p1(v):
    lines = get_lines(v)
    chunks = v.split('\n\n')
    p1 = deque(lazy_ints(get_lines(chunks[0])[1:]))
    p2 = deque(lazy_ints(get_lines(chunks[1])[1:]))
    r = 0
    while p1 and p2:
        r += 1
        c1 = p1.popleft()
        c2 = p2.popleft()
        if c1 < c2:
            p2.append(c2)
            p2.append(c1)
        else:
            p1.append(c1)
            p1.append(c2)

    score = 0
    winner = p1 if p1 else p2
    for i in range(1, len(winner)+1):
        score += i * winner[-i]

    return score

def p2(v):
    lines = get_lines(v)
    chunks = v.split('\n\n')
    p1 = lazy_ints(get_lines(chunks[0])[1:])
    p2 = lazy_ints(get_lines(chunks[1])[1:])
    p1, p2 = rec(p1, p2)
    score = 0
    winner = p1 if p1 else p2
    for i in range(1, len(winner)+1):
        score += i * winner[-i]

    return score

    


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
