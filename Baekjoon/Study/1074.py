'''Z'''

N, r, c = map(int, input().split())

dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]

def visit(s, n, x, y):
    if n == 1:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == r and ny == c:
                print(s + i)
                exit()
        return
    
    n -= 1
    for i in range(4):
        nx = x + dx[i] * (2 ** n)
        ny = y + dy[i] * (2 ** n)
        if nx <= r < nx + (2 ** n) and ny <= c < ny + (2 ** n):
            visit(s + i * (2 ** (2 * n)), n, nx, ny)

visit(0, N, 0, 0)