from collections import defaultdict, deque

def solution(enroll, referral, seller, amount):
    answer = defaultdict(int)
    dict_enr = {}
    
    for e, r in zip(enroll, referral):
        dict_enr[e] = r
        answer[e] = 0
    
    for s, a in zip(seller, amount):
        q = deque()
        q.append(s)
        price = a * 100
        
        while q:
            cur = q.pop()
            parent = dict_enr[cur]
            
            if price * 0.1 < 1:
                answer[cur] += price
                price = 0
            else:
                answer[cur] += price - int(price * 0.1)
                price = int(price * 0.1)
            
            if parent != "-":
                q.append(parent)    
    
    result = list(answer.values())
    
    return result