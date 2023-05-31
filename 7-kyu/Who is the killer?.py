def killer(suspect_info, dead):
    for k, v in suspect_info.items():
        if set(dead).issubset(set(v)):
            return k
