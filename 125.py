ax=int(input())
a=list(map(int,input().split()))
c=0
for i in range(1,max(a)+1):
    for n in a:
        if n%i!=0:
            break
    else:
        c=i
print(c)
