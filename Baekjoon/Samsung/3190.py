'''뱀'''

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())    # 보드의 크기
K = int(input())    # 사과의 개수
apple = [list(map(int, input().split())) for _ in range(K)]

L = int(input())    # 뱀의 방향 변환 횟수
dir = []
for _ in range(L):
    X, C = input().split()
    dir.append((int(X), C))

# 상0 우1 하2 좌3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

snake = deque()
snake.append([1, 1])
head = [1, 1]
time = 0
d = 1

def check_head(move_head):
    for _ in range(len(snake)):
        tail = snake.popleft()
        if move_head == tail:
            return False
        snake.append(tail)
    return True

while True:
    time += 1
    move_head = [head[0] + dx[d], head[1] + dy[d]]

    # 꼬리랑 만나는지 체크
    if not check_head(move_head):
        break

    # 사과 있는지 확인
    if move_head in apple:
        snake.appendleft(move_head)
        apple.remove(move_head)
    else:  
        tail = snake.pop()
        snake.appendleft(move_head)  

    # 맵 밖으로 나가는지 확인
    if move_head[0] < 1 or move_head[0] > N or move_head[1] < 1 or move_head[1] > N:
        break

    # 방향 전환
    if len(dir) > 0 and time == dir[0][0]:
        if dir[0][1] == 'L':
            d = (d - 1) % 4
        elif dir[0][1] == 'D':
            d = (d + 1) % 4
        del dir[0]
    head = move_head
    
print(time)
