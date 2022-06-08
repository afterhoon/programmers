## 위장
## https://programmers.co.kr/learn/courses/30/lessons/42578

from typing import Counter

def solution(clothes):
    answer = 1
    for i in dict(Counter(list(map(lambda x: x[1], clothes)))).values():
        answer *= i+1
    return answer-1

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

result = solution(clothes)
print(result)