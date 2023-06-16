def square_digits(num):
    n = ''
    for i in str(num):
        n += str(int(i)**2)
    return int(n)
