def remainder(a,b):
    try:
        m = max(a, b)
        n = min(a, b)
        return m%n
    except:
        return None
