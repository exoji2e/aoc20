# String parsing
def get_ints(v):
    return [int(x) for x in v.split()]

def get_lines(data):
    return data.strip('\n').split('\n')

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