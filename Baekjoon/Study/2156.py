'''포도주 시식'''
import sys
input = sys.stdin.readline

n = int(input())
wine = [0] + [int(input()) for _ in range(n)]

dp = [0] * (n+1)

dp[1] = wine[1]
if n < 2:
    print(wine[1])
else:
    dp[2] = wine[1] + wine[2]

    for i in range(3, n+1):
        dp[i] = max(dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i])
        dp[i] = max(dp[i-1], dp[i])

    print(max(dp))