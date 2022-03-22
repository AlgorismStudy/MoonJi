'''테트로미노'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0

def dfs(x, y, depth, total):
    global result
    if depth == 3:
        result = max(result, total)
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False:
                if depth == 1:
                    visited[nx][ny] = True
                    dfs(x, y, depth + 1, total + maps[nx][ny])
                    visited[nx][ny] = False 
                visited[nx][ny] = True
                dfs(nx, ny, depth + 1, total + maps[nx][ny])
                visited[nx][ny] = False    


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 0, maps[i][j])
        visited[i][j] = False

print(result)