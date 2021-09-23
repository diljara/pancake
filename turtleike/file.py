def away(n):
    a=[]
    b=[]
    n=n.replace('(','')
    n=n.replace(')','')
    a=n.split(', ')
    print(len(a))
    for i in range (len(a)//2):
        b.append([a[2*i], a[2*i+1]])
    return b


print(away('(0, 200), (90, 100), (90, 200), (90, 100), (90, 0)'))

