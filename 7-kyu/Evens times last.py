# DESCRIPTION:
# Given a sequence of integers, return the sum of all the integers that have an even index (odd index in COBOL), multiplied by the integer at the last index.

# Indices in sequence start from 0.

# If the sequence is empty, you should return 0.

def even_last(numbers):
    s = 0
    for i, dig in enumerate(numbers):
        if i % 2 == 0:
            s += dig
    if numbers: return s * numbers[-1]
    else: return 0  
