## 문자열 압축
## https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    if len(s) == 1:
        return 1
    
    answer = 10000
    lst = []
    unit = [10, 100, 1000]

    for i in range(1, len(s)//2+1):
        temp = s
        cnt = 1
        result = 0
        while temp:
            lst.append(temp[:i])
            temp = temp[i:]

        result += i
        for j in range(1, len(lst)):
            if lst[j-1] == lst[j]:
                if cnt == 1:
                    result += 1

                cnt += 1
                if cnt in unit:
                    result += 1
            else:
                result += len(lst[j])
                cnt = 1

        lst = []
        answer = min(answer, result)

    return answer

s = "xxxxxxxxxxyyy"

result = solution(s)
print(result)