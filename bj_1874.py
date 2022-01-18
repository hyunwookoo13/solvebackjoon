n = int(input())

count = 0
stack= []
result=[]

for i in range(1,n+1): # 데이터의 개수만큼 반복
    data = int(input())
    while count <= data: # 입력 받은 데이터에 도달할 때까지 삽입
        stack.append(count)
        count +=1
        result.append('+')
    if stack[-1] == data: # 스택의 최상위 원소가 데이터와 같을 때 출력 
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)
print('\n'.join(result))
