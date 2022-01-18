test_case = int(input())

for _ in range(test_case):
    left_stack = []
    right_stack = []
    data = input()
    for i in data:
        if i == '-':
            if left_stack:
                left_stack.pop()
        elif i == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif i == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(i)
    left_stack.extend(reversed(right_stack)) #오른쪽 스택을 reversed 한 상태로 extend해야 제대로 출력이 됩니다.
    print("".join(left_stack)) 