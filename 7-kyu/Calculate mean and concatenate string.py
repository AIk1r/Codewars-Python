def mean(lst):
    string = ''
    digit = 0
    count = 0
    
    for i in lst:
        if i.isdigit():
            count += 1
            digit += int(i)
        elif i.isalpha():
            string += i
            
    return [digit/count, string]
