#구구단-2단 
n = int(input())

for i in range(9):
    print("{} * {} = {}".format(n, i+1, n*(i+1)))