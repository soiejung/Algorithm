def solution(bridge_length, weight, truck_weights):
    answer = 0
    run = [0] * bridge_length
    sum = 0
    while len(run):
       
        answer += 1
        r = run.pop(0)
        sum -= r
        if truck_weights:
            if sum + truck_weights[0] <= weight:
                t = truck_weights.pop(0)
                run.append(t)
                sum += t
            else:
                run.append(0)         
    return answer