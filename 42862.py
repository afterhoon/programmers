## 체육복
## https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    answer = 0
    std = [1 for i in range(n)]
    for i in lost:
        std[i-1] -= 1
    for i in reserve:
        std[i-1] += 1

    print(std)
    borrow(std, 0, n)

    return answer

def borrow(std, i, n):
    global answer
    temp = std
    if i == n:
        return answer
    if std[i] == 2:
        if std[i-1] == 0:
            temp[i], temp[i-1] = 1, 1
            answer += 1
            return borrow(temp, i+1, n)
        if std[i+1] == 0:
            temp[i], temp[i+1] = 1, 1
            answer += 1
            return borrow(temp, i+1, n)

answer = 0
n = 5
lost = [2, 4]
reverve = [1, 3, 5]

result = solution(n, lost, reverve)
print(result)