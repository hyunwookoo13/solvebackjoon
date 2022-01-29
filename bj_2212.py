from audioop import reverse
import sys

n = int(input())
k = int(input())

if  k >= n:
    print(0)
    sys.exit()

arr = list(map(int, input().split(" ")))
arr.sort()

distances = []
for i in range(1,n):
    distances.append(arr[i]-arr[i-1])
distances.sort(reverse=True)

for i in range(k-1):
    distances[i] = 0
print(sum(distances))

