#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 4
def get_year(): return 2020

need = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
def p1(v):
    ports = v.split('\n\n')
    cnt = 0
    for port in ports:
        things = port.split()
        found = set()
        for t in things:
            found.add(t[:3])
        ok = True
        for v in need:
            if v not in found:
                ok = False
        if ok:
            cnt +=1 
    return cnt

def inside(field, lo, hi):
    try:
        x = int(field)
        if not lo <= x <= hi:
            return False
    except:
        return False
    return True

def iscolor(s):
    if s[0] != '#': return False
    for c in s[1:]:
        if not ('0' <= c <= '9' or 'a' <= c <= 'f'):
            return False
    return True

def check_height(h):
    if h[-2:] == 'cm':
        if not inside(h[:-2], 150, 193): return False
    elif h[-2:] == 'in':
        if not inside(h[:-2], 59, 76): return False
    else:
        return False
    return True

def check(found):
    rules = {
        'byr': lambda v: inside(v, 1920, 2002),
        'iyr': lambda v: inside(v, 2010, 2020),
        'eyr': lambda v: inside(v, 2020, 2030),
        'hgt': lambda v: check_height(v),
        'hcl': lambda v: iscolor(v),
        'ecl': lambda v: v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        'pid': lambda v: len(v) == 9 and all('0' <= c <= '9' for c in v)
    }
    for k, r in rules.items():
        if k not in found: return False
        if not r(found[k]): return False

    return True
    
 


def p2(v):
    ports = v.split('\n\n')
    cnt = 0
    for port in ports:
        things = port.split()
        found = {}
        for t in things:
            found[t[:3]] = t[4:]
        if check(found):
            cnt += 1
        
    return cnt



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
