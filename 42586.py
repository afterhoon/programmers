## 기능개발
## https://programmers.co.kr/learn/courses/30/lessons/42586

from math import ceil

def solution(progresses, speeds):
    answer = []
    length = len(progresses)
    cnt = 0

    for i in range(length):
        progresses[i] = ceil((100 - progresses[i])/speeds[i])

    progresses.append(200)
    temp = progresses[0]
    for i in range(length):
        cnt += 1
        if temp < progresses[i+1]:
            temp = progresses[i+1]
            answer.append(cnt)
            cnt = 0

    return answer

progresses = [96, 99, 98, 97]
speeds = [1, 1, 1, 1]

result = solution(progresses, speeds)
print(result)