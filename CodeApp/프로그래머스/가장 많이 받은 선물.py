# https://school.programmers.co.kr/learn/courses/30/lessons/258712
def solution(friends, gifts):
    answer = 0
    give = {} # 선물 준 횟수
    take = {} # 선물 받은 횟수

    # 사람들끼리 선물 주고 받은 횟수 2차원 배열
    matrix = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    # 선물 지수 배열
    point = []
    # 다음 달에 받을 선물 수 배열
    present = [0 for _ in range(len(friends))]


    for f in friends:
        give[f] = 0
        take[f] = 0
    
    # 선물 준 횟수와 받은 횟수 구하기, 선물 주고 받은 횟수 2차원 배열 값 구하기
    for i in range(len(gifts)):
        who , to = gifts[i].split()
        give[who] += 1
        take[to] += 1
        
        for j in range(len(friends)):
            for p in range(len(friends)):
                if who == friends[j]:
                    if to == friends[p]:
                        matrix[j][p] += 1

    # 선물 지수 값 구하기
    for key in give.keys():
        point.append(give[key] - take[key])
        
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            
            # 자기 자신은 선물 주고 받기 제외
            if i != j:
                # 만약 선물을 더 많이 줬다면 다음 달에 선물 받기
                if matrix[i][j] > matrix[j][i]:
                    present[i] += 1
                
                elif matrix[i][j] < matrix[j][i]:
                    present[j] += 1

                # 만약 선물을 서로 주고 받지 않았거나, 서로 주고 받은 횟수가 같다면    
                else:
                    # 선물 지수가 큰 쪽이 작은쪽에게 다음 달에 선물 받기
                    # 만약 선물 지수 까지 같다면 다음 달에 선물 받지 않는다.
                    if point[i] > point[j]:
                        present[i] += 1
                    elif point[i] < point[j] :
                        present[j] += 1
    
    # 현재 present 배열에는 2배의 값이 들어있음(위 for문에서 비교를 2번 하기 때문)
    for i in range(len(present)):
        present[i] = int(present[i]/2)
    
    answer = max(present)

    return answer
