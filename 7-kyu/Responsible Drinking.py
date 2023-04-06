# Codewars Bar recommends you drink 1 glass of water per standard drink so you're not hungover tomorrow morning.
# Your fellow coders have bought you several drinks tonight in the form of a string.
# Return a string suggesting how many glasses of water you should drink to not be hungover.

def hydrate(drink_string): 
    res = 0
    for i in drink_string:
        if i in '0123456789':
            res += int(i) 
    return f'{res} glass of water' if res < 2 else f'{res} glasses of water'
