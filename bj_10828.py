import sys
n = int(sys.stdin.readline())
stack = []

for i in range(n):
    arr = sys.stdin.readline().split()
    
    if arr[0]=='push':
        stack.append(arr[1])
    elif arr[0]=='top':
        if len(stack) == 0:
            print(-1)
        else:
            top_t = stack[-1]
            print(top_t)
    if arr[0]=='size':
        print(len(stack))
    if arr[0]=='empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if arr[0]=='pop':
        if len(stack) == 0:
            print(-1)
        else:
            top_p = stack.pop()
            print(top_p)
