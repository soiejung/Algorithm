from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for _ in range(bridge_length)]
    bridge = deque(bridge)
    truck = deque(truck_weights)
    w = 0
    while bridge:
        
        answer += 1
        b = bridge.popleft()
        w -= b
        if truck:
            if w + truck[0] <= weight:
                t = truck.popleft()
                bridge.append(t)
                w += t
            else:
                bridge.append(0)

    return answer