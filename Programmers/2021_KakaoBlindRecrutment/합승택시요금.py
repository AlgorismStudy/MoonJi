from collections import deque

def find_min_fare(start, fare):
    answer = [987654321 for _ in range(n+1)]
    answer[start] = 0

    q = deque()
    q.append(start)
    
    while q:
        cur = q.popleft()
        for i in range(1, len(fare[cur])):
            if answer[i] > fare[start][cur] + fare[cur][i]:
                answer[i] = fare[start][cur] + fare[cur][i]
                q.append(i)
    return answer


def solution(n, s, a, b, fares):
    fare = [[987654321] * (n+1) for _ in range(n+1)]
    for i in range(1, 7):
        fare[i][i] = 0
    
    for f in fares:
        c, d, f = f
        fare[c][d] = f
        fare[d][c] = f

    s_answer = find_min_fare(s, fare)
    
    return answer


n, s, a, b = 6, 4, 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))