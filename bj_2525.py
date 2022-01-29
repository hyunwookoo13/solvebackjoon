h,m = map(int, input().split(' '))
mt = int(input())

k = m+mt
nh = h+ (k//60)
nm = k%60

if nh >= 24:
    nh = nh%24
    print(nh,nm,sep=" ")
else:
    print(nh,nm,sep=" ")