ax=list(map(int,input().split()))
a=list(map(int,input().split()))
a.sort()
c=[]
for i in range(ax[1],ax[2]+1):
    if i>=ax[1] and i<=ax[2]:
        c.append(i)
print(min(c))
