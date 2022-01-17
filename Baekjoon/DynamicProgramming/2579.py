'''계단 오르기'''
import sys 
input = sys.stdin.readline

n = int(input())
s = [0] + [int(input()) for _ in range(n)]
d = [0] * (n + 1)

d[1] = s[1]
if n > 1:
    d[2] = s[1] + s[2]
for i in range(3, n+1):
    d[i] = max(s[i-1] + d[i-3], d[i-2]) + s[i]

print(d[n])