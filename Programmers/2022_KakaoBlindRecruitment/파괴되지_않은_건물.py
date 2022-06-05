def solution(board, skills):
    b = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]

    for s in skills:
        type, r1, c1, r2, c2, degree = s
        if type == 1: degree *= -1
        
        b[r1][c1] += degree
        b[r1][c2 + 1] -= degree
        b[r2 + 1][c1] -= degree
        b[r2 + 1][c2 + 1] += degree
        
    answer = 0
    for i in range(len(b)):
        for j in range(1, len(b[0])):
            b[i][j] += b[i][j-1]
    for i in range(1, len(b)):
        for j in range(len(b[0])):
            b[i][j] += b[i-1][j]
    
    for i in range(len(board)):
        for j in range(len(board[0])): 
            if board[i][j] + b[i][j] > 0: answer += 1
            board[i][j] += b[i][j]
    return answer