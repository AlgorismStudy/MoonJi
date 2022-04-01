'''숨바꼭질'''
from collections import deque

N, K = map(int, input().split())
visit = [0] * 100001

q = deque([N])
while q:
    cur = q.popleft()
    if cur == K:
        break
    move = [cur - 1, cur + 1, cur * 2]
    for m in move:
        if 0 <= m <= 100000 and visit[m] == 0:
            q.append(m)
            visit[m] = visit[cur] + 1
    
print(visit[K])

        
