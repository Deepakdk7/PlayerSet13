ax=list(map(int,input().split()))
a=list(map(int,input().split()))
k=ax[1]
c=0
for i in a:
    if k==i:
        c=c+1
if c>0:
    print('yes',c)
else:
    print('no')
