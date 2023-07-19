from collections import deque
def solution(board, moves):
    answer = 0
    matrix = []
    for b in board:
        matrix.append(b)
        
    stack = []
    for m in moves:
        for n in range(len(matrix)):
            if matrix[n][m-1] != 0:
                if stack and stack[-1] == matrix[n][m-1]:
                    stack.pop()
                    answer += 2
                    matrix[n][m-1] = 0
                else:
                    stack.append(matrix[n][m-1])
                    matrix[n][m-1] = 0
                break
            
    return answer