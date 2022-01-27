# 신년을 맞이해서 쥐를 잡으려고 한다. 
# 더글라스는 쥐를 n1마리 잡아서 그들의 귀에 태그를 붙히고 방출했다. 
# 두번째 날에는 n2마리 잡아서 관찰했다. n12를 마크된 첫날 동안 뭘했는지 알아 보았다. 

def cal(n1,n2,n12):
    k = (n1+1)*(n2+1)//(n12+1)-1
    return k

n1, n2, n12 = map(int, input().split(" "))
result = cal(n1,n2,n12)
print(result)
