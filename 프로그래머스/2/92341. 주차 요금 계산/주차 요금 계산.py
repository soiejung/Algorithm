import re
def solution(fees, records):
    answer = []
    lst = []
    std_time = fees[0]
    std_fee = fees[1]
    uni_time = fees[2]
    uni_fee = fees[3]
    
    in_cars = {}
    out_cars = {}
    time_cars = {}
    check = {}
    
    for r in records:
        value, key, inout = r.split()
        check[key] = 0
        
    for r in records:
        
        value, key, inout = r.split()
        times = []

        for t in re.split('[:]',value):
            times.append(int(t))
        
        
        if inout == "IN":
            check[key] += 1
            if key in in_cars.keys():
                in_cars[key] += times[0] * 60 + times[1]
                
            else:
                in_cars[key] = times[0] * 60 + times[1]
                
        elif inout == "OUT":
            check[key] -= 1
            if key in out_cars.keys():
                out_cars[key] += times[0] * 60 + times[1]
            else:
                out_cars[key] = times[0] * 60 + times[1]

            

    for key in in_cars.keys():
        if check[key] != 0:
            if key not in out_cars.keys():
                out_cars[key] = 23 * 60 + 59
            else:
                out_cars[key] += 23 * 60 + 59
                
    
    for key in in_cars.keys():
        
        time_cars[key] = out_cars[key] - in_cars[key]


    for key in time_cars.keys():
        
        if time_cars[key] > std_time:
            if (time_cars[key] - std_time) % uni_time != 0: 
                f = std_fee + ((time_cars[key] - std_time) // uni_time + 1) * uni_fee
            else:
                f = std_fee + ((time_cars[key] - std_time) / uni_time) * uni_fee
        else:
            f = std_fee
            
        lst.append([key, int(f)])

    lst.sort(key = lambda x : x[0])
    
    for l in lst:
        answer.append(l[1])
        
    return answer