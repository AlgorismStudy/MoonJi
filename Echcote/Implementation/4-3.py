'''
왕실의 나이트

왕실 정원은 8 x 8 좌표 평면이다. 나이트는 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없다. 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하라.
'''

k = input()

x = ord(k[0]) - 96
y = int(k[1])

dx = [-2, -2, 2, 2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, -2, -2, 2, 2]

count = 0

for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx > 0 and nx <= 8 and ny > 0 and ny <= 8:
        count += 1

print(count)