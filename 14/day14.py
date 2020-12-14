#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 14
def get_year(): return 2020

def getMask(line):
    msk = line.split()[-1]
    zeroMsk = 0
    oneMsk = 0
    for i in range(36):
        if msk[35-i] == '1':
            oneMsk |= (1<<i)
        elif msk[35-i] == '0':
            zeroMsk |= (1<<i)
    return oneMsk, zeroMsk

def getAddrVal(line):
    l = line.replace('[', ' ').replace(']', ' ')
    arr = l.split()
    addr = int(arr[1])
    value = int(arr[-1])
    return addr, value


def p1(v):
    lines = get_lines(v)
    chunks = v.split('\n\n')
    mem = Counter()
    for line in lines:
        if line[:4] == 'mask':
            oneMsk, zeroMsk = getMask(line)
        else:
            addr, value = getAddrVal(line)
            value2 = (value | oneMsk | zeroMsk) ^ zeroMsk
            mem[addr] = value2
    return sum(mem.values())
# not 1239276646133
# not 26272648022616

def p2(v):
    lines = get_lines(v)
    chunks = v.split('\n\n')
    currOnes = set()
    currZero = set()
    mem = Counter()
    for line in lines:
        if line[:4] == 'mask':
            oneMsk, zeroMsk = getMask(line)
            XMsk = (2**36 - 1) ^ oneMsk ^ zeroMsk
            xs = []
            for i in range(36):
                if (1<<i) & XMsk != 0:
                    xs.append(i)
        else:
            addr, value = getAddrVal(line)
            addr |= oneMsk
            for i in range(1<<len(xs)):
                add = 0
                rm = 0
                for a in range(len(xs)):
                    if i & (1<<a) != 0:
                        add |= (1<<xs[a])
                    else:
                        rm |= (1<<xs[a])
                addr2 = (addr | add | rm) ^ rm
                mem[addr2] = value

    return sum(mem.values())


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
