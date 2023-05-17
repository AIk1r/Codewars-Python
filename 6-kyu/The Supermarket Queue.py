def queue_time(cust, n):
    tills = [0] * n
    for i in cust:
        tills[0] += i
        tills.sort()
    return max(tills)
