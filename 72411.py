## 메뉴 리뉴얼
## https://programmers.co.kr/learn/courses/30/lessons/72411

def solution(orders, course):
    answer = []
    co = [[] for i in range(11)]

    for i in range(len(orders)):
        for j in range(i+1,len(orders)):
            temp = []
            cnt = 0
            for k in orders[i]:
                if k in orders[j]:
                    temp.append(k)
                    cnt += 1
            co[cnt].append(temp)

    for i in range(len(co)):
        print(co[i])

    return answer

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]

result = solution(orders, course)
print(result)