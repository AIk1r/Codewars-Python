def initialize_names(name):
    s = name.split()
    if len(s) <= 2:
        return name
    inic = ''
    res = []
    for i in s[1:-1]:
        inic += i[0] + '.'
        res.append(inic)
        inic = ''
    return f"{s[0]} {' '.join(res)} {s[-1]}" 
