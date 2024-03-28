def solution(m, n, board):
    answer = 0
    
    dx = [0,1,1,0]
    dy = [1,1,0,0]
    matrix = []
    
    # 배열화
    for b in board:
        lst = []
        for bb in b:
            lst.append(bb)
        matrix.append(lst)
    
    
    while True: 
        idx = []
        for i in range(len(matrix)-1):
            for j in range(len(matrix[i])-1):
                
                if matrix[i][j] != '-':
                    
                    # 오른쪽, 대각선, 아래가 같은 문양인지 확인
                    for k in range(3):
                        xx = i + dx[k]
                        yy = j + dy[k]

                        flag = 1
                        if 0 <= xx and xx <= len(matrix)-1 and 0 <= yy and yy <= len(matrix[i])-1:
                            if matrix[i][j] != matrix[xx][yy]:
                                flag = 0
                                break
                    # 모두 같다면
                    if flag:
                        for k in range(4):
                            xx = i + dx[k]
                            yy = j + dy[k]
                            # 위치 추가
                            if [xx,yy] not in idx:
                                idx.append([xx,yy])
                                answer += 1

        # 터질 볼록이 존재한다면(4개가 같음) - 로 변경
        if idx:
            for i in idx:
                x, y = i
                matrix[x][y] = '-'

            for i in range(len(matrix)-1,0,-1):
                for j in range(len(matrix[i])):
                    if matrix[i][j] == '-':
                        # 아래서부터 채울 블록 찾아서 가져오기
                        for k in range(i-1,-1,-1):
                            if matrix[k][j] != '-':
                                matrix[i][j] = matrix[k][j]
                                matrix[k][j] = '-'
                                break
        else:
            break
    
    return answer