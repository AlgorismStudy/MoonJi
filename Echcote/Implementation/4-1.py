'''
상하좌우

N x N 크기의 정사각형 공간 위에서 서있다. (1, 1)에서 출발하여 도착할 지점의 좌표를 출력하라.
'''

N = int(input())
moves = input().split()

#      상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

x, y = 1, 1

for move in moves:
    if move == 'U':
        nx = x + dx[0]
        ny = y + dy[0]
    if move == 'D':
        nx = x + dx[1]
        ny = y + dy[1]
    if move == 'L':
        nx = x + dx[2]
        ny = y + dy[2]
    if move == 'R':
        nx = x + dx[3]
        ny = y + dy[3]

    if nx <= N and nx > 0 and ny <= N and ny > 0:
        x, y = nx, ny

print(x, y)