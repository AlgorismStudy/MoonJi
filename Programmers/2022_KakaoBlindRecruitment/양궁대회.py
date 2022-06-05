'''양궁 대회'''

from copy import deepcopy

def cal_score(info1, info2):
    apeach, lion = 0, 0
    for i in range(11):
        if info1 >= info2:
            apeach += 10 - i
        else:
            lion += 10 - i
    return lion - apeach

def solution(n, info):

    def bfs(n, depth):
        global max_score, answer, result
        if depth == 11:
            if n != 0:  answer[10] = n
            score = cal_score(info, answer)
            if score > max_score:
                max_score = score
                result = deepcopy(answer)
                return
            return
        
        if info[depth] < n:
            answer[depth] = info[depth] + 1
            bfs(n - info[depth] - 1, depth + 1)
            answer[depth] = 0
        
        bfs(n, depth + 1)

    global max_score, answer, result
    
    answer = [0] * 11
    max_score = 0
    bfs(n, 0)
            
    return result

n = 5
info = 	[2,1,1,1,0,0,0,0,0,0,0]
print(solution(n, info))