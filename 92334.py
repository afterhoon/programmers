## 신고 결과 받기
## https://programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    answer = []
    reported = {}
    reporting = {}

    for i in range(len(id_list)):
        reporting[id_list[i]] = 0
        reported[id_list[i]] = []

    report = list(set(report))

    for i in range(len(report)):
        a, b = report[i].split()
        reported[b].append(a)

    for i in range(len(id_list)):
        if len(reported[id_list[i]]) >= k:
            for j in range(len(reported[id_list[i]])):
                reporting[reported[id_list[i]][j]] += 1

    for value in reporting.values():
        answer.append(value)
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
# result = [2,1,1,0]

# id_list = ["con", "ryan"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# k = 3
# result = [0,0]

result = solution(id_list, report, k)
print(result)