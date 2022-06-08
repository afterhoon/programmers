## 실패율
## https://programmers.co.kr/learn/courses/30/lessons/42889

import operator

def solution(N, stages):
    dict = {}
    for i in range(N):
        dict[i+1] = 0.0

    tot = len(stages)

    for i in range(N):
        cnt = 0
        for j in range(len(stages)):
            if stages[j] == i+1:
                cnt += 1
        dict[i+1] = cnt/tot
        print(cnt, '/', tot)
        tot -= cnt
        if tot == 0:
            break

    dict = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
    print(dict)
    answer = list(dict.keys())

    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

result = solution(N, stages)
print(result)