'''녹색 옷 입은 애가 젤다지?'''

from collections import deque
import sys
input = sys.stdin.readline

index = 1

while True:
    N = int(input().rstrip())
    if N == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(N)]
    result = [[987654321] * N for _ in range(N)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dq = deque()
    dq.append([0, 0])
    result[0][0] = graph[0][0]

    while dq:
        x, y = dq.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N:
                if result[nx][ny] > result[x][y] + graph[nx][ny]:
                    result[nx][ny] = result[x][y] + graph[nx][ny]
                    dq.append([nx, ny])
                    
    print("Problem " + str(index) + ":", result[N-1][N-1])
    index += 1