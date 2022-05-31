## 오픈채팅방
## https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    command = []
    member = {}
    
    for i in range(len(record)):
        temp = list(record[i].split())
        command.append([temp[0], temp[1]])
        if temp[0] != 'Leave':
            member[temp[1]] = temp[2]
    
    for i in range(len(record)):
        s = ''
        if command[i][0] == 'Enter':
            answer.append(member[command[i][1]] + '님이 들어왔습니다.')
        elif command[i][0] == 'Leave':
            answer.append(member[command[i][1]] + '님이 나갔습니다.')

    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

# result = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
result = solution(record)
print(result)