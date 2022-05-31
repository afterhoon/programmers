## 없는 숫자 더하기
## https://programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    return sum(list(filter(lambda x: x not in numbers, [1,2,3,4,5,6,7,8,9,0])))


numbers = [1,2,3,4,6,7,8,0]

result = solution(numbers)
print(result)