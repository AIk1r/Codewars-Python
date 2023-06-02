def j_a(n):
    j = [0]
    a = [1]
    for i in range(1, n):
        j.append((i - a[j[i-1]])) 
        a.append((i - j[a[i-1]]))
    return j, a

def john(n):
    return j_a(n)[0]
    
def ann(n):
    return j_a(n)[1]
    
def sum_john(n):
    return sum(john(n))
    
def sum_ann(n):
    return sum(ann(n))
