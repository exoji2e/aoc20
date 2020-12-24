#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 20
def get_year(): return 2020

def p1(v):
    lines = get_lines(v)
    chunks = v.split('\n\n')
    tiles = []
    allB = set()
    for chunk in chunks:
        lines = get_lines(chunk)
        id = int(lines[0].split()[1][:-1])
        borders = []
        lines = lines[1:]
        sTop = lines[0]
        sBot = lines[-1]
        sLeft = ''.join(line[0] for line in lines)
        sRight = ''.join(line[-1] for line in lines)
        borders = [sTop, sLeft, sBot, sRight]
        for b in borders:
            allB.add(b)
        tiles.append((id, borders))
    #print(len(tiles)*4, len(allB))
    edgs = defaultdict(list)
    cnt = Counter()
    for i, b in tiles:
        for j, b2 in tiles:
            if i == j: continue
            for ii, e in enumerate(b):
                for jj, e2 in enumerate(b2):
                    if e == e2:
                        edgs[i, ii].append((j, jj, 0))
                        cnt[i] += 1
                    if e == e2[::-1]:
                        edgs[i, ii].append((j, jj, 1))
                        cnt[i] += 1
    keys = list(cnt.keys())
    keys = sorted(keys, key=lambda k: cnt[k])
    p = 1
    for k in keys[:4]:
        p *= k
    
    return p

def getEdgs(tiles):
    edgs = defaultdict(list)
    cnt = Counter()
    for i, b, _ in tiles:
        for j, b2, _ in tiles:
            if i == j: continue
            for ii, e in enumerate(b):
                for jj, e2 in enumerate(b2):
                    if e == e2 or e == e2[::-1]:
                        edgs[i].append((j, ii, jj, e!= e2))
                        cnt[i] += 1
    return edgs, cnt

def neighs(x, y, sz):
    return [(xx, yy) for xx, yy in grid4n(x, y) if (0 <= xx < sz and 0 <= yy < sz)]

def getGrid(tiles):
    edgs, cnt = getEdgs(tiles)

    keys = list(cnt.keys())
    keys = sorted(keys, key=lambda k: cnt[k])
    sz = int(len(keys)**.5)
    grid = [[-1]*sz for _ in range(sz)]
    grid[0][0] = keys[0]
    used = {keys[0] : (0, 0)}
    q = [keys[0]]

    while q:
        q2 = []
        for u in q:
            es = [l[0] for l in edgs[u]]
            ngs = neighs(used[u][0], used[u][1], sz)
            for e in es:
                if e in used: continue
                ees = [l[0] for l in edgs[e]]
                for x, y in ngs:
                    if grid[x][y] != -1: continue
                    ok = True
                    n2 = neighs(x, y, sz)
                    ok = len(n2) == len(edgs[e])
                    for xx, yy in n2:
                        if grid[xx][yy] != -1:
                            ok = ok and grid[xx][yy] in ees
                    if ok:
                        grid[x][y] = e
                        used[e] = x, y
                        q2.append(e)
                        break
        q = q2
    return grid

def getTiles(inp):
    chunks = inp.split('\n\n')
    tiles = []

    allB = set()
    for chunk in chunks:
        lines = get_lines(chunk)
        id = int(lines[0].split()[1][:-1])
        borders = []
        lines = lines[1:]
        sTop = lines[0]
        sBot = lines[-1]
        sLeft = ''.join(line[0] for line in lines)
        sRight = ''.join(line[-1] for line in lines)
        borders = [sTop, sLeft, sBot, sRight]
        for b in borders:
            allB.add(b)
        tiles.append((id, borders, lines))
    return tiles

def getTileEdgs(lines):
    sTop = lines[0]
    sBot = lines[-1][::-1]
    sLeft = ''.join(line[0] for line in lines)[::-1]
    sRight = ''.join(line[-1] for line in lines)
    borders = [sTop, sRight, sBot, sLeft]
    return borders

def rot90(tile):
    szR, szC = len(tile), len(tile[0])
    t2 = [''.join(tile[szR-r-1][c] for r in range(szR)) for c in range(szC)]
    return t2

def rots(tile):
    t2 = [line[::-1] for line in tile]
    for i in range(4):
        yield tile
        yield t2
        tile = rot90(tile)
        t2 = rot90(t2)

def match(M, FG, r, c):
    R, C = len(FG), len(FG[0])
    mR, mC = len(M), len(M[0])
    if R < mR + r or C < mC + c: return set()
    out = set()
    for rr in range(mR):
        for cc in range(mC):
            if M[rr][cc] == '#':
                if FG[r+rr][c+cc] != '#': return set()
                out.add((r+rr, c+cc))
    return out

def p2(inp):
    tiles = getTiles(inp)
    edgs, cnt = getEdgs(tiles)
    grid = getGrid(tiles)
    tls = {}
    C = Counter()
    for id, b, full in tiles:
        tls[id] = (b, full) 
        for bb in b:
            C[bb] += 1
            C[bb[::-1]] += 1


    sz = len(grid)
    g2 = defaultdict(lambda: None)
    TILES = []
    for r in range(sz):
        for c in range(sz):
            id = grid[r][c]
            ngs = neighs(r, c, sz)
            before = [v for v in ngs if v < (r, c)]
            
            e = edgs[id]
            LEFT = None
            TOP = None
            for rr, cc in before:
                idB = grid[rr][cc]
                if rr < r:
                    TOP = getTileEdgs(g2[rr,cc])[2][::-1]
                else:
                    LEFT = getTileEdgs(g2[rr,cc])[1][::-1]
            def ok(bord, left, top):
                okTop = bord[0] == top
                if top == None:
                    okTop = C[bord[0]] == 1
                okL = bord[3] == left
                if left == None:
                    okL = C[bord[3]] == 1
                return okTop and okL
            tile = tls[id][1]

            for i, t_rot in enumerate(rots(tile)):
                t_edgs = getTileEdgs(t_rot)
                v = []
                for e in t_edgs:
                    v.append((C[e], e))
                if r == 0 and c == 0 and (i == 2 or i==1): #herpderp
                    continue

                if ok(t_edgs, LEFT, TOP):
                    g2[r, c] = t_rot
                    TILES.append(t_rot)
                    break
            if g2[r, c] == None:
                return 0
    small = []
    for t in TILES:
        t2 = [line[1:-1] for line in t[1:-1]]
        small.append(t2)
    FG = [['' for _ in range(len(small[0])*sz)] for _ in range(len(small[0])*sz)] 
    sz2 = len(small[0])
    for i, t in enumerate(small):
        r = i//sz
        c = i%sz
        for rr in range(len(t)):
            for cc in range(len(t[0])):
                FG[r*sz2+rr][c*sz2+cc] = t[rr][cc]
    #print('\n'.join(''.join(line) for line in FG))
    MONSTER="""                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.split('\n')
    monsters = list(rots(MONSTER))
    taken = set()
    for r in range(len(FG)):
        for c in range(len(FG)):
            for m in monsters:
                taken |= match(m, FG, r, c)
    CHash = ''.join(''.join(line) for line in FG).count('#')
    return CHash - len(taken)
    
    





    


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
