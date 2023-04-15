def triple_x(s):
    res = []
    res.append((s.find('x'), s.find('xxx')))
    for i in res:
        print(i)
        if i[0] == i[1] and i[0] >= 0 and i[1] >= 0:
            return True
        else: return False
