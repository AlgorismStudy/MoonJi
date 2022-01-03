'''
미로 탐색

N x M크기의 배열로 표현되는 미로가 있다. 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. (1, 1)에서 출발하여 (N, M) 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하라
'''
from collections import deque

N, M = map(int, input().split())
maze = []
for i in range(N):
    s = input()
    l = [int(j) for j in s]
    maze.append(l)

x, y = [0, 0]
#     상 하  좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

d = deque()
d.append([x, y])
while d:
    x, y = d.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if maze[nx][ny] == 1:
                d.append([nx, ny])
                maze[nx][ny] = maze[x][y] + 1
    
print(maze[N-1][M-1])

