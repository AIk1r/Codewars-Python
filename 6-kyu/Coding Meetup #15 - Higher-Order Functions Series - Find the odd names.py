def find_odd_names(lst):
    res = []
    for i in lst:
        if sum(map(ord, i['firstName'])) % 2:
            res.append(i)
    return res
