## 타겟 넘버
## https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    global answer
    answer = 0

    myFunc(numbers, target, 0, 0)

    return answer

def myFunc(numbers, target, i, n):
    global answer
    if i == len(numbers):
        if target == n:
            answer += 1
        return
    
    myFunc(numbers, target, i+1, n+numbers[i])
    myFunc(numbers, target, i+1, n-numbers[i])


numbers = [4, 1, 2, 1]
target = 4

result = solution(numbers, target)
print(result)