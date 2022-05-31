## 신규 아이디 추천
## https://programmers.co.kr/learn/courses/30/lessons/72410

import re

def solution(new_id):
    answer = ''

    answer = new_id.lower()
    answer = re.sub("([^a-z0-9-_.])", "", answer)
    answer = re.sub("[.]+", ".", answer)
    answer = answer.strip('.')
    answer = 'a' if answer == '' else answer
    answer = answer[:15].rstrip('.')
    answer = answer.ljust(3, answer[-1])

    return answer

new_id = "...!@BaT#*..y.abcdefghi1234jklm"
result = solution(new_id)
print(result)