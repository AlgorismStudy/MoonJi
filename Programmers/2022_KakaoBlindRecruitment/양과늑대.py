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
        if node in tree.keys():
            child = tree[node]
            child.sort(key = lambda x:info[x])
            for c in child:
                if info[c] == 0:
                    sheep, wolf = dfs(c, sheep + 1, wolf)
                elif info[c] == 1:
                    nsheep, nwolf = dfs(c, sheep, wolf + 1)
                    if nsheep > nwolf + 1:
                        sheep, wolf = nsheep, nwolf
            return sheep, wolf
        else:
            return sheep, wolf
    
    sheep, wolf = dfs(0, 1, 0)
    
    return answer

# info = [0,0,1,1,1,0,1,0,1,0,1,1]
# edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

info = [0,1,0,1,1,0,1,0,0,1,0]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
solution(info, edges)