'''직사각형'''

for _ in range(4):
    
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    result = 'a'

    if p1 < x2 or q1 < y2 or p2 < x1 or q2 < y1:
        result = 'd'
    elif p1 == x2:
        if q1 == y2 or y1 == q2: result = 'c'
        else:   result = 'b'
    elif q1 == y2:
        if p1 == x2 or x1 == p2: result = 'c'
        else: result = 'b'
    elif x1 == p2:
        if y1 == q2 or y2 == q1: result = 'c'
        else: result = 'b'
    elif q2 == y1:
        if x1 == p2 or x2 == p1: result = 'c'
        else: result = 'b'

    print(result)
            
