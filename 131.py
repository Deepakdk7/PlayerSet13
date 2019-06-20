ax=list(input())
c=0
ax=list(map(int,ax))
for i in ax:
    if i%2!=0:
        c=c+i
if c%2==0:
    print('E')
else:
    print('O')
