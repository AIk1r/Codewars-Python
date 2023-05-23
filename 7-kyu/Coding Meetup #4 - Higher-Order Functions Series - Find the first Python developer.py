def get_first_python(users):
    res = []
    for i in users:
        if i['language'] == 'Python':
            res.append(f'{i["first_name"]}, {i["country"]}')
    return res[0] if res else 'There will be no Python developers'
