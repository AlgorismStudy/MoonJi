'''
게임

게임 횟수 : X
이긴 게임 : Y (Z%)
Z는 형택이의 승률이고, 소수점은 버린다.
X와 Y가 주어졌을 때, 형택이가 게임을 최소 몇 번 더 해야 Z가 변하는지 구하는 프로그램을 작성하시오.
'''

X, Y = map(int, input().split())

Z = Y * 100 // X
count = 0
start, end = 0, X

while start <= end:
    mid = (start + end) // 2
    new_Z = (Y + mid) * 100 // (X + mid)
    if new_Z <= Z:
        start = mid + 1
    else:
        end = mid - 1
if start > X:
    print(-1)
else:  
    print(start)