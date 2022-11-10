N = int(input())
A = list(map(int, input().split()))
operator = list(map(int, input().split()))

def solution(N, A, operator):
    global max_value, min_value
    max_value = -987654321
    min_value = 987654321

    backtracking(N, A, operator, 1, A[0])
    print(max_value)
    print(min_value)
    

def backtracking(N, A, operator, depth, value):
    global max_value, min_value
    if depth == N:
        max_value = max(max_value, value)
        min_value = min(min_value, value)
        return

    if operator[0] > 0:
        operator[0] -= 1
        backtracking(N, A, operator, depth+1, value + A[depth])
        operator[0] += 1
    
    if operator[1] > 0:
        operator[1] -= 1
        backtracking(N, A, operator, depth+1, value - A[depth])
        operator[1] += 1

    if operator[2] > 0:
        operator[2] -= 1
        backtracking(N, A, operator, depth+1, value * A[depth])
        operator[2] += 1

    if operator[3] > 0:
        operator[3] -= 1
        backtracking(N, A, operator, depth+1, int(value / A[depth]))
        operator[3] += 1

solution(N, A, operator)