'''N-Queen'''
import sys
input = sys.stdin.readline

N = int(input())
graph = [0] * N
result = 0

def dfs(cnt):
    global result, graph

    if cnt == N:
        result += 1
        return
    
    else:
        for i in range(N):
            is_queen = True
            for j in range(cnt):
                if graph[j] == i or abs(cnt - j) == abs(i - graph[j]):
                    is_queen = False
                    break
            if is_queen:
                graph[cnt] = i
                dfs(cnt + 1)
                graph[cnt] = 0

dfs(0)
print(result)