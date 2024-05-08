import itertools
def solution(routes):
    answer = 1
    queue = []
    routes.sort(key = lambda x: x[1])
    
    camera = routes[0][1]
    for r in routes:

        if camera < r[0]:
            camera = r[1]
            answer += 1

    return answer