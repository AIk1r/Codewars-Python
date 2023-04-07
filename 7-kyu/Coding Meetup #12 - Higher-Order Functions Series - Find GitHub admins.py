def find_admin(lst, lang):
    res = []
    for i in lst:
        if i['language'] == lang and i['githubAdmin'] == 'yes':
            res.append(i)
    return res if len(res) != 0 else []
