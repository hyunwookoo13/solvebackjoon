n = int(input())
for i in range(n):
    k = i+1
    print((" "*(n-k))+("*"*k))
for j in range(n,0,-1):
    p=j-1
    print((" "*(n-p))+("*"*p))
    