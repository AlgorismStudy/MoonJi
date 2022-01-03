'''
바이러스

한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다. 1번 컴퓨터가 웜 바이러스에 걸렸을 때 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하라
'''
from collections import deque

n = int(input())
m = int(input())
computer = [[] for _ in range(n + 1)] 
for _ in range(m):
    n1, n2 = map(int, input().split())
    computer[n1].append(n2)
    computer[n2].append(n1)
for c in computer:
    c.sort()

d = deque()
d.append(1)
visited = [1]
while d:
    cur = d.popleft()
    for i in computer[cur]:
        if i not in visited:
            d.append(i)
            visited.append(i)
print(len(visited) - 1)
