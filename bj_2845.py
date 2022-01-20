l, p = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))

hm = l*p

n_arr = []
for i in range(len(arr)):
    a = arr[i]-hm
    n_arr.append(a)

for i in range(len(n_arr)):
    print(n_arr[i], end =' ' )
