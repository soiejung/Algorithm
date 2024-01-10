# https://school.programmers.co.kr/learn/courses/30/lessons/250137#
def solution(bandage, health, attacks):
    answer = 0
    
    # 시간 제한
    limit = attacks[-1][0]
    # 현재 체력
    now_health = health
    # 현재 시간
    now = 0
    # attacks의 index
    idx = 0
    # 연속 회복 카운트
    count = 0
    # 초가 제한시간을 넘어가지 않을 때까지
    while now <= limit:
        
        # 만약 현재 시간이 공격당한 시간과 같을 때
        if now == attacks[idx][0]:
            # 현재 체력에서 공격당한 데미지 빼기
            now_health -= attacks[idx][1]
            # 다음 공격으로 이동
            idx += 1
            # 연속 회복 카운트 초기화
            count = 0
        else:
            # 만약 현재 시간이 공격당한 시간이 아닐 때
            # 현재 체력이 최대 체력보다 작을 때 붕대 감기, 연속 회복 카운트 + 1
            if now_health < health:
                now_health += bandage[1]
                count += 1
            else:
                # 현재 체력이 최대 체력보다 크거나 같을 때는 붕대를 감지 않는다. 연속 회복 카운트 초기화
                if now_health >= health:
                    now_health = health
                    count = 0
        
        # 시전시간동안 붕대로 회복한 경우
        if count == bandage[0]:
            # 추가 체력을 현재 체력에 추가해준다.
            now_health += bandage[2]
            # 만약 현재 체력이 최대 체력보다 큰 경우 그 이상으로 추가되지 않는다.
            if now_health >= health:
                now_health = health
            # 연속 회복 카운트 초기화
            count = 0
        
        # 만약 제한 시간 내에 현재 체력이 0 이하로 떨어지면 -1을 리턴
        if now_health <= 0:
            return -1
    
        # 현재 시간 + 1
        now += 1
        
        
    return now_health