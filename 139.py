ax=int(input())
a=bin(ax)[2:]
c=0
for i in a:
    if i=='1':
        c=c+1
print(c)
