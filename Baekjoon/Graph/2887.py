'''행성 터널'''

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def make_cost(star_a, star_b):
    cost = 987654321
    for a, b in zip(star_a, star_b):
        if abs(a - b) < cost:
            cost = abs(a - b)
    return cost 

N = int(input())
parent = [0] * (N + 1)

stars = []
for _ in range(N):
    x, y, z = map(int, input().split())
    stars.append((x, y, z))

edges = []
result = 0

for i in range(1, N + 1):
    parent[i] = i

for i in range(N-1):
    for j in range(i, N):
        cost = make_cost(stars[i], stars[j])
        edges.append((cost, i, j))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)