'''2048'''
from copy import deepcopy

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
result = 0

def up(board):
    for j in range(N):
        p = 0
        for i in range(1, N):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0

                if board[p][j] == 0:
                    board[p][j] = tmp
                elif board[p][j] == tmp:
                    board[p][j] *= 2
                    p += 1
                else:
                    p += 1
                    board[p][j] = tmp
    return board

def down(board):
    for j in range(N):
        p = N - 1
        for i in range(N - 2, -1, -1):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0

                if board[p][j] == 0:
                    board[p][j] = tmp
                elif board[p][j] == tmp:
                    board[p][j] *= 2
                    p -= 1
                else:
                    p -= 1
                    board[p][j] = tmp
    return board

def left(board):
    for i in range(N):
        p = 0
        for j in range(1, N):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0

                if board[i][p] == 0:
                    board[i][p] = tmp
                elif board[i][p] == tmp:
                    board[i][p] *= 2
                    p += 1
                else:
                    p += 1
                    board[i][p] = tmp
    return board

def right(board):
    for i in range(N):
        p = N - 1
        for j in range(N - 2, -1, -1):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0

                if board[i][p] == 0:
                    board[i][p] = tmp
                elif board[i][p] == tmp:
                    board[i][p] *= 2
                    p -= 1
                else:
                    p -= 1
                    board[i][p] = tmp
    return board

def dfs(depth, board):
    if depth == 5:
        return max(map(max, board))
    
    result = max(
        dfs(depth + 1, up(deepcopy(board))), 
        dfs(depth + 1, down(deepcopy(board))),
        dfs(depth + 1, left(deepcopy(board))),
        dfs(depth + 1, right(deepcopy(board)))
        )
    return result
    

result = dfs(0, board)
print(result)