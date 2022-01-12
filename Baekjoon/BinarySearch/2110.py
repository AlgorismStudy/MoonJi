'''
공유기 설치

집 N개가 수직선 위에 있다. 각각의 집의 좌표는 X1, X2, ..., Xn이고, 집 여러개가 같은 좌표를 가지는 일은 없다.
공유기 C개를 설치하려고 한다. 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치한다.
C개의 공유기를 N개의 집에 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하라.
'''
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]
house.sort()

start, end = 0, max(house)
max_d = 0
while start <= end:
    d = 0
    mid = (start + end) // 2
    wifi = [0]
    for i in range(1, N):
        d += house[i] - house[i-1]
        if d >= mid:
            wifi.append(i)
            d = 0
    if len(wifi) >= C:
        if mid > max_d:
            max_d = mid
        start = mid + 1
    elif len(wifi) < C:
        end = mid - 1


print(max_d)