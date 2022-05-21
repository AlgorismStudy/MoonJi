'''퇴사 2'''

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (N + 1)

for i in range(1, N + 1):
    t, p = arr[i-1]
    
    if dp[i] < dp[i - 1]:
        dp[i] = dp[i - 1]

    if i + t - 1 > N:
        continue
    dp[i - 1 + t] = max(dp[i - 1] + p, dp[i - 1 + t])

print(dp[N])