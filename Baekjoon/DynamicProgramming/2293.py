'''동전'''

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

d = [0 for _ in range(k+1)]
d[0] = 1

for c in coins:
    for i in range(1, k+1):
        if i >= c:
            d[i] += d[i-c]
print(d[k])
