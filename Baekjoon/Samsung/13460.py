'''구슬 탈출2'''
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
red = []
blue = []
hole = []
for i in range(N):
    s = input().strip()
    board.append(s)
    for j in range(M):
        if s[j] == 'R':
            red = [i, j]
        if s[j] == 'B':
            blue = [i, j]
        if s[j] == 'O':
            hole = [i, j]

#      상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 움직일 수 있는 칸 수 계산
def move(x, y, d):
    count = 0
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        count += 1
        if board[nx][ny] == 'O': 
            break
        if board[nx][ny] == '#': 
            count -= 1
            break
        x = nx
        y = ny
    return count

dq = deque([red])
b_dq = deque([blue])
visited = [[0] * M for _ in range(N)]
visited[red[0]][red[1]] = 1
flag = True

while dq:
    x, y = dq.popleft()
    bx, by = b_dq.popleft()
    if board[bx][by] == 'O':
        flag = False
        break
    if board[x][y] == 'O':
        break
    for d in range(4):
        # red
        move_count = move(x, y, d)
        nx = x + dx[d] * move_count
        ny = y + dy[d] * move_count
        # blue
        move_count = move(bx, by, d)
        nbx = bx + dx[d] * move_count
        nby = by + dy[d] * move_count

        if nx == nbx and ny == nby:
            if x == bx and d == 2: 
                if y < by:  nby += 1
                else: ny += 1
            if y == by:
                if x > bx:  nbx += 1
                else: nx += 1

        if 0 < nx < N-1 and 0 < ny < M-1 and visited[nx][ny] == 0:
            dq.append([nx, ny])
            b_dq.append([nbx, nby])
            # print(nbx, nby)
            visited[nx][ny] = visited[x][y] + 1

# print(*visited, sep='\n')
if flag:
    print(visited[hole[0]][hole[1]] - 1)
else:
    print(-1)