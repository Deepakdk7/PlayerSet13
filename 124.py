ax=int(input())
a=list(map(int,input().split()))
i=1
b=0
while b==0:
    for n in a:
        if i%n!=0:
            i=i+1
            break
    else:
        b=1
        print(i)
