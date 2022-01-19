'''병사 배치하기'''

import sys
input = sys.stdin.readline

N = int(input())
soldiers = list(map(int, input().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):
        if soldiers[j] > soldiers[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(N - max(dp))