def diamond(n):
    if n % 2 == 0 or not str(n).isdigit():
        return None
    s = ''
    for i in range(n):
        a = '*'*(i*2+1) if i <= n/2 else '*'*((n-i)*2-1)
        s += ' '*int((n-len(a))/2)+a+'\n'
    return s
