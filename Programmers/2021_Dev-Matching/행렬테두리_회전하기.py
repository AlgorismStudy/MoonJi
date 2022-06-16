def solution(rows, columns, queries):
    answer = []
    global board
    board = [[columns * j + i + 1 for i in range(columns)] for j in range(rows)]
    
    def turn(query):
        global board
        x1, y1, x2, y2 = query
        ex, cur = 0, 0
        ex = board[x1-1][y1-1]
        min_num = ex

        for j in range(y1, y2):
            cur = board[x1-1][j]
            board[x1-1][j] = ex
            ex = cur
            min_num = min(ex, min_num)
        for i in range(x1, x2):
            cur = board[i][y2-1]
            board[i][y2-1] = ex
            ex = cur
            min_num = min(ex, min_num)
        for j in range(y2-2, y1-2, -1):
            cur = board[x2-1][j]
            board[x2-1][j] = ex
            ex = cur
            min_num = min(ex, min_num)
        for i in range(x2-2, x1-2, -1):
            cur = board[i][y1-1]
            board[i][y1-1] = ex
            ex = cur
            min_num = min(ex, min_num)
        return min_num
        
    for query in queries:
        answer.append(turn(query))
    return answer

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries))