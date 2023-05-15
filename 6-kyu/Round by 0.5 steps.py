import math
def solution(n):
    f = math.floor(n)
    c = math.ceil(n)
    if n - f < 0.25:
        return f
    elif n - (f+0.5) >= 0.25:
        return c
    return f + 0.5
        
