## 크레인 인형뽑기 게임
## https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    basket = [-1]
    length = len(board)
    new_board = [[] for i in range(length)]
    for i in range(length):
        for j in range(length):
            if board[length-j-1][i] != 0:
                new_board[i].append(board[length-j-1][i])

    for i in range(len(moves)):
        try:
            temp = new_board[moves[i]-1].pop()
            if basket[-1] == temp:
                basket.pop()
                answer += 2
            else:
                basket.append(temp)
        except:
            0

    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

result = solution(board, moves)
print(result)


'''
1	네오
2	무지
3	튜브
4	어피치
5	프로도
'''