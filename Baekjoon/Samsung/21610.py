'''마법사 상어와 비바라기'''

import sys 
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
d, s = [], []
for _ in range(M):
    input_d, input_b = map(int, input().split())
    d.append(input_d)
    s.append(input_b)

# 인덱스를 맞추기 위해 0번째는 더미 값
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

cloud = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
visited = [[0] * N for _ in range(N)]

def move_cloud(d, s):
    for i in range(len(cloud)):
        cloud[i][0] = (cloud[i][0] + dx[d] * s) % N
        cloud[i][1] = (cloud[i][1] + dy[d] * s) % N
        
def rain_cloud():
    global cloud
    for x, y in cloud:
        A[x][y] += 1
        visited[x][y] = 1
    cloud = []

def water_copy_bug():
    dx = [-1, -1, 1, 1]
    dy = [-1, 1, 1, -1]
    for x in range(N):
        for y in range(N):
            if visited[x][y] != 0:
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < N and 0 <= ny < N and A[nx][ny] != 0:
                        A[x][y] += 1

def make_cloud():
    global visited
    for i in range(N):
        for j in range(N):
            if visited[i][j] != 0:
                visited[i][j] = 0
            elif A[i][j] >= 2:
                cloud.append([i, j])
                A[i][j] -= 2


for i in range(M):
    move_cloud(d[i], s[i])
    rain_cloud()
    water_copy_bug()
    make_cloud()

result = sum([sum(a) for a in A])
print(result)
