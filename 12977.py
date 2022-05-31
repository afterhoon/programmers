## 소수 만들기
## https://programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations

def solution(nums):
    n = 50000
    a = [False,False] + [True] * (n-1)
    primes = []

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False

    return len(list(filter(lambda x: x in primes, list(map(lambda x: sum(x), list(combinations(nums, 3)))))))

nums = [1,2,7,6,4]

result = solution(nums)
print(result)