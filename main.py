import argparse
import sys, time, os
from datetime import datetime
import logging as log
import pathlib
sys.path.extend(['..', '.'])
from fetch import fetch, get_samples, get_input_file_name, submit
from utils import get_lines, is_integer

def get_target(YEAR, DAY):
    target = datetime(YEAR, 12, DAY, 6, 0, 0, 100)
    return target

def writeInputToFolder(FILE, content):    
    parent = pathlib.Path(FILE).parent.absolute()
    input_dst = '{}/input.in'.format(parent)
    with open(input_dst,'w') as f:
        f.write(content)

def printStatistics(v):
    lines = get_lines(v)
    print('INPUT[:10]:')
    for line in lines[:10]:
        print('> ' + line)
    if len(lines) > 10:
        print('...')
    tot_tokens = 0
    int_tokens = 0
    for line in lines:
        for tok in line.split():
            tot_tokens += 1
            if is_integer(tok):
                int_tokens += 1
    print('lines: {}, tokens: {}, int_tokens: {}'.format(
        len(lines), tot_tokens, int_tokens))


def run(YEAR, DAY, p1_fn, p2_fn, cmds, FILE=None):
    if 'run_samples' in cmds:
        for fname, data in get_samples(YEAR, DAY):
            print(fname)
            print('p1: ', p1_fn(data))
            print('p2: ', p2_fn(data))
    target = get_target(YEAR, DAY)
    fmt_str = '%(asctime)-15s %(filename)8s:%(lineno)-3d %(message)s'
    log.basicConfig(level=log.DEBUG, format=fmt_str)
    force = 'force_fetch' in cmds
    v = fetch(YEAR, DAY, log, wait_until_date=target, force=force)
    if FILE != None:
        writeInputToFolder(FILE, v)
    if 'debug_print' in cmds:
        printStatistics(v)
    
    if 'run1' in cmds:
        res = p1_fn(v)
        print('part_1: {}'.format(res))
        if 'submit1' in cmds:
            submit(YEAR, DAY, 1, res)
    if 'run2' in cmds:
        res = p2_fn(v)
        print('part_2: {}'.format(res))
        if 'submit2' in cmds:
            submit(YEAR, DAY, 2, res)




