ax=list(map(int,input().split()))
a=input().split()
z=[]
k=ax[1]
n=ax[0]
for i in range(0,n):
    c=0
    for j in range(0,n):
        if a[i]==a[j]:
            c=c+1
    if c<k:
        z.append(a[i])
z=list(dict.fromkeys(z))
z=sorted(z)
print(*z)
