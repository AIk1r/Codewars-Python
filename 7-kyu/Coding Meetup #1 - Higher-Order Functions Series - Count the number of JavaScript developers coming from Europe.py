def count_developers(lst):
    count = 0
    for i in lst:
        if i['continent'] == 'Europe' and i['language'] == 'JavaScript':
            count += 1
    return count
