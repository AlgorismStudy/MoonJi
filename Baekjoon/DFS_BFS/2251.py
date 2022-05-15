'''물통'''

from collections import deque

A, B, C = map(int, input().split())

result = []

q = deque()
q.append(C)

while q:
    cur = q.popleft()
    
