'''
토마토

하루가 지나면, 익은 토마토들의 인접한 토마토들은 익은 토마토의 영향을 받아 익게 된다. 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 토마토들이 며칠이 지나면 다 익게 되는지 최소 일수를 구하라.
'''
from collections import deque

M, N = map(int, input().split())

tomato = []
d = deque()

for i in range(N):
    t = list(map(int, input().split()))
    [d.append([i, j]) for j in range(M) if t[j] == 1]
    tomato.append(t)

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

while d:
    x, y = d.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                d.append([nx, ny])

if all(0 not in t for t in tomato):
    print(max(map(max, tomato)) - 1)
else:
    print(-1)