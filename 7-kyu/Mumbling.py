def accum(s):
    count = 0
    result = ''
    for i in s:
        count += 1
        result += i.upper()
        for x in range(count - 1):
            result += i.lower()
        if count < len(s):
            result += '-'
    return result
