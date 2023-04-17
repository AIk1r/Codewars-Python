# Task
# Write function which validates an input string. If the string is a perfect square return true,false otherwise.

# What is perfect square?
# * We assume that character '.' (dot) is a perfect square (1x1) * Perfect squares can only contain '.' (dot) and optionally '\n' (line feed) characters.
# * Perfect squares must have same width and height -> cpt.Obvious
# * Squares of random sizes will be tested!

def perfect_square(square):
    arr = square.split('\n')
    l = len(arr[0])
    if len(arr) != l:
        return False
    for i in range(len(arr)):
        if len(arr[i]) != l:
            return False
        for j in arr[i]:
            if j != '.':
                return False
    return True
