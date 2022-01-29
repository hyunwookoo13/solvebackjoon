arr = list(map(int, input().split(" ")))

if len(set(arr)) == 1:
    print(10000+arr[0]*1000)
elif len(set(arr)) == 3:
    print(max(arr)*100)
else:
    count = [0] * (7)
    for i in arr:
        count[i] += 1
    k = count.index(max(count))
    print(1000+k*100)


