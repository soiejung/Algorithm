
T = int(input())
hint = [list(map(str, input().split())) for _ in range(T)]
answer = 0
# 세 자리 수 만들기
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):

            counter = 0

            if i == j or j == k or k == i:
                continue

            for h in hint:
                check = list(h[0]) # ['1','2','3']
                strike = int(h[1])
                ball = int(h[2])

                strike_count = 0
                ball_count = 0

                if i == int(check[0]):
                    strike_count += 1
                if j == int(check[1]):
                    strike_count += 1
                if k == int(check[2]):
                    strike_count += 1

                if i == int(check[1]) or i == int(check[2]):
                    ball_count += 1
                if j == int(check[0]) or j == int(check[2]):
                    ball_count += 1
                if k == int(check[0]) or k == int(check[1]):
                    ball_count += 1

                if strike != strike_count:
                    break

                if ball != ball_count:
                    break

                counter += 1

            if counter == T:
                answer += 1
print(answer)