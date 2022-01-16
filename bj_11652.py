import sys
n = int(sys.stdin.readline())

a = dict()

for i in range(n):
    b = int(sys.stdin.readline())
    if b in a:
        a[b] +=1
    else:
        a[b] = 1

a = sorted(a.items(), key = lambda x : (-x[1],x[0]))
print(a[0][0])
