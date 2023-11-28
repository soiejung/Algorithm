import sys
# 시간초과 나서 넣었음
input = sys.stdin.readline
N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
prefix = [[ 0 for i in range(N+1)] for j in range(N+1)]

# 2차원 배열 누적합 => 왼쪽과 위에있는 값을 더 한 후 중복되는 값인 대각선 값을 한번 빼준 후 현재 그래프의 값을 더해준다
for i in range(N):
    for j in range(N):
        prefix[i+1][j+1] = matrix[i][j] + prefix[i][j+1]+prefix[i+1][j] - prefix[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    # x2,y2 까지 다 더한 값 에서 x2는 그대로이고 y1보다 1 작은 수를 빼주고, y2는 그대로이고 x1보다 1 작은 수를 빼주고 중복되어 빼진 x1-1, y1-1을 더해준다
    print(prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1])


