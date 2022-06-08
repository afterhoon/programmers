## 모의고사
## https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    index = [0, 0, 0]
    score = [0, 0, 0]
    pattern = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    length = [5, 8, 10]

    for i in range(len(answers)):
        for j in range(3):
            if pattern[j][index[j]] == answers[i]:
                score[j] += 1
            index[j] = (index[j] + 1) % length[j]

    _max = 0
    for i in range(3):
        if _max < score[i]:
            _max = score[i]
            answer.clear()
            answer.append(i+1)
        elif _max == score[i]:
            answer.append(i+1)
    return answer

answer = [1,3,2,4,2]

result = solution(answer)
print(result)