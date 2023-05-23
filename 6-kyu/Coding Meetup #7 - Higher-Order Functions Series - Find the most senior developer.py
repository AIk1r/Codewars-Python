def find_senior(lst):
    dig = [i['age'] for i in lst]
    dig.sort()
    
    res = []
    for i in lst:
        if dig[-1] == i['age']:
            res.append(i)
    return res
