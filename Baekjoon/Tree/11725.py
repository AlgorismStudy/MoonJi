'''트리의 부모 찾기'''
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

result = [0] * (N+1)
dq = deque([1])

while  dq:
    parent = dq.popleft()
    child = tree[parent]
    for c in child:
        if result[c] == 0:
            result[c] = parent
            dq.append(c)

print(*result[2:], sep="\n")