def replace_exclamation(s):
    a = ''
    for i in s:
        if i in 'aeiouAEIOU':
            a += '!'
        else: a += i
    return a
