'''구슬 탈출2'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = [input().strip() for _ in range(N)]
def down(board):
    for i in range(N):
        index = board[i].find('R')
        if index != -1:
            for j in range(i+1, N-1):
                if board[j][index] == "#":
                    break
                if board[j][index] == ".":
                    board[j-1] = board[j-1][:index] + "." + board[j-1][index+1:]
                    board[j] = board[j][:index] + "R" + board[j][index+1:]

print(board)
down(board)
print(board)