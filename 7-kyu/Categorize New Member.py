def open_or_senior(data):
    m = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            m.append('Senior')
        else:
            m.append('Open')
    return m 
