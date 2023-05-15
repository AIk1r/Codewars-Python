def snail(column, day, night):
    count = 1
    m = day
    while m < column:
        m -= night
        count += 1
        m += day
    return count
