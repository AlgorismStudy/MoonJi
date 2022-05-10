'''마법사 상어와 파이어볼'''

from collections import defaultdict

N, M, K = map(int, input().split())
# r, c, m, s, d
fireball = {}
for i in range(M):
    r, c, m, s, d = map(int, input().split())
    fireball[(r, c)] = [(m, s, d)]
# visited = [[0] * N for _  in range(N)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def move_fireball(key, value):
    r, c = key
    m, s, d = value
    nr = (r + dx[d] * s) % N
    nc = (c + dy[d] * s) % N
    moved_fireball = nr, nc, m, s, d
    return moved_fireball

def func1():
    global fireball
    new_fireball = defaultdict(list)
    for key, value in fireball.items():
        for v in value:
            r, c, m, s, d = move_fireball(key, v)
            new_fireball[(r, c)].append((m, s, d))
    fireball = new_fireball

def func():
    global fireball
    new_fireball = defaultdict(list)
    for key, value in fireball.items():
        r, c = key
        if len(value) == 1:
            new_fireball[(r, c)] += fireball[(r, c)]
        elif len(value) >= 2:
            new_m, new_s = 0, 0
            flag1, flag2 = True, True
            for v in value:
                m, s, d = v
                new_m += m
                new_s += s
                if d % 2 == 0: flag1 = False
                else: flag2 = False

            for i in range(4):
                if new_m//5 != 0:
                    if flag1 or flag2:
                        new_fireball[(r, c)].append((new_m//5, new_s//len(value), i * 2))
                    else:
                        new_fireball[(r, c)].append((new_m//5, new_s//len(value), i * 2 + 1))
    fireball = new_fireball

for i in range(K):
    func1()
    func()

result = 0
for key, value in fireball.items():
    for v in value:
        m, s, d = v
        result += m

print(result)