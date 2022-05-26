from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    mail = defaultdict(int)
    d = defaultdict(list)
    
    for r in report:
        a, b = r.split()
        if a not in d[b]:
            d[b].append(a)
        
    for key, value in d.items():
        if len(value) >= k:
            for v in value:
                mail[v] += 1       
                    
    for id in id_list:
        if mail[id] > 0:
            answer.append(mail[id])
        else:
            answer.append(0)
    
    return answer