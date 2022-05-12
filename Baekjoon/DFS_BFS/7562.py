'''나이트의 이동'''

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

for _ in range(T):
    L = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    visited = [[0] * L for _ in range(L)]
    dq = deque()
    dq.append(start)
    visited[start[0]][start[1]] = 1

    while dq:
        x, y = dq.popleft()
        if [x, y] == end:
            break

        for d in range(8):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < L and 0 <= ny < L and visited[nx][ny] == 0:
                dq.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

    print(visited[end[0]][end[1]] - 1)