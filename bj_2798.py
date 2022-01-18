n,m = map(int, input().split(" "))
a = list(map(int, input().split()))

sum=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            result = a[i]+a[j]+a[k]
            if result <= m:
                sum = max(sum,result)
print(sum)
