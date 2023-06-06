def diagonal_sum(array):
    sum_main = 0
    for i in range(len(array)):
        sum_main += array[i][i]
    return(sum_main)
