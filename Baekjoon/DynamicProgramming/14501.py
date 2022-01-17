'''퇴사'''

N = int(input())
T, P = [], []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0] * N
for i in range(N):
    temp = 0
    if T[i] + i > N:
        continue
    dp[i] = P[i]
    for j in range(i):
        if T[j] + j <= i and dp[j] > temp:
            temp = dp[j]
    dp[i] += temp

print(max(dp))
             