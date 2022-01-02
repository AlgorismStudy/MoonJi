'''
DFS와 BFS

그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다.
'''
from collections import deque

def main():
    # 정점, 간선, 시작 정점
    N, M, V = map(int, input().split())
    graph = [[] for _ in range(N + 1)] 

    for _ in range(M):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)

    for g in graph:
        g.sort()

    visited = []
    DFS(graph, V, visited)
    print(*visited, sep=" ")
    visited = []
    BFS(graph, V, visited)
    print(*visited, sep=" ")


def DFS(graph, v, visited):
    visited.append(v)
    for i in range(len(graph[v])):
        if graph[v][i] not in visited:
            DFS(graph, graph[v][i], visited)

def BFS(graph, v, visited):
    d = deque()
    d.append(v)
    visited.append(v)
    while d:
        cur = d.popleft()
        for i in range(len(graph[cur])):
            if graph[cur][i] not in visited:
                d.append(graph[cur][i])
                visited.append(graph[cur][i])

main()