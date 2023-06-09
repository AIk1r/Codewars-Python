def xo(s):
    countx = 0
    counto = 0
    for char in s:
        if char == 'x' or char == 'X':
            countx += 1
        elif char == 'o' or char == 'O':
            counto += 1
    if countx == counto:
        return True
    else:
        return False
