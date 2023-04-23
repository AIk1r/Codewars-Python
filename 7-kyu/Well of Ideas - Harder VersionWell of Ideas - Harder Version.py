def well(arr):
    res = []
    for i in arr:
        res.extend(i)
    
    count = 0
    for i in res:
        if str(i).lower() == 'good':
            count += 1
            
    if 0 < count <= 2: return 'Publish!'
    elif count >= 3: return 'I smell a series!'
    else: return 'Fail!'
    
