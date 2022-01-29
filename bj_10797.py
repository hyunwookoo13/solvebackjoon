n = int(input())
arr = list(map(int, input().split()))
count = 0
for i in arr:
    if n == i:
        count +=1

print(count)