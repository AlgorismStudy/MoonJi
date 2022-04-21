'''토마토'''
from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())

tomato = []
q = deque()

for i in range(H):
    tmp = []
    for j in range(N):
        tmp.append(list(map(int, input().split())))
        for k in range(M):
            if tmp[j][k] == 1:
                q.append([i, j, k])
    tomato.append(tmp)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while q:
    z, x, y = q.popleft()

    for d in range(6):
        nx = x + dx[d]
        ny = y + dy[d]
        nz = z + dz[d]

        if 0<=nx<N and 0<=ny<M and 0<=nz<H and tomato[nz][nx][ny] == 0:
            q.append([nz, nx, ny])
            tomato[nz][nx][ny] = tomato[z][x][y] + 1

result = 0
for box in tomato:
    for line in box:
        if 0 in line:
            print(-1)
            sys.exit()
        result = max(result, max(line))

print(result-1)


