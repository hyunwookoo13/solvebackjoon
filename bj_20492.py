def saa(x):
    cal = (x//100)*22
    return cal

def saa2(x):
    cal = (x//100)*20
    return cal 

a = int(input())
b = saa2(a)

print(a-saa(a))
print(a-saa(b))