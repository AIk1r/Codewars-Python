def unused_digits(*numbers):
    return ''.join(i for i in '0123456789' if i not in str(numbers))
