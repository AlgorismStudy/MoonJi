'''전보'''

INF = int(1e9)
N, M, C = map(int, input().split())
graph = [[INF] * (N+1) for _ in range(N+1)]
for _ in range(M):
    x, y, z = map(int, input().split())
    graph[x][y] = z

for a in range(N):
    graph[a][a] = 0

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
count = 0
time = 0
for i in range(N):
    if graph[C][i] < INF:
        count += 1
        time += graph[C][i]

print(count, time)