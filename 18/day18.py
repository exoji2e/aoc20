#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 18
def get_year(): return 2020

def evl(line):
    stack = []
    repl = []
    for i, c in enumerate(line):
        if '(' == c:
            stack.append(i)
        if ')' == c:
            j = stack.pop()
            if len(stack) == 0:
                V = evl(line[j+1:i])
                repl.append((j, i, V))
    for s, e, v in repl[::-1]:
        line = line[:s] + str(v) + line[e+1:]
    
    for i in range(len(line)-1, -1, -1):
        if line[i] == '*':
            return evl(line[:i]) * int(line[i+1:])
        if line[i] == '+':
            return evl(line[:i]) + int(line[i+1:])

    return eval(line)

def evl2(line):
    stack = []
    repl = []
    for i, c in enumerate(line):
        if '(' == c:
            stack.append(i)
        if ')' == c:
            j = stack.pop()
            if len(stack) == 0:
                V = evl2(line[j+1:i])
                repl.append((j, i, V))
    for s, e, v in repl[::-1]:
        line = line[:s] + str(v) + line[e+1:]
    
    if '*' in line:
        idx = line.find('*')
        return evl2(line[:idx]) * evl2(line[idx+1:])
    if '+' in line:
        idx = line.find('+')
        return evl2(line[:idx]) + evl2(line[idx+1:])
    return int(line)

def p1(v):
    lines = get_lines(v)
    SU = 0
    for line in lines:
        SU += evl(line.replace(' ', ''))
    return SU

def p2(v):
    lines = get_lines(v)
    SU = 0
    for line in lines:
        SU += evl2(line.replace(' ', ''))
    return SU


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
