def solution(s):
    r = ''
    for i in s:
        if i.isupper():
            r += ' '
        r += i
    return(r)
