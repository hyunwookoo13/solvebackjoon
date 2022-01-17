t=int(input())
for i in range(t):
    h,w,n=map(int,input().split())
    flo = 0
    room = 0
    if n%h==0:
        flo = 100*h
        room = n//h
    else:
        flo = (n%h)*100
        room= n//h+1
    print(flo+room)
