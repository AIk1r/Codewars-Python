def switcher(arr):
    d = {str(i):chr(123-i) for i in range(1, 27)}
    d['27'] = '!'
    d['28'] = '?'
    d['29'] = ' '
    res = ''
    for i in arr:
        res += d[i]
    return res
        
