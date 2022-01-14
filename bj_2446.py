n = int(input())
for i in range(n):
    k=i+1
    print((" "*i)+("*"*(n-i))+("*"*(n-k)))
for j in range(n,1,-1):
    p=j-1
    print((" "*(p-1))+("*"*(n-(p-1)))+("*")*(n-p))