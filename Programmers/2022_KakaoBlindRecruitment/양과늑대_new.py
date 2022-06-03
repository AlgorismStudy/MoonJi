'''양과 늑대'''

from collections import defaultdict

def solution(info, edges):
    answer = 0
    tree = defaultdict(list)
    visited = [0] * len(info)
    for edge in edges:
        parent, child = edge
        tree[parent].append(child)
    
    def dfs(node, sheep, wolf):
        global max_sheep

        if info[node] == 0:
            sheep += 1
            max_sheep = max(sheep, max_sheep)
        else:
            wolf += 1
            if wolf >= sheep:
                return 

        for i in range(len(visited)):
            if visited[i] == 1:
                child = tree[i]
                for c in child:
                    if visited[c] == 0:
                        visited[c] = 1
                        dfs(c, sheep, wolf)
                        visited[c] = 0
        return
    
    global max_sheep
    max_sheep = 0
    visited[0] = 1
    dfs(0, 0, 0)
    return max_sheep

info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

# info = [0,1,0,1,1,0,1,0,0,1,0]
# edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
print(solution(info, edges))