# a = ur = 지역 대회에서적어도 한문제는 푼 대학교의 수이다. 
# b = tr = 지역 대회에서 적어도 한문제는 푼 팀의 수이다. 
# c = uo = topc에서 적어도 한 문제는 푼 대학교의 수이다. 
# d = to = topc에서 적어도 한 문제는 푼 대학교의 수이다. 

# 전체 스코어 56a + 24b + 14c + 6d 

a,b,c,d = map(int, input().split(" "))

result = 56*a + 24*b + 14*c + 6*d
print(result)