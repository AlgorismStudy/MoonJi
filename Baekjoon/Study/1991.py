'''트리 순회'''

N = int(input())
graph = {}

for _ in range(N):
    parent, left, right = input().split()
    graph[parent] = [left, right]

def preTraversal(node):
    if node == ".": return
    print(node, end="")
    preTraversal(graph[node][0])
    preTraversal(graph[node][1])

def inTraversal(node):
    if node == ".": return
    inTraversal(graph[node][0])
    print(node, end="")
    inTraversal(graph[node][1])
    pass

def postTraversal(node):
    if node == ".": return
    postTraversal(graph[node][0])
    postTraversal(graph[node][1])
    print(node, end="")

preTraversal('A')
print()
inTraversal('A')
print()
postTraversal('A')