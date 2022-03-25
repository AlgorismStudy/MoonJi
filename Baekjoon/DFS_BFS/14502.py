'''연구소'''

from collections import deque
import copy
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

result = 0

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    global result
    copy_maps = copy.deepcopy(maps)
    dq = deque()

    for i in range(N):
        for j in range(M):
            if copy_maps[i][j] == 2:
                dq.append([i, j])


    while dq:
        x, y = dq.popleft()

        for n in range(4):
            nx = x + dx[n]
            ny = y + dy[n]

            if 0 <= nx < N and 0 <= ny < M and copy_maps[nx][ny] == 0:
                copy_maps[nx][ny] = 2
                dq.append([nx, ny])
    
    zero_cnt = 0
    for i in range(N):
        zero_cnt += copy_maps[i].count(0)

    result = max(result, zero_cnt)

def makeWall(cnt):
    if cnt == 3:
        bfs()
        return
    
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                maps[i][j] = 1
                makeWall(cnt + 1)
                maps[i][j] = 0


makeWall(0)
print(result)

