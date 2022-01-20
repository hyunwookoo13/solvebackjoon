sum = 0
for i in range(4):
    a = int(input())
    sum += a

minute = sum//60
sec = sum%60

print(minute)
print(sec)
