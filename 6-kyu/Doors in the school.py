def doors(n):
    d = {i: False for i in range(0, n)}
    for a in range(0,n):
        for b in range(a,n,a+1):
            d[b] = not d[b]
    result = 0
    for i in d.values():
        if i == True:
            result += 1
    return result
