def bingo(ticket,win):
    l = []
    count = 0
    for i in ticket:
        row = []
        l.append(row)
        for j in i[0]:
            row.append(ord(j))
        if i[1] in row:
            count += 1
    if win <= count:
        return 'Winner!'
    else: return 'Loser!'
