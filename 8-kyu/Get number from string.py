def get_number_from_string(string):
    s = ''
    for i in string:
        if i in '0123456789':
            s += i
    return int(s)
