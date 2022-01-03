'''
단지 번호 붙이기

정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 없는 곳을 나타낸다. 연결된 집의 모임인 단지를 정의하고 단지에 번호를 붙이려 한다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하라
'''
from collections import deque

def main():
    N = int(input())
    apart = []
    for i in range(N):
        s = input()
        l = [int(j) * (-1) for j in s]
        apart.append(l)

    cur = 1
    l = []
    for i in range(N):
        for j in range(N):
            if apart[i][j] == -1:
                bfs(i, j, apart, cur, l)
                cur += 1

    print(len(l))
    l.sort()
    for i in l:
        print(i)

def bfs(x, y, apart, cur, l):
    count = 0
    #     상 하  좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    d = deque()
    d.append([x, y])
    while d:
        x, y = d.popleft()
        if apart[x][y] == -1:
            apart[x][y] = cur 
            count += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(apart) and 0 <= ny < len(apart):
                if apart[nx][ny] == -1:
                    d.append([nx, ny])
                    apart[nx][ny] = cur 
                    count += 1
    l.append(count)


main()