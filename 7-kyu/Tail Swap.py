def tail_swap(strings):
    a, b = strings[0], strings[1]
    a, b = a.split(':'), b.split(':')
    return [f'{a[0]}:{b[1]}', f'{b[0]}:{a[1]}']
