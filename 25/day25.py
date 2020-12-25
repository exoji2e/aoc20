#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 25
def get_year(): return 2020

def get_loop_size(target):
    subj = 7
    M = 20201227
    v = 1
    i = 0
    while v != target:
        v = (v*subj)%M
        i += 1
    return i

def get_enc(subj, no):
    M = 20201227
    v = 1
    for _ in range(no):
        v = (v*subj)%M
    return v

def p1(v):
    lines = get_lines(v)
    assert 8 == get_loop_size(5764801)
    a, b = lazy_ints(lines)
    l1 = get_loop_size(a)
    enc1 = get_enc(b, l1)

    return enc1

def p2(v):
    return 'Merry X-mas!'


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
