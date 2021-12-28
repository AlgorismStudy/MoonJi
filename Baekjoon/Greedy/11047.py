'''
동전 0

동전은 총 N종류이고 개수는 매우 많다. 가치의 합을 K로 만들 때 필요한 동전 개수의 최솟값을 구하라
'''

N, K = map(int, input().split())

coins = [int(input()) for i in range(N)]
coins.sort(reverse=True)

count = 0
for coin in coins:
    if coin <= K:
        count += K // coin
        K %= coin

print(count)
