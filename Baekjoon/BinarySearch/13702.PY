'''
이상한 술집

막걸리를 N 주전자를 주문하고, 자신을 포함한 친구들 K명에게 막걸리를 똑같은 양으로 나눠주려고 한다. 분배 후 주전자에 막걸리가 남아 있다면 그냥 막걸리를 버린다. K명에게 최대한의 많은 양의 막걸리를 분배할 수 있는 용량 ml를 구하라.
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
pot = [int(input()) for _ in range(N)]

start, end = 1, max(pot)
max_drink = 0
while start <= end:
    mid = (start + end) // 2
    count = 0
    for p in pot:
        count += p // mid

    if count >= K:
        if mid > max_drink:
            max_drink = mid
        start = mid + 1
    else:
        end = mid - 1

print(max_drink)