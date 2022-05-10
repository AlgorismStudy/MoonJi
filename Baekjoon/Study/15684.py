'''사다리 조작'''
import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
ladder = [[0] * N for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().split())
    ladder[a-1][b-1] = 1

result = 4

def is_same():
    for j in range(N):
        pos = j
        for i in range(H):
            if ladder[i][pos] == 1:
                pos += 1
            elif pos > 0 and ladder[i][pos-1] == 1:
                pos -= 1
        if pos != j:
            return False
    return True

def add_ladder(depth, x, y):
    global result
    if is_same():
        result = min(result, depth)
    if depth == 3 or result <= depth:
        return

    for i in range(x, H):
        for j in range(y, N - 1):
            if ladder[i][j] == 1 or (j > 0 and ladder[i][j-1] == 1) or ladder[i][j+1] == 1:
                continue
            ladder[i][j] = 1
            add_ladder(depth + 1, x, y+2)
            ladder[i][j] = 0
        y = 0


add_ladder(0, 0, 0)
if result > 3:
    print(-1)
else:
    print(result)