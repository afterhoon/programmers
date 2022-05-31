## 숫자 문자열과 영단어
## https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    answer = 0
    eng = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 
            '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    temp = ''

    for i in range(len(s)):
        temp += s[i]

        try:
            answer = answer*10 + eng[temp]
            temp = ''
        except:
            0

    return answer

s = "one4seveneight"
result = solution(s)

print(result)