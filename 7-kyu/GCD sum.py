def solve(s,g):
    for i in range(g, s+1, g):
        remainder = s - i
        if remainder % g == 0:
            return (i, remainder)
    return -1
