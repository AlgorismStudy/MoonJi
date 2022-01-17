'''효율적인 화폐 구성'''

N, M = map(int, input().split())
coins = [int(input()) for _ in range(N)]
d = [10001] * (M + 1)

d[0] = 0
for i in range(N):
    for j in range(coins[i], M + 1):
        if d[j - coins[i]] != 10001:
            d[j] = min(d[j], d[j - coins[i]] + 1)

if d[M] == 10001:
    print(-1)
else:
    print(d[M])