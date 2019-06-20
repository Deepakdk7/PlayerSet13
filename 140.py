ax=list(input())
c=0
for i in ax:
    if i=='a' or i=='b':
        c=c+1
if c==len(ax):
    print('yes')
else:
    print('no')
