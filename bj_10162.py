n = int(input())

a = 300
b = 60
c = 10
a_count = 0
b_count = 0
c_count = 0

if n % c != 0:
    print(-1)
else:
    k = n%a
    p = k%b

    a_count += n//a
    b_count += k//b
    c_count += p//c
    print(a_count, b_count, c_count,sep=" ")
        


