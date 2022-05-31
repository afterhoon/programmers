## 키패드 누르기
## https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    pad = [i+1 for i in range(9)] + ['*', 0, '#']
    answer = ''
    lp, rp = 9, 11
    for i in range(len(numbers)):
        if numbers[i] in [1, 4, 7]:
            answer += 'L'
            lp = pad.index(numbers[i])
        elif numbers[i] in [3, 6, 9]:
            answer += 'R'
            rp = pad.index(numbers[i])
        else:
            if distance(lp, pad.index(numbers[i])) < distance(rp, pad.index(numbers[i])):
                answer += 'L'
                lp = pad.index(numbers[i])
            elif distance(lp, pad.index(numbers[i])) > distance(rp, pad.index(numbers[i])):
                answer += 'R'
                rp = pad.index(numbers[i])
            else:
                if hand == 'left':
                    answer += 'L'
                    lp = pad.index(numbers[i])
                else:
                    answer += 'R'
                    rp = pad.index(numbers[i])

    return answer

def distance(finger, target):
    result = abs(finger//3 - target//3) + abs(finger%3 - target%3)
    return result

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

result = solution(numbers, hand)
print(result)