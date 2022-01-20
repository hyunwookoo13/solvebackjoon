n = list(map(int, input().split(" ")))

sum = 0
for i in range(len(n)):
    a = n[i]
    sum += a**2
print(sum%10)
