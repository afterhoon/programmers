## 내적
## https://programmers.co.kr/learn/courses/30/lessons/70128

def solution(a, b):
    return sum(list(map(lambda x, y: x * y, a, b)))

a = [1,2,3,4]
b = [-3,-1,0,2]

result = solution(a, b)
print(result)