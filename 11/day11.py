#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 11
def get_year(): return 2020

def genNeighMap(G, neigh_fn):
    R, C = len(G), len(G[0])
    neighMap = {}
    for r in range(R):
        for c in range(C):
            neighMap[r, c] = neigh_fn(r, c, R, C, G)
    return neighMap

def genNext(G, neighs, update):
    R, C = len(G), len(G[0])
    G2 = [['' for _ in range(C)] for _ in range(R)]
    ch = False
    for r in range(R):
        for c in range(C):
            CNT = Counter()
            for rr, cc in neighs[r, c]:
                CNT[G[rr][cc]] += 1
            ch2, v = update(G[r][c], CNT)
            ch = ch or ch2
            G2[r][c] = v
    return ch, G2

def solver(inp, neigh_fn, update_fn):
    lines = get_lines(inp)
    G = [list(line) for line in lines]
    neighMap = genNeighMap(G, neigh_fn)
    ch = True
    while ch:
        ch, G = genNext(G, neighMap, update_fn)

    return ''.join(''.join(row) for row in G).count('#')


def p1(v):

    def update1(oldV, CNT):
        if oldV == 'L' and CNT['#'] == 0:
            return True, '#'
        elif oldV == '#' and CNT['#'] >= 4:
            return True, 'L'
        else:
            return False, oldV

    def get_neighs_1(r, c, R, C, G):
        neighs = []
        for rr, cc in grid8n(r, c):
            if 0 <= rr < R and 0 <= cc < C:
                neighs.append((rr, cc))
        return neighs

    return solver(v, get_neighs_1, update1)

def p2(v):
    def update2(oldV, CNT):
        if oldV == 'L' and CNT['#'] == 0:
            return True, '#'
        elif oldV == '#' and CNT['#'] >= 5:
            return True, 'L'
        else:
            return False, oldV

    def get_neighs_2(r, c, R, C, G):
        neighs = []
        def walk(r, c, dr, dc):
            while 0 <= r < R and 0 <= c < C:
                if G[r][c] != '.': 
                    neighs.append((r, c))
                    return
                r, c = r + dr, c + dc
            
        for dr, dc in grid8n(0,0):
            walk(r + dr, c + dc, dr, dc)
        return neighs

    return solver(v, get_neighs_2, update2)

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
