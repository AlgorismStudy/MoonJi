'''
유기농 배추

인접한 배추는 한 마리의 배추흰지렁이가 보호할 수 있다. 배추들이 몇 군데 퍼져있는지 조사하라
'''
from collections import deque

def main():
    T = int(input())
    for _ in range(T):
        M, N, K = map(int, input().split())
        print(earthworm(M, N, K))

def earthworm(M, N, K):
    count = 0
    cabbage = [[0]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        cabbage[y][x] = 1
    
    for i in range(M):
        for j in range(N):
            if cabbage[j][i] == 1:
                bfs(cabbage, i, j)
                count += 1

    return count

def bfs(cabbage, x, y):
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    d = deque()
    d.append([y, x])

    while d:
        y, x = d.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < len(cabbage) and 0 <= nx < len(cabbage[0]):
                if cabbage[ny][nx] == 1:
                    d.append([ny, nx])
                    cabbage[ny][nx] = -1


main()