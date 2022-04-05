'''치킨 배달'''
from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
city = []
chikens = []
house = []
for i in range(N):
    city.append(list(map(int, input().split())))
    for j in range(N):
        if city[i][j] == 2:
            chikens.append([i, j])
        if city[i][j] == 1:
            house.append([i, j])

result = 987654321

for chiken in combinations(chikens, M):
    total = 0
    for h in house:
        min_d = 200
        for c in chiken:
            d = abs(h[0] - c[0]) + abs(h[1] - c[1])
            min_d = min(min_d, d)
        total += min_d
    result = min(total, result)

print(result)

