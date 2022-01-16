n = int(input())
arr = []
for _ in range(n):
    k = input().split(" ")
    arr.append([k[0],int(k[1]),int(k[2]),int(k[3])])
s_arr = sorted(arr, key= lambda x: (-x[1], x[2], -x[3], x[0]))

for i in s_arr:
    print(i[0])
    