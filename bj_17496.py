n,t,c,p= map(int,input().split())

count = 0
for i in range(1, n, t):
    if i + t > n:
        break
    count +=1
num = count * c
cal = num *p

print(cal)


