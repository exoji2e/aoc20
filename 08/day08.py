#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 8
def get_year(): return 2020


def exec_instr(vm, ins):
    if vm.i in vm.seen:
        vm.running = False
        return 0
    code = ins[0]
    if code == 'jmp':
        return ins[1] 
    elif code == 'nop':
        pass
    elif code == 'acc':
        vm.reg['acc'] += ins[1]
    else:
        print('unknown instruction code:', code)
        vm.running = False
        return 0
    return 1

def run_prog(prog):
    vm = VM(Counter(), prog, exec_instr)
    vm.exec()
    return vm.i >= len(prog), vm.reg['acc']

def parse_prog(v):
    lines = get_lines(v)
    return [lazy_ints(line.split()) for line in lines]

def p1(v):
    prog = parse_prog(v)
    return run_prog(prog)[1]

def swap(prog, i):
    if prog[i][0] == 'nop':
        prog[i] = 'jmp', prog[i][1]
    elif prog[i][0] == 'jmp':
        prog[i] = 'nop', prog[i][1]

def p2(v):
    prog = parse_prog(v)
    for i in range(len(prog)):
        #print(i, '/', len(prog))
        swap(prog, i)
        ok, acc = run_prog(prog)
        if ok: return acc
        swap(prog, i)


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
