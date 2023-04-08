def solution(pairs):
    l = []
    for k, v in pairs.items():
        l.append(f'{k} = {v}')
    l.sort()
    return ','.join(l)
