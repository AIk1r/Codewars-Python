def digit_sum(n):
    sum = 0
    for i in str(n):
        if int(i) > 0:
            sum += int(i)
    return sum
