INF = 987654321
def solution(n, s, a, b, fares):
    fare = [[INF] * (n+1) for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]

    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))
        

    def find_min_fare(start, fare):
        distance = [INF] * (n+1)
        visited = [False] * (n+1)

        def get_smallest_node():
            min_value = INF
            index = 0
            for i in range(1, n+1):
                if distance[i] < min_value and not visited[i]:
                    min_value = distance[i]
                    index = i
            return index


        distance[start] = 0
        visited[start] = True
        for j in graph[start]:
            distance[j[0]] = j[1]
        for i in range(n-1):
            now = get_smallest_node()
            visited[now] = True

            for j in graph[now]:
                cost = distance[now] + j[1]
                if cost < distance[j[0]]:
                    distance[j[0]] = cost
        return distance

    s_answer = find_min_fare(s, fare)
    answer = 987654321
    for i in range(1, n+1):
        i_answer = find_min_fare(i, fare)
        answer = min(answer, s_answer[i] + i_answer[a] + i_answer[b])

    return answer


n, s, a, b = 6, 4, 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares)) 