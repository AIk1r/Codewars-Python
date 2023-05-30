def permute_a_palindrome (input): 
    freq = {}

    for ch in input:
        if ch in freq:
            del freq[ch]
        else:
            freq[ch] = True

    return len(freq) <= 1
