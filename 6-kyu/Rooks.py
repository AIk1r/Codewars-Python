def rooks(n, k):
    ans = 1
    for i in range(k):
        ans *= n * n
        n -= 1
        ans //= (i+1)
    return ans
