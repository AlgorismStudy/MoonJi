def solution(n, computers):
    visited = [0] * n
    answer = 0
    stack = []
    for v in range(n):
        if visited[v] == 0:
            answer += 1
            dfs(computers, v, visited)
        print(v, answer)
            
    
    return answer

def dfs(computers, v, visited):
    visited[v] = 1

    for i in range(len(computers)):
        if computers[v][i] == 1 and visited[i] == 0:
            dfs(computers, i, visited)

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))