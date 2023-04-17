def data_reverse(data):
    l = []
    res = []
    for i in range(0, len(data),8):
        l.append(data[i:i+8])
    for i in reversed(l):
        res.extend(i)
    return res
