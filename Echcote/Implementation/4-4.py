'''
게임 개발

맵은 1 x 1 크기의 정사각형으로 이뤄진 N x M 크기의 직사각형으로 각각의 칸은 육지 또는 바다이다. 캐릭터는 동서남북 중 한 곳을 바라본다. 캐릭터는 상하좌우로 움직일 수 있고, 바다는 갈 수 없다. 

캐릭터가 방문한 칸의 수를 출력하는 프로그램을 만드시오.
'''

N, M = map(int, input().split())
x, y, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]

#    북0 동1 남2 서3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 1
visited = [[0] * M for _ in range(N)]
turn_time = 0

while True:
    d -= 1
    if d == -1:
        d = 3
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < M and 0 <= ny < N:
        if visited[nx][ny] == 0 and map[nx][ny] == 0:
            count += 1
            visited[nx][ny] = 1
            x, y = nx, ny
        else:
            turn_time += 1

    if turn_time == 4:
        turn_time = 0
        nx = x - dx[d]
        ny = y - dy[d]

        if map[nx][ny] == 1:
            break
        x, y = nx, ny

print(count)    
