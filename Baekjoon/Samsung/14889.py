'''스타트와 링크'''

from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

com = list(combinations(range(N), N//2))
result = 987654321

for i in range(len(com)):
    team1 = com[i]
    team2 = [n for n in range(N) if n not in team1]
    s_1, s_2 = 0, 0
    for j in team1:
        for k in team1:
            s_1 += S[j][k]

    for j in team2:
        for k in team2:
            s_2 += S[j][k]

    if abs(s_1 - s_2) < result:
        result = abs(s_1 - s_2)

print(result)