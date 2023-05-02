def all_non_consecutive(arr):
    out = []
    for i, num in enumerate(arr[1:]):
        if num != (arr[i]+1):
            out.append({'i': i+1, 'n': num})
    return out
