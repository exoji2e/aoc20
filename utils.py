# String parsing
def get_ints(v):
    return [int(x) for x in v.split()]

def get_lines(data):
    return data.strip('\n').split('\n')

def multi_split(s, schars):
    out = []
    curr = ''
    for c in s:
        if c in schars:
            if curr:
                out.append(curr)
                curr = ''
        else:
            curr += c
    if curr: out.append(curr)
    return out

def lazy_ints(arr):
    out = []
    for v in arr:
        if is_integer(v):
            out.append(int(v))
        else:
            out.append(v)
    return out

# Grids
def grid_neigh(r, c):
    return [(r-1, c), (r, c-1), (r, c+1), (r+1, c)]
def grid_diag_neigh(r, c):
    o = []
    for rr in range(r-1, r+2):
        for cc in range(c-1, c+2):
            if (rr, cc) != (r, c):
                o.append((rr, cc))
    return o

def is_integer(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


def print_stats(v):
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