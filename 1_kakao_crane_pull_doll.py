# board 배열은 2차원 배열로 크기는 "5 x 5" 이상 "30 x 30" 이하입니다.
# board의 각 칸에는 0 이상 100 이하인 정수가 담겨있습니다
# [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	[1,5,3,5,1,2,1,4]	4

import random

arr_size = 19

def solution(board, moves):
    stacks = []
    answer = 0
    for pull in moves:
        take = board[pull-1].pop()
        if take == 0: continue
        # print("대상:", board[pull-1], take)
        if not stacks:
            stacks.append(take)
        else:
            if stacks[-1] == take:
                stacks.pop()
                answer += 1
            else:
                stacks.append(take)
        # print(stacks, answer)
    return answer*2

board = []
# a = [ random.randint(0, 100) for x in range(0, 30)]

def random_arr(random_max, range_max):
    return [random.randint(0, random_max) for x in range(0, range_max)]

for x in range(0, arr_size):
    board.append(random_arr(100, arr_size))

moves= random_arr(arr_size, arr_size)
# print(board)
# print(moves)
result = solution(board=board, moves=moves)

print(result)



    
    
