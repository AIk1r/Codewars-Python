# DESCRIPTION:
# Given a variable n,

# If n is an integer, Return a string with dash'-'marks before and after each odd integer, but do not begin or end the string with a dash mark. If n is negative, then the negative sign should be removed.

# If n is not an integer, return the string "None".

def dashatize(n):
    s = ''
    l = []
    
    if type(n) != int:
        return 'None'
    
    for i in str(n):
        if i.isdigit():
            if int(i) % 2 != 0:
                s += '-'+ i +'-'
            else:
                s += i
    for i in s.split('-'):
        if i != '':
            l.append(i)
    return('-'.join(l))
