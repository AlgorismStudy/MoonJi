'''팀 결성'''

def find_parent(parent, x):
    if parent[x] == x:
        return parent[x]
    else:
        return find_parent(parent, parent[x])  

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
parent = [0] * (N + 1)
for i in range(1, N+1):
    parent[i] = i

for _ in range(M):
    oper, a, b = map(int, input().split())
    if oper == 0:
        union_parent(parent, a, b)

    elif oper == 1:
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a == b:
            print("YES")
        else:
            print("NO")