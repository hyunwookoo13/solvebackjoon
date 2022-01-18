# union-find 알고리즘 사용(재귀용법 적용)
# dictionary로 해시 표현해서 사용 
import sys

def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(a,b):
    x = find(a)
    y = find(b)

    if x != y:
        parent[y] = x
        number[x] += number[y]
        
test_case = int(sys.stdin.readline())
for _ in range(test_case):
    parent = dict()
    number = dict()

    f = int(sys.stdin.readline())

    for _ in range(f):
        x, y = sys.stdin.readline().split(' ')

        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1

        union(x,y)
        print(number[find(x)])