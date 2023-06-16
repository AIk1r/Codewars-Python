def high_and_low(numbers):
    high = max([int(x) for x in numbers.split()])
    low = min([int(x) for x in numbers.split()])
    result = str(high) +' '+ str(low)
    return result
