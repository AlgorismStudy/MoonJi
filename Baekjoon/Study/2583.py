'''영역 구하기'''
from collections import deque

m, n, k = map(int, input().split())

graph = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[j][i] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    count = 1
    dq = deque()
    dq.append([i, j])
    graph[i][j] = 1

    while dq:
        x, y = dq.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
                dq.append([nx, ny])
                graph[nx][ny] = 1
                count += 1
    return count

area = 0
total_count = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            total_count.append(bfs(i, j))
            area += 1
            
total_count.sort()
print(area)
print(*total_count, sep=" ")
