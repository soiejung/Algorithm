def solution(progresses, speeds):
    answer = []
    days = []

    for i in range(len(progresses)):
        day = (100 - progresses[i])/speeds[i]
        plus = (100 - progresses[i])%speeds[i]
        if plus != 0:
            day +=1
        days.append(int(day))

    while days:
        tmp = days.pop(0)
        c=1
        while days and tmp >= days[0]:
            days.pop(0)
            c+=1
        answer.append(c)

        
    return answer