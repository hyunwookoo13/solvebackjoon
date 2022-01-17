n = int(input())
for i in range(n):
    data = input()
    stack = []

    for j in data:
        if j=='(':
            stack.append(j)
        elif j==')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
