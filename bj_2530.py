h,m,s = map(int, input().split(' '))
ms = int(input())

a = s+ms
n_ms= a%60 
mt= a//60
k = m+mt
nh = h+ (k//60)
nm = k%60

if nh >= 24:
    nh = nh%24
    print(nh,nm,n_ms,sep=" ")
else:
    print(nh,nm,n_ms,sep=" ")