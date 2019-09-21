def wab(n,k):
    l = [1, 1]
    for i in range(2,n):    
        l.append(l[i-1]+(k*l[i-2]))
    return l[n-1]

print wab(33,2)