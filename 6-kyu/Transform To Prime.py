# DESCRIPTION:
# Task :
# Given a List [] of n integers , find minimum number to be inserted in a list, so that sum of all elements of list should equal the closest prime number .

def check_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def minimum_number(numbers):
    sym = sum(numbers)
    while check_prime(sym) != True:
        sym += 1
    return sym - sum(numbers)
