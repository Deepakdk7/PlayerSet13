ax=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    c=c+i
    if c%2==0:
        print(c,end=' ')
    else:
        print(i,end=' ')
