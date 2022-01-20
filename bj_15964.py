def new(a,b):
    n = (a+b)*(a-b)
    return n

x,y = map(int, input().split(" "))
print(new(x,y))