from collections import deque

N, M, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def solution(N, M, K, graph):
    dice = [2, 4, 1, 3, 5, 6]
    dir = 1

    x, y = 0, 0
    score = 0

    for _ in range(K):
        x, y, dir = move_dice(x, y, dir)
        dice = rotate_dice(dice, dir)

        c = bfs(x, y)
        score += graph[x][y] * c

        A, B = dice[5], graph[x][y]
        if A > B:
            dir = (dir+1) % 4
        elif A < B:
            dir = (dir-1) % 4

    return score

def check(x, y):
    if 0 <= x < N and 0 <= y < M:
        return False
    return True

def move_dice(x, y, dir):
    nx = x + dx[dir]
    ny = y + dy[dir]

    if check(nx, ny):
        new_dir = (dir + 2) % 4
        nx = x + dx[new_dir]
        ny = y + dy[new_dir]
        return [nx, ny, new_dir]

    return [nx, ny, dir]

def rotate_dice(dice, dir):
    if dir == 0:
        # dice = [1, 4, 5, 3, 6, 2]
        dice[0], dice[2], dice[4], dice[5] = dice[2], dice[4], dice[5], dice[0]   
    elif dir == 1:
        # dice = [2, 6, 4, 1, 5, 3]
        dice[1], dice[2], dice[3], dice[5] = dice[5], dice[1], dice[2], dice[3]
    elif dir == 2:
        # dice = [6, 4, 2, 3, 1, 5]
        dice[0], dice[2], dice[4], dice[5] = dice[5], dice[0], dice[2], dice[4]
    elif dir == 3:
        # dice = [2, 1, 3, 6, 5, 4]
        dice[1], dice[2], dice[3], dice[5] = dice[2], dice[3], dice[5], dice[1]
    return dice


def bfs(x, y):
    cnt = 1
    visited = [[0]*M for _ in range(N)]
    q = deque()
    q.append([x, y])
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if check(nx, ny):
                continue
            if graph[x][y] == graph[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append([nx, ny])
                cnt += 1
    return cnt

print(solution(N, M, K, graph))
