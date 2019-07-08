n,m=list(map(int,input().split()))
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
for i in a:
    if m in i:
        print('yes')
        break
else:
    print('no')
