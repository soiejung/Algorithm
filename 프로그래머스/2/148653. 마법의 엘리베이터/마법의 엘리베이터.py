def solution(storey):
    answer = 0
    c = len(str(storey))
    num = list(str(storey))
    idx = c-1
    while idx > -1:
        
        num = list(str(storey))
        # 5초과일때 올림
        if int(num[idx]) > 5:
            answer += (10 - int(num[idx]))
            storey += (10 - int(num[idx])) * (10 ** (c-1-idx))
            num = list(str(storey))
            if len(num) != c:
                idx += 1
        # 5 미만일때
        elif int(num[idx]) < 5:
            answer += int(num[idx])
            
        # 5일때
        else:
            if idx > 0:
                # 앞자리가 5 이상일때
                if int(num[idx-1]) >= 5:
                    answer += (10 - int(num[idx]))
                    storey += (10 - int(num[idx])) * (10 ** (c-1-idx))
                    num = list(str(storey))
                    if len(num) != c:
                        idx += 1
                else:
                    answer += int(num[idx])
            else:
                answer += int(num[idx])

        idx -= 1
    return answer