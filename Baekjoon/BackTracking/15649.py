'''N과 M (1)'''

N, M = map(int, input().split())
arr = []

def seq(depth):
    if depth == M:
        print(*arr, sep=" ")
        return

    for i in range(1, N+1):
        if i not in arr:
            arr.append(i)
            seq(depth+1)
            arr.remove(i)

seq(0)