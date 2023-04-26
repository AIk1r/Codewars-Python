import re
def is_digit(n):
    res = re.findall(r'[\d]', n)
    return res[0] == n if res else False
