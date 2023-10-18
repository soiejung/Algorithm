
T = int(input())
answer = [-1 for i in range(T)]
home = [list(map(int, input().split())) for _ in range(T)]
home_x = []
home_y = []
for h in home:
    home_x.append(h[0])
    home_y.append(h[1])


for x in home_x:
    for y in home_y:
        dist = []
        for ex, ey in home:
            d = abs(ex - x) + abs(ey - y)
            dist.append(d)

        #가까운 순서대로 정렬
        dist.sort()

        tmp = 0
        for i in range(len(dist)):
            d = dist[i]
            tmp += d
            if answer[i] == -1:
                answer[i] = tmp
            else:
                answer[i] = min(tmp, answer[i])

print(*answer)