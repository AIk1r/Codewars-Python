def duplicate_count(text):
    l = set([i for i in text.lower() if text.lower().count(i) > 1])
    return len(l)
