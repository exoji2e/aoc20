#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 21
def get_year(): return 2020

def parse(inp):
    lines = get_lines(inp)
    all2inglist = defaultdict(list)
    ingC = Counter()
    for line in lines:
        ings, allg = line.split(' (contains ')
        allg = multi_split(allg, ' ),')
        ings = ings.split()
        for a in allg:
            all2inglist[a].append(set(ings))
        for i in ings:
            ingC[i] += 1
    return all2inglist, ingC


def p1(v):
    all2inglist, ingC = parse(v)

    possible = set()
    for a, L in all2inglist.items():
        v = L[0]
        for l in L:
            v &= l
        possible |= v
    no = 0
    for k, v in ingC.items():
        if k not in possible:
            no += v
    return no

def p2(v):
    all2inglist, ingC = parse(v)

    X = {}
    for a, L in all2inglist.items():
        v = L[0]
        for l in L:
            v &= l
        X[a] = v
    pairs = {}
    while X:
        k, S = next((k, v) for (k, v) in X.items() if len(v) == 1)
        m = S.pop()
        pairs[k] = m
        del X[k]
        for k, S in X.items():
            if m in S:
                S.remove(m)
    itms = sorted(pairs.items())
    out = [v for _, v in itms]
    return ','.join(out)



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
