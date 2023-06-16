def disemvowel(string):
    s = 'aAeEiIoOuU'
    for i in range(len(s)):
        string = string.replace(s[i],"")
    return string
