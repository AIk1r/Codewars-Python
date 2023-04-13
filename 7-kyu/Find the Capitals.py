def capital(capitals): 
    res = []
    for i in capitals:
        if 'state' in i:
            res.append(f'The capital of {i["state"]} is {i["capital"]}')
        else:
            res.append(f'The capital of {i["country"]} is {i["capital"]}')
    return res
