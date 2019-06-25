ax=int(input())
a=[]
for i in range(0,ax):
    for j in range(0,ax):
        if i*j==ax:
            a.append(i)
            a.append(j)
a=list(dict.fromkeys(a))
a.sort()
for i in a:
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=' ')
