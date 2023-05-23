def is_ruby_coming(lst): 
    return any(i['language'] == 'Ruby' for i in lst)
