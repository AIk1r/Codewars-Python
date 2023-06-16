def array_diff(a, b):
    for num in b:
        if num in a:
            for j in range(a.count(num)):
                a.remove(num)
    return a
