# Task
# Write a function that returns true if the number is a "Very Even" number.
# If a number is a single digit, then it is simply "Very Even" if it itself is even.
# If it has 2 or more digits, it is "Very Even" if the sum of its digits is "Very Even".

def is_very_even_number(n):
    res = sum([int(i) for i in str(n)])
    while len(str(res)) != 1:
        res = (sum([int(i) for i in str(res)]))
    return res % 2 == 0
