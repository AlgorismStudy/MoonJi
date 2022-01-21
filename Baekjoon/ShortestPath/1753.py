'''최단 경로'''

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())    # 정점의 개수 V, 간선의 개수 E
K = int(input())                    # 시작 노드
graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split()) # u -> v (가중치 w)
    graph[u].append((v, w))

def dijkstra(K):
    q = []
    heapq.heappush(q, (0, K))
    distance[K] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(K)

for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
