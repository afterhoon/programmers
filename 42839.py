## 소수 찾기
## https://programmers.co.kr/learn/courses/30/lessons/42839

from math import sqrt
from itertools import permutations

def solution(numbers):
    answer = 0

    lst = []
    for i in range(len(numbers)):
        lst += permutations(numbers, i+1)
    
    for i in range(len(lst)):
        lst[i] = "".join(lst[i])

    lst = list(set(map(int, lst)))
    for num in lst:
        answer += (1 if isPrime(num) else 0)

    return answer

def isPrime(x):
    if x < 2:
        return False

    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

numbers = "011"

result = solution(numbers)
print(result)