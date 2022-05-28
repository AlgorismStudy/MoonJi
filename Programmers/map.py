def solution(N, L):
    # 두 점의 방향 맞추기
    for i in range(N):
        if L[i][0] > L[i][2]:
            X1, Y1, X2, Y2 = L[i]
            L[i] = X2, Y2, X1, Y1
    x = []
    y = []

    for i in range(N-1):
        for j in range(i+1, N):
            overX = isOverlapX(L[i], L[j])
            overY = isOverlapY(L[i], L[j])
            # X와 Y가 둘 다 겹쳐야 사각형이 겹침
            if overX * overY != 0:
                x.append(overX)
                y.append(overY)
    print(x, y)
    if len(x) == 1:
        return min(abs(x[0]), abs(y[0]))

    min_answer = 987654321
    for i in range(len(x)):
        answer = 0
        for j in range(len(x)):
            if i == j:
                continue
            else:
                answer += min(abs(x[i]), abs(y[i]))
        min_answer = min(min_answer, answer)
    
    return min_answer

def isOverlap(N, L):
    for i in range(N-1):
        for j in range(i+1, N):
            overX = isOverlapX(L[i], L[j])
            overY = isOverlapY(L[i], L[j])
            # X와 Y가 둘 다 겹쳐야 사각형이 겹침
            if overX * overY != 0:
                return True
    return False

def isOverlapX(L1, L2):
    a1, a2 = min(L1[0], L1[2]), max(L1[0], L1[2])
    b1, b2 = min(L2[0], L2[2]), max(L2[0], L2[2])

    if a1 <= b1 <= a2 <= b2:
        return a2 - b1 + 1
    if a1 <= b1 <= b2 <= a2:
        return b2 - b1 + 1
    if b1 <= a1 <= b2 <= a2:
        return a1 - b2 - 1
    if b1 <= a1 <= a2 <= b2:
        return a1 - a2 - 1
    return 0

def isOverlapY(L1, L2):
    a1, a2 = min(L1[1], L1[3]), max(L1[1], L1[3])
    b1, b2 = min(L2[1], L2[3]), max(L2[1], L2[3])

    if a1 <= b1 <= a2 <= b2:
        return a2 - b1 + 1
    if a1 <= b1 <= b2 <= a2:
        return b2 - b1 + 1
    if b1 <= a1 <= b2 <= a2:
        return a1 - b2 - 1
    if b1 <= a1 <= a2 <= b2:
        return a1 - a2 - 1
    return 0


print(solution(3, [[5,7,6,6],[3,9,5,4],[8,2,7,6]]))
print(solution(3, [[2,11,5,6],[4,12,7,9],[5,9,10,5]]))