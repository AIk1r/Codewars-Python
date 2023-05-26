def vampire_test(a, b):    
    ab = list(str(a) + str(b))
    ab_sorted = ''.join(sorted(ab))
    prod = list(str(a * b))
    prod_sorted = ''.join(sorted(prod))
    return ab_sorted == prod_sorted
