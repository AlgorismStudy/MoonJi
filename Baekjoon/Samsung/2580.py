'''스도쿠'''

import sys
input = sys.stdin.readline

maps = [list(map(int, input().split())) for _ in range(9)]
blank = []

def dfs(depth):
    if depth == len(blank):
        for i in range(9):
            print(*maps[i], sep=" ")
        sys.exit()

    x, y = blank[depth]

    for n in check_map(x, y):
        maps[x][y] = n
        dfs(depth+1)
        maps[x][y] = 0

def check_map(i, j):
    nums = set(range(10))

    # 3x3 체크
    x, y = i - i % 3, j - j % 3
    for l in maps[x:x+3]:
        for n in l[y:y+3]:
            if n in nums:
                nums.remove(n)

    # 행, 열 체크
    for k in range(9):
        if maps[k][j] in nums:
            nums.remove(maps[k][j])
        if maps[i][k] in nums:
            nums.remove(maps[i][k])

    return nums


for i in range(9):
    for j in range(9):
        if maps[i][j] == 0:
            blank.append((i, j))

dfs(0)