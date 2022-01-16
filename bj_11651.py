n = int(input())
arr = []

for _ in range(n):
    a,b = map(int, input().split())
    arr.append([b,a])

s_arr = sorted(arr)

for b,a in s_arr:
    print(a,b)
    



