def who_is_online(friends):
    d = {}
    online = []
    offline = []
    away = []
    for i in friends:
        print(i)
        if i['last_activity'] > 10 and i['status'] == 'online':
            away.append(i['username'])
            d['away'] = away
        elif i['status'] == 'offline':
            offline.append(i['username'])
            d[i['status']] = offline
        else:
            online.append(i['username'])
            d[i['status']] = online
    return d
