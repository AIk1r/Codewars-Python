# DESCRIPTION:
# You are given a string of n lines, each substring being n characters long: For example:

# s = "abcd\nefgh\nijkl\nmnop"

# We will study some transformations of this square of strings.

# Clock rotation 180 degrees: rot
# rot(s) => "ponm\nlkji\nhgfe\ndcba"
# selfie_and_rot(s) (or selfieAndRot or selfie-and-rot) It is initial string + string obtained by clock rotation 180 degrees with dots interspersed in order (hopefully) to better show the rotation when printed.
# s = "abcd\nefgh\nijkl\nmnop" --> 
# "abcd....\nefgh....\nijkl....\nmnop....\n....ponm\n....lkji\n....hgfe\n....dcba"
# or printed:
# |rotation        |selfie_and_rot
# |abcd --> ponm   |abcd --> abcd....
# |efgh     lkji   |efgh     efgh....
# |ijkl     hgfe   |ijkl     ijkl....   
# |mnop     dcba   |mnop     mnop....
#                            ....ponm
#                            ....lkji
#                            ....hgfe
#                            ....dcba
# Notice that the number of dots is the common length of "abcd", "efgh", "ijkl", "mnop".

# Task:
# Write these two functions rotand selfie_and_rot
# and

# high-order function oper(fct, s) where

# fct is the function of one variable f to apply to the string s (fct will be one of rot, selfie_and_rot)

def rot(strng):
    return(strng[::-1])
def selfie_and_rot(strng):
    res = []
    s = ''
    for i in strng.split():
        s += i + (len(i)*'.')+'\n'
    a = s+s[::-1]
    for i in a.split():
        res.append(i)
    return '\n'.join(res)
def oper(fct, s):
    if fct == rot:
        return rot(s)
    return(selfie_and_rot(s))
