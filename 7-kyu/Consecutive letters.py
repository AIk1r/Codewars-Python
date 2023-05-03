def solve(st):
    arr = list(st)
    arr.sort()

    letters = 'abcdefghijklmnopqrstuvwxyz'

    return letters.count(''.join(arr)) >= 1
