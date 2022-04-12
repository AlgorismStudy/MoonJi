'''벽 부수고 이동하기'''

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0,0] for _ in range(M)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = -1

q = deque()
q.append((0, 0, 0))
visited[0][0][0] = 1

while q:
    x, y, w = q.popleft()
    if x == N-1 and y == M-1:
        result = visited[x][y][w]
        break
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < M:
            if maps[nx][ny] == 0 and visited[nx][ny][w] == 0:
                q.append((nx, ny, w))
                visited[nx][ny][w] = visited[x][y][w] + 1
            if maps[nx][ny] == 1 and w == 0:
                q.append((nx, ny, w + 1))
                visited[nx][ny][w + 1] = visited[x][y][w] + 1

print(result)