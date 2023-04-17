def get_strings(city):
    d = {}
    for i in city.lower():
        if i.isalpha():
            d[i] = '*' * city.lower().count(i)
    return(','.join(k+':'+ v for k, v in d.items()))
