from collections import Counter

def count_languages(lst): 
    return Counter([i['language'] for i in lst])
