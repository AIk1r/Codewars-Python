def boredom(staff):
    d = {'accounts': 1,
        'finance': 2,
        'canteen': 10,
        'regulation': 3,
        'trading': 6,
        'change': 6,
        'IS': 8,
        'retail': 5,
        'cleaning': 4,
        'pissing about': 25}
    count = 0
    for i in staff:
        if staff[i] in d:
            count += d[staff[i]]
    
    if count <= 80:
        return 'kill me now'
    elif 80 < count < 100:
        return 'i can handle this'
    else:
        return 'party time!!'
