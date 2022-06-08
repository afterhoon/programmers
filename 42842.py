## 카펫
## https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    tmp = brown//2-2

    for i in range(1, tmp):
        if i * (tmp-i) == yellow:
            return [tmp-i+2, i+2]

brown = 10
yellow = 2

result = solution(brown, yellow)
print(result)