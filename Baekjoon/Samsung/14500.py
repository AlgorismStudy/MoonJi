'''테트로미노'''

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max_value = 0

def tetromino1(i, j):
    global max_value
    if j+3 < M:
        total = maps[i][j] + maps[i][j+1] + maps[i][j+2] + maps[i][j+3]
        max_value = max(max_value, total)
    if i+3 < N:
        total = maps[i][j] + maps[i+1][j] + maps[i+2][j] + maps[i+3][j]
        max_value = max(max_value, total)

def tetromino2(i, j):
    global max_value
    if i+1 < N and j+1 < M:
        total = maps[i][j] + maps[i][j+1] + maps[i+1][j] + maps[i+1][j+1]
        max_value = max(max_value, total)

def tetromino3(i, j):
    global max_value
    if i+2 < N and j+1 < M:
        total1 = maps[i][j] + maps[i+1][j] + maps[i+2][j] + maps[i+2][j+1]
        total2 = maps[i][j] + maps[i+1][j] + maps[i+2][j] + maps[i][j+1]
        max_value = max(max_value, total1, total2)
    if i+2 < N and j-1 >= 0:
        total1 = maps[i][j] + maps[i+1][j] + maps[i+2][j] + maps[i+2][j-1]
        total2 = maps[i][j] + maps[i+1][j] + maps[i+2][j] + maps[i][j-1]
        max_value = max(max_value, total1, total2)
    if i+1 < N and j+2 < M:
        total1 = maps[i][j] + maps[i][j+1] + maps[i][j+2] + maps[i+1][j+2]
        total2 = maps[i][j] + maps[i][j+1] + maps[i][j+2] + maps[i+1][j]
        max_value = max(max_value, total1, total2)
    if i-1 >= 0 and j+2 < M:
        total1 = maps[i][j] + maps[i][j+1] + maps[i][j+2] + maps[i-1][j+2]
        total2 = maps[i][j] + maps[i][j+1] + maps[i][j+2] + maps[i-1][j]
        max_value = max(max_value, total1, total2)

def tetromino4(i, j):
    global max_value
    if i+2 < N and j+1 < M:
        total = maps[i][j] + maps[i+1][j] + maps[i+1][j+1] + maps[i+2][j+1]
        max_value = max(max_value, total)
    if i+2 < N and j-1 >= 0:
        total = maps[i][j] + maps[i+1][j] + maps[i+1][j-1] + maps[i+2][j-1]
        max_value = max(max_value, total)
    if i+1 < N and j+2 < M:
        total = maps[i][j] + maps[i][j+1] + maps[i+1][j+1] + maps[i+1][j+2]
        max_value = max(max_value, total)
    if i-1 >= 0 and j+2 < M:
        total = maps[i][j] + maps[i][j+1] + maps[i-1][j+1] + maps[i-1][j+2]
        max_value = max(max_value, total)

def tetromino5(i, j):
    global max_value
    if i+1 < N and j+2 < M:
        total = maps[i][j] + maps[i][j+1] + maps[i][j+2] + maps[i+1][j+1]
        max_value = max(max_value, total)
    if i-1 >= 0 and j+2 < M:
        total = maps[i][j] + maps[i][j+1] + maps[i][j+2] + maps[i-1][j+1]
        max_value = max(max_value, total)
    if i+2 < N and j+1 < M:
        total = maps[i][j] + maps[i+1][j] + maps[i+1][j+1] + maps[i+2][j]
        max_value = max(max_value, total)
    if i+2 < N and j-1 >= 0:
        total = maps[i][j] + maps[i+1][j] + maps[i+1][j-1] + maps[i+2][j]
        max_value = max(max_value, total)


for i in range(N):
    for j in range(M):
        tetromino1(i, j)
        tetromino2(i, j)
        tetromino3(i, j)
        tetromino4(i, j)
        tetromino5(i, j)

print(max_value)