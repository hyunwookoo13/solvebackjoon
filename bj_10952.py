sum=0
try:
    while 1:
        a,b=map(int,input().split())
        sum = a+b
        if sum ==0:
            break
        else:
            print(sum)
except:
    exit()
