## 베스트앨범
## https://programmers.co.kr/learn/courses/30/lessons/42579

from ast import operator


def solution(genres, plays):
    answer = []
    total = {}

    for g, p in zip(genres, plays):
        if g not in total:
            total[g] = p
        else:
            total[g] += p

    music = []
    for i in range(len(genres)):
        music.append([i, plays[i], total[genres[i]], genres[i], 0])
    
    music = sorted(music, key = lambda x: (x[3], -x[1], x))
    cnt = 0
    music = [music[0]] + music
    for i in range(1, len(music)):
        if music[i-1][3] != music[i][3]:
            cnt = 0
        cnt += 1
        if cnt > 2:
            continue
        music[i][4] = cnt
        answer.append(music[i])

    answer = list(map(lambda x: x[0], sorted(answer, key = lambda x: (-x[2], -x[1], x[0]))))

    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

result = solution(genres, plays)
print(result) # [4, 1, 3, 0]