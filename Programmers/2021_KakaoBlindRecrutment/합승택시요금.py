def solution(n, s, a, b, fares):
    fee = [[987654321] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        fee[i][i] = 0
    
    for c, d, f in fares:
        fee[c][d] = f
        fee[d][c] = f

    for r in range(1, n+1):
        for start in range(1, n+1):
            for end in range(1, n+1):
                fee[start][end] = min(fee[start][end], fee[start][r] + fee[r][end])
    
    answer = 987654321
    for i in range(1, n+1):
        answer = min(answer, fee[s][i] + fee[i][a] + fee[i][b])

    return answer


n, s, a, b = 6, 4, 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))