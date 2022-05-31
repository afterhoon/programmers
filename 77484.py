## 로또의 최고 순위와 최저 순위
## https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    answer = []
    cnt = 0

    for i in range(6):
        if lottos[i] in win_nums:
            cnt += 1

    answer = [7-(cnt+lottos.count(0)) if cnt+lottos.count(0) > 1 else 6,7-cnt if cnt > 1 else 6]

    return answer

# lottos = [44, 1, 0, 0, 31, 25]
# win_nums = [31, 10, 45, 1, 6, 19]

lottos = [0, 0, 0, 0, 0, 0]
win_nums = [38, 19, 20, 40, 15, 25]
result = solution(lottos, win_nums)

print(result)