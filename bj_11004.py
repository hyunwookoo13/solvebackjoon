import sys
n,k = map(int, sys.stdin.readline().split(" "))

arr = list(map(int,sys.stdin.readline().split(" ")))

s_arr = sorted(arr)
print(s_arr[k-1])

