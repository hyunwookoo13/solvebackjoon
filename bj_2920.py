n=list(map(int,input().split(" ")))

ascending = True
descending = True

if ascending:
    for i in range(1,len(n)):
        if n[i-1] < n[i]:
            descending =False
        else:
            ascending =False
elif descending:
    for i in range(1, len(n)):
        if n[i-1] > n[i]:
            ascending =False
        else:
            descending = False

if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")
