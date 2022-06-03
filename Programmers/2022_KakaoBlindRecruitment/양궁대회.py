def cal_score(info1, info2):
    apeach, lion = 0, 0
    for i in range(11):
        if info1 >= info2:
            apeach += 10 - i
        else:
            lion += 10 - i
    if apeach >= lion:
        return False
    else:
        return True

def bfs(n, depth, answer, info):
    if depth == 11:
        if cal_score(info, answer):
            print(answer)
            exit()
        return
    
    for i in range(n):
        answer[depth] = i
        bfs(n, depth + 1, answer, info)
        answer[depth] = 0
    
def solution(n, info):
    answer = [0] * 11
    
    bfs(n, 0, answer, info)
            
    return answer

n = 5
info = 	[2,1,1,1,0,0,0,0,0,0,0]
solution(n, info)