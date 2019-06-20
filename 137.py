bx=int(input())
a=list(bin(bx)[::-1])
c=1
for i in a:
    if i=='1':
        print(c)
        break
    else:
        c=c+1
