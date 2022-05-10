'''사다리 조작'''

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = []
max_h, min_h = 1, 100

for _ in range(N):
    s = list(map(int, input().split()))
    max_h = max(max_h, max(s))
    min_h = min(min_h, min(s))
    graph.append(s)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(h, i, j):
    q = deque()
    q.append([i, j])
    visited[i][j] = 1

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and graph[nx][ny] > h:
                q.append([nx, ny])
                visited[nx][ny] = 1

result = 0

for h in range(min_h, max_h):
    visited = [[0] * N for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            if graph[i][j] > h and visited[i][j] == 0:
                bfs(h, i, j)
                count += 1

    result = max(result, count)

print(result)