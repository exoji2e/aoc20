#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples
from utils import *
def get_day(): return datetime.date.today().day
def get_year(): return 2020

def p1(v):
    lines = get_lines(v)
    return 0

def p2(v):
    lines = get_lines(v)
    return 0


if __name__ == '__main__':
    cmds = [
        'run1',
        'run2',
        'print_stats',
        #'submit1',
        #'submit2',
    ]
    run_samples(p1, p2, cmds, __file__)
    run(get_year(), get_day(), p1, p2, cmds, FILE=__file__)
