'''행성 터널'''

import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
parent = [i for i in range(N)]
edges = []
stars = []

for i in range(N):
    x, y, z = map(int, input().split())
    stars.append((x, y, z, i))

for j in range(3):
    stars.sort(key=lambda x:x[j])
    before = stars[0][3]
    for i in range(1, N):
        cur = stars[i][3]
        edges.append([abs(stars[i][j] - stars[i-1][j]), before, cur])
        before = cur

edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        union(a, b)
        result += cost

print(result)