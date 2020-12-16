#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 16
def get_year(): return 2020

from collections import defaultdict
class Flow:
    def __init__(self, sz):
        self.G = [
            defaultdict(int) for _ in range(sz)
        ] # neighbourhood dict, N[u] = {v_1: cap_1, v_2: cap_2, ...}
        self.Seen = set() # redundant
    
    def increase_capacity(self, u, v, cap):
        """ Increases capacity on edge (u, v) with cap. 
            No need to add the edge """
        self.G[u][v] += cap
    
    def max_flow(self, source, sink):
        def dfs(u, hi):
            G = self.G
            Seen = self.Seen
            if u in Seen: return 0
            if u == sink: return hi
            
            Seen.add(u)
            for v, cap in G[u].items():
                if cap >= self.min_edge:
                    f = dfs(v, min(hi, cap))
                    if f:
                        G[u][v] -= f
                        G[v][u] += f
                        return f
            return 0

        flow = 0
        self.min_edge = 2**30 # minimal edge allowed
        while self.min_edge > 0:
            self.Seen = set()
            pushed = dfs(source, float('inf'))
            if not pushed:
                self.min_edge //= 2
            flow += pushed
        return flow

def inside(val, inter):
    lo, hi = map(int, inter.split('-'))
    return lo <= val <= hi

def test(val, rules):
    for rule in rules:
        if inside(val, rule[1]) or inside(val, rule[2]):
            return True
    return False
        
def parse(inp):
    chunks = inp.split('\n\n')
    assert len(chunks) == 3
    rules = chunks[0].split('\n')
    def parseRule(line):
        name = line.split(':')[0]
        arr = line.split()
        f, s = arr[-3], arr[-1]
        return name, f, s
    def toIntList(s):
        return [int(x) for x in s.split(',')]
    your = toIntList(chunks[1].split('\n')[1])
    nearby = [toIntList(line) for line in chunks[2].split('\n')[1:]]
    return [parseRule(line) for line in rules], your, nearby
    


def p1(v):
    rules, your, nearby = parse(v)
    error = 0
    for ticket in nearby:
        for val in ticket:
            if not test(val, rules):
                error += val
    return error

def p2(v):
    rules, your, nearby = parse(v)
    tickets = [your]
    for ticket in nearby:
        ok = True
        for val in ticket:
            if not test(val, rules):
                ok = False
        if ok:
            tickets.append(ticket)
    rls = len(rules)
    sz = rls*2 + 2
    net = Flow(sz)
    for i, rule in enumerate(rules):
        for ti in range(len(tickets[0])):
            ok = True
            for t in tickets:
                if not inside(t[ti], rule[1]) and not inside(t[ti], rule[2]):
                    ok = False
            if ok:
                net.increase_capacity(i, ti + rls, 1)
    for i in range(rls):
        net.increase_capacity(sz-2, i, 1)
        net.increase_capacity(i+rls, sz - 1, 1)
    f = net.max_flow(sz-2, sz-1)
    MP = {}
    for i in range(rls):
        bMap = net.G[rls + i]
        for k, v in bMap.items():
            if v:
                MP[k] = i
    p = 1
    for i, rule in enumerate(rules):
        if 'departure' in rule[0]:
            p *= your[MP[i]]
    return p
            

    


    
        




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
