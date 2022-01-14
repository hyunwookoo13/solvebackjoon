n = int(input())
for i in range(n):
    k=i+1
    print(("*"*k)+(" "*(n-k))+(" "*(n-k))+("*"*k))
for j in range(n,0,-1):
    k=j-1
    print(("*"*k)+(" "*(n-k))+ (" "*(n-k))+("*"*k))
    