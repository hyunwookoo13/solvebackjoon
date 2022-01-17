t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())

    live = [x for x in range(1, n+1)]

    for i in range(k):
         for j in range(1,n):
             live[j] += live[j-1]
    print(live[-1])
