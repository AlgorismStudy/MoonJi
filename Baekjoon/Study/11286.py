'''절댓값 힙'''
import heapq
import sys
input = sys.stdin.readline

n = int(input())
hq = []

for _ in range(n):
    num = int(input())

    if num == 0:
        if len(hq) == 0:
            print(0)
        else:
            min_value = heapq.heappop(hq)
            print(min_value[0] * min_value[1])

    elif num > 0:
        heapq.heappush(hq, (num, 1))
    else:
        heapq.heappush(hq, (-num, -1))

    