'''N과 M (1)'''

N, M = map(int, input().split())
arr = []

def seq(dept):
    global arr

    if dept == M:
        print(*arr, sep=" ")
        return

    for i in range(1, N+1):
        if i not in arr:
            arr.append(i)
            seq(dept+1)
            arr.remove(i)

seq(0)