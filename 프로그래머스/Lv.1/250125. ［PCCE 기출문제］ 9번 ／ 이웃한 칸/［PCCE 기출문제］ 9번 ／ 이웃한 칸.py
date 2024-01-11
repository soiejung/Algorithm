def solution(board, h, w):
    answer = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        x = h + dx[i]
        y = w + dy[i]
        
        if 0 <= x < len(board) and 0 <= y < len(board[x]):
            if board[h][w] == board[x][y]:
                answer += 1
    return answer