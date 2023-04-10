# DESCRIPTION:
# Write a function with the signature shown below:

# def is_int_array(arr):
#     return True
# returns true  / True if every element in an array is an integer or a float with no decimals.
# returns true  / True if array is empty.
# returns false / False for every other input.

from decimal import Decimal

def is_int_array(arr):
    try:
        if type(arr) != str:
            return all([type(i) == int for i in arr]) or all([type(i) == float and Decimal(str(i)).as_tuple().exponent*(-1) == 1 for i in arr])
        
        return False
    except:
        return False
