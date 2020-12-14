#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 13
def get_year(): return 2020

def p1(v):
    lines = get_lines(v)
    chunks = v.split('\n\n')
    S = int(lines[0])
    OS = S
    buss = [int(ch) for ch in lines[1].split(',') if ch != 'x']
    while True:
        for b in buss:
            if S%b == 0:
                return (S - OS)*b
        S += 1

    return 0

def xgcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = (a // b, b, a % b)
        x0, x1 = (x1, x0 - q * x1)
        y0, y1 = (y1, y0 - q * y1)
    return (a, x0, y0)


def gcd(a, b):
    return a if b == 0 else gcd(b, a%b)

def crt(la, ln):
    assert len(la) == len(ln)
    for i in range(len(la)):
        assert 0 <= la[i] < ln[i]
    prod = 1
    for n in ln:
        assert gcd(prod, n) == 1
        prod *= n
    lN = []
    for n in ln:
        lN.append(prod//n)
    x = 0
    for i, a in enumerate(la):
        _, Mi, mi = xgcd(lN[i], ln[i])
        x += a*Mi*lN[i]
    return x % prod


def p2(v):
    lines = get_lines(v)
    S = int(lines[0])
    OS = S
    buss = [(int(ch), i%int(ch)) for i, ch in enumerate(lines[1].split(',')) if ch != 'x']
    X = crt([(-i)%b for b, i in buss], [b for b, _ in buss])
    
    return X


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
