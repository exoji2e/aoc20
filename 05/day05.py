#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 5
def get_year(): return 2020

def parse(line):
    r = int(line[:7].replace('F', '0').replace('B', '1'), 2)
    c = int(line[7:].replace('L', '0').replace('R', '1'), 2)
    return r*8 + c

def p1(v):
    lines = get_lines(v)
    mx = 0
    for line in lines:
        mx = max(mx, parse(line))
    return mx

def p2(v):
    lines = get_lines(v)
    seats = set()
    for line in lines:
        seats.add(parse(line))

    for i in range(min(seats), max(seats)):
        if i not in seats:
            return i


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
