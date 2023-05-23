def is_same_language(lst): 
    r = ''
    res = []
    for i in lst:
        r = i['language']
        res.append(i['language'])
    return all(i == r for i in res)
