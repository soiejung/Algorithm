import re
def solution(book_time):
    answer = 1
    # 기본 1개
    time_table = []
    n = len(book_time)
    room = [[] for _ in range(len(book_time))]
    idx = 0
    
    for time in book_time:
        lst = []
        for t in time:
            a,b = re.split('[:]',t)
            hour = int(a) * 60
            # 10은 청소시간
            minute = int(b)
            lst.append(hour+minute)
        time_table.append(lst)
    
    # 입실 시간 기준 정렬
    time_table.sort(key = lambda x: x[0])
    
    room[idx%n].append(time_table[0])

    for i in range(1,len(time_table)):
        for j in range(n):
            if room[j]:         
                if room[j][-1][1] + 10 <= time_table[i][0]:
                    room[j].append(time_table[i])
                    break
                else:
                    continue
            idx += 1
            answer += 1
            room[idx%n].append(time_table[i])
            break
            
    
    return answer