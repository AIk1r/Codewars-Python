def balance(left, right):
    d = {'!': 2, '?': 3}
    sum_left = sum(d[l] for l in left)
    sum_right = sum(d[r] for r in right)
    
    if sum_left > sum_right: return 'Left'
    elif sum_left == sum_right: return 'Balance'
    else: return 'Right'
