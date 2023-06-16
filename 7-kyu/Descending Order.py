def descending_order(num):
    rev_num = "".join(sorted(str(num), reverse=True))
    return int(rev_num)
