ax=int(input())
a=list(map(int,input().split()))
c=[]
d=[]
if ax%2==0:
    n=ax//2
else:
    n=(ax-1)//2
for i in range(0,n):
    c.append(a[i])
for i in range(n,len(a)):
    d.append(a[i])
c.sort()
d.sort(reverse=True)
print(*c+d)
