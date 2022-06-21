from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = defaultdict(int)
    
    for order in orders:
        for i in range(2, len(order)+1):
            for l in list(combinations(order, i)):
                answer["".join(sorted(l))] += 1
            
    answer = sorted(answer.items(), key = lambda item : (len(item[0]), -item[1])) 
    
    result = []
    n = len(answer[0])
    max_value = answer[0][1]
    for menu, num in answer:
        if n == len(menu) and n in course and max_value == num and max_value > 1:
            result.append(menu)
        elif n != len(menu):
            n = len(menu)
            max_value = num
            if n in course and max_value > 1:
                result.append(menu)
    result = sorted(result)
    
    return result