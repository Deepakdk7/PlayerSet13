ax=int(input())
for i in range(0,ax+1):
    if 2**i==ax:
        print('yes')
        break
else:
    print('no')
