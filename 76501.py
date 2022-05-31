## 음양 더하기
## https://programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    return sum(list(map(lambda x, y: x * (1 if y else -1), absolutes, signs)))

absolutes = [4,7,12]
signs = [True,False,True]

result = solution(absolutes, signs)
print(result)