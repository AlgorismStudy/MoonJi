'''카드 구매하기'''

N = int(input())
pack = list(map(int, input().split()))
dp = [0] * (N + 1)

for i in range(1, N + 1):
    for j in range(i, N + 1):
        dp[j] = max(dp[j], dp[j-i] + pack[i-1])

print(dp[N])
