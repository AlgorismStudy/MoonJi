'''2 x n 타일링2'''
import sys 
input = sys.stdin.readline

N = int(input())
d = [0] * N

d[0] = 1
if N > 1:
    d[1] = 3

for i in range(2, N):
    d[i] = (d[i-1] + 2 * d[i-2]) % 10007

print(d[N-1])