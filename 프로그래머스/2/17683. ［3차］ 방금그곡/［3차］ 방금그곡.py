import re
def solution(m, musicinfos):
    answer = ''
    dic = []
    for music in musicinfos:
        start_s, end_s, title, melody = re.split('[,]',music)
        melody_l = list(melody)
        for i in range(1,len(melody_l)):
            if melody_l[i] == '#':
                melody_l[i-1] = melody_l[i-1].lower()
        melody = ''
        for i in range(len(melody_l)):
            if melody_l[i] != '#':
                melody += melody_l[i]
            
        start, end = 0,0
        
        hour_s, minute_s = re.split('[:]',start_s)
        start = int(hour_s) * 60 + int(minute_s)
        
        hour_e, minute_e = re.split('[:]',end_s)
        end = int(hour_e) * 60 + int(minute_e)

        
        total_time = end - start

        s = ''
        if len(melody) > total_time:
            for i in range(total_time):
                s += melody[i]
        elif len(melody) == total_time:
            s = melody 
        else:
            a = int(total_time / len(melody))
            melody *= (a+1)

            for i in range(total_time):
                s += melody[i]


        dic.append([title,s,total_time])
    

    m_l = list(m)
    for i in range(1,len(m_l)):
        if m_l[i] == '#':
            m_l[i-1] = m_l[i-1].lower()
            
    m = ''
    for i in range(len(m_l)):
        if m_l[i] != '#':
            m += m_l[i]

    dic.sort(key = lambda x: (x[2]), reverse = True)

    for i in range(len(dic)):
        for j in range(len(dic[i])):
            if m in dic[i][1]:
                return dic[i][0]
    

    return "(None)"