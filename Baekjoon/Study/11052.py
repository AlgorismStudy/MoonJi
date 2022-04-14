'''카드 구매하기'''

N = int(input())
pack = list(map(int, input().split()))

# price_per_piece = [(pack[i] / (i + 1), i + 1)for i in range(N)]
# price_per_piece.sort(reverse=True)

# total = 0
# count = 0
# for p, n in price_per_piece:
#     while count + n <= N:
#         count += n
#         total += p * n
#     if count == N:
#         break

# print(int(total))

dp = [0] * (N + 1)

for i in range(1, N + 1):
    for j in range(i, N + 1):
        dp[j] = max(dp[j], dp[j-i] + pack[i-1])

print(dp[N])
