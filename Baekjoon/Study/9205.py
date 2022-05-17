'''맥주 마시면서 걸어가기'''

from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    start = list(map(int, input().split()))
    stores = [list(map(int, input().split())) for _ in range(n)]
    end = list(map(int, input().split()))

    visited = [0] * n
    dq = deque()
    dq.append(start)
    while dq:
        x, y = dq.popleft()

        if abs(end[0] - x) + abs(end[1] - y) <= 1000:
            print("happy")
            break

        for i in range(n):
            if not visited[i] and abs(stores[i][0]-x) + abs(stores[i][1] - y) <= 1000:
                dq.append(stores[i])
                visited[i] = 1
    else: print("sad")