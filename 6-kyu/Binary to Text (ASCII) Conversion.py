def binary_to_string(binary):
    def grouper(iterable, n):
        args = [iter(iterable)] * n
        return zip(*args)

    l = [''.join(i) for i in grouper(binary, 8)]
    res = [chr(int(i, 2)) for i in l]
    return ''.join(res)
