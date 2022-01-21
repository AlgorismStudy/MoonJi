'''경로 찾기'''

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = max(graph[a][b], graph[a][k] * graph[k][b])

for g in graph:
    print(*g, sep=" ")
