n = int(input())


for i in range(n):
    a = int(input())
    d = [0,1,2,4]

    if a == 1:
        print(d[1])
    elif a == 2:
        print(d[2])
    elif a == 3:
        print(d[3])
    else:
        for i in range(4,a+1):
            d.append(d[i-3]+d[i-2]+d[i-1])
        print(d[a])

   


        
    
      