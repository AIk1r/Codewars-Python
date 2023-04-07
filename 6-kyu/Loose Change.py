# Welcome young Jedi!
# In this Kata you must create a function that takes an amount of US currency in cents,
# and returns a dictionary/hash which shows the least amount of coins used to make up that amount.
# The only coin denominations considered in this exercise are: Pennies (1¢), Nickels (5¢), Dimes (10¢) and Quarters (25¢).
#   Therefor the dictionary returned should contain exactly 4 key/value pairs.

# Notes:

# If the function is passed either 0 or a negative number, the function should return the dictionary with all values equal to 0.
# If a float is passed into the function, its value should be rounded down, and the resulting dictionary should never contain fractions of a coin.

def loose_change(cents):
    di = {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    
    if cents < 0:
        return di
    
    while int(cents):
        if cents >= 25:
            q = cents//25
            di['Quarters'] = int(q)
            cents -= 25*q
        elif 10 <= cents < 25:
            d = cents//10
            di['Dimes'] = int(d)
            cents -= 10*d
        elif 5 <= cents < 10:
            n = cents//5
            di['Nickels'] = int(n)
            cents -= 5*n
        elif 0 < cents < 5:
            p = cents//1
            di['Pennies'] = int(p)
            cents -= 1*p
    return(di)
