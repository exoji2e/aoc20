#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 19
def get_year(): return 2020

class Rule:
    def __init__(self, line):
        id, match = line.split(': ')
        self.id = int(id)
        if '"' in match:
            self.v = match.replace('"', '')
            self.deps = None
        else:
            g = match.split(' | ')
            self.deps = [[int(x) for x in gg.split()] for gg in g]
            self.v = None
    def __repr__(self):
        if self.deps != None:
            return '{} {}'.format(self.id, self.deps)
        else:
            return '{} "{}"'.format(self.id, self.v)

DP = {}    
def possible(rule, rules):
    if rule.id in DP:
        return DP[rule.id]
    S = set()
    if rule.v != None:
        S.add(rule.v)
        DP[rule.id] = S
        return S
    for g in rule.deps:
        X = set([''])
        for r_id in g:
            X2 = set()
            for curr in possible(rules[r_id], rules):
                for x in X:
                    v = x + curr
                    if len(v) > 96:
                        continue
                    X2.add(v)
            X = X2
        S |= X
    DP[rule.id] = S
    return S

def possible2(rule, rules):
    if rule.id in DP:
        return DP[rule.id]
    S = set()
    if rule.v != None:
        S.add(rule.v)
        DP[rule.id] = S
        return S
    for g in rule.deps:
        if rule.id in [0, 8, 11]:
            print(rule.id, g)

        X = set([''])
        for r_id in g:
            X2 = set()
            for curr in possible2(rules[r_id], rules):
                for x in X:
                    v = x + curr
                    if len(v) > 96:
                        continue
                    X2.add(v)
            X = X2
        S |= X
    DP[rule.id] = S
    return S

def p1(v):
    lines = get_lines(v)
    chunks = v.split('\n\n')
    rules = [Rule(line) for line in get_lines(chunks[0])]
    rules.sort(key=lambda r: r.id)
    S = possible(rules[0], rules)
    no = 0
    for line in get_lines(chunks[1]):
        if line in S:
            no += 1
    return no

def prefixes(line, S, fn):
    p = {0 : 0}
    ch = True
    while ch:
        ch = False
        p2 = dict(p)
        for s, no in p.items():
            for e in range(s+1, len(line)+1):
                if line[s:e] in S:
                    if e not in p2 or fn(p2[e], no+1) != p2[e] :
                        p2[e] = no + 1
                        ch = True
        p = p2

    return p


def p2(v):
    lines = get_lines(v)
    chunks = v.split('\n\n')
    rules = [Rule(line) for line in get_lines(chunks[0])]
    rules.sort(key=lambda r: r.id)
    """
    for i in range(2, 96):
        if i*8 <= 96:
            rules[8].deps.append([42]*i)
    for i in range(2, 96//2):
        if i*16 <= 96:
            rules[11].deps.append([42]*i + [31]*i)
            """
    ###
    # 0 -> 8 11
    # 8 -> 42+
    # 11 -> 42{k} 31{k}
    # ....
    # 0 -> 42{a} 31{b}, a < b 

    S = possible(rules[0], rules)
    s42 = DP[42]
    s31 = DP[31]
    s31Rev = set()
    for a in s31:
        s31Rev.add(a[::-1])
    cnt = 0
    for line in get_lines(chunks[1]):
        p = prefixes(line, s42, max)
        s = prefixes(line[::-1], s31Rev, min)
        for i in range(1, len(line)):
            j = len(line) - i
            if i in p and j in s:
                no42 = p[i]
                no31 = s[j]
                if no42 > no31:
                    cnt += 1
                    break


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
