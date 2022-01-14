date = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
month_31 = [1,3,5,7,8,10,12]
month_30 = [4,6,9,11]

x,y = map(int, input().split())
sum = 0 
for i in range(x-1):
    k = i+1
    if k in month_31:
        sum += 31
    elif k in month_30:
        sum += 30
    else:
        sum +=28

cal = (sum+y-1) % 7
print(date[cal])




