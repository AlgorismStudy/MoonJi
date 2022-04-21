'''로봇 청소기'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

    #  북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y = r, c
maps[r][c] = 2
count = 1

while True:
    for _ in range(4):
        d = (d - 1) % 4
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 0:
            maps[nx][ny] = 2
            x, y = nx, ny
            count += 1
            break
    else:
        nx = x + dx[(d + 2) % 4]
        ny = y + dy[(d + 2) % 4]
        if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] != 1:
            x, y = nx, ny
        else:
            break

print(count)