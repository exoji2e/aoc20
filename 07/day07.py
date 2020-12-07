#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 7
def get_year(): return 2020


def parse(INP):
    lines = get_lines(INP)
    G = defaultdict(list)
    G2 = defaultdict(dict)
    for l in lines:
        k, v = l.split('contain')
        K = ' '.join(k.split()[:2])
        for vs in v.split(','):
            bg = vs.strip()
            if 'no other' in bg:
                break
            ws = bg.split()
            no = ws[0]
            bId = ' '.join(ws[1:3])
            G[bId].append(K)
            G2[K][bId] = int(no)
    return G, G2 


def p1(INP):
    G, _ = parse(INP)
    q = ['shiny gold']
    vis = set(q)
    while q:
        q2 = []
        for u in q:
            for v in G[u]:
                if v not in vis:
                    vis.add(v)
                    q2.append(v)
        q = q2
    return len(vis) - 1

def p2(INP):
    _, G2 = parse(INP)
    q = 'shiny gold'
    DP = {}
    def count(bN):
        if bN in DP:
            return DP[bN]
        c = 1
        for k, no in G2[bN].items():
            c += no*count(k)
        return c

    return count(q) - 1


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
