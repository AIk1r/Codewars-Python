def even_chars(st): 
    res = [st[i] for i in range(len(st)) if i % 2]
    return res if 1 < len(st) < 101  else 'invalid string'
