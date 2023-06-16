def DNA_strand(dna):
    chars = {'A':'T', 'G':'C'}
    char_str = ''
    for i in dna:
        for key, value in chars.items():
            if i == key:
                char_str += value
            elif i == value:
                char_str += key
        
    return char_str
