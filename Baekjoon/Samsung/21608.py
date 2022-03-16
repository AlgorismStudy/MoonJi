'''상어 초등학교'''

import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
arr = [[0] * N for _ in range(N)]
like_dict = defaultdict(list)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for _ in range(N*N):
    _input =  list(map(int, input().split()))
    like_dict[_input[0]] = _input[1:]

    cur = [0, 0]
    max_like = -1
    max_empty = -1
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                like, empty = 0, 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < N and 0 <= ny < N:
                        if arr[nx][ny] in _input:
                            like += 1
                        if arr[nx][ny] == 0:
                            empty += 1
                if like > max_like or (like == max_like and empty > max_empty):
                    max_like = like
                    max_empty = empty
                    cur = [i, j]
       
    arr[cur[0]][cur[1]] = _input[0]

result = 0
for i in range(N):
    for j in range(N):
        count = 0
        like = like_dict[arr[i][j]]

        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] in like:
                    count += 1
        if count != 0:
            result += 10 ** (count - 1)

print(result)
