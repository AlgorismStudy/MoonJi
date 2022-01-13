'''
K번째 수

크기가 N x N인 배열 A가 있을 때 A[i][j] = i x j 이다. 배열 A를 일차원 배열 B에 넣었을 때 B[k]의 값을 구하라. 
배열 A와 B의 인덱스는 1부터 시작한다.
'''

import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

start, end = 1, K
while start <= end:
    mid = (start + end) // 2

    temp = 0
    for i in range(1, N+1):
        temp += min(mid//i, N)
    
    if temp >= K:
        end = mid - 1
    else:
        start = mid + 1

print(start)


