def binary_array_to_number(arr):
    count = 0
    i = 1
    for num in arr[::-1]:
        count += (i*num)
        i *= 2
    return count
