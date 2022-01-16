n = int(input())

array=  []

for i in range(n):
    data = int(input())
    array.append(data)

array = sorted(array)

for data in array:
    print(data)