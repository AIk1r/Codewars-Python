def greet_developers(lst): 
    for i in lst:
        i['greeting'] = f'Hi {i["firstName"]}, what do you like the most about {i["language"]}?'
    return lst
