# https://www.acmicpc.net/problem/9251

import sys

#sys.stdin = open("CodeApp/input.txt","r")


A = list(input())
B = list(input())

dp = [[0 for _ in range(len(B)+1)]for _ in range(len(A)+1)]

for i in range(1,len(A)+1):
    for j in range(1,len(B)+1):
        if A[i-1] == B[j-1]:
            # 만약 같은 문자인 경우 끝에있는 그 문자를 없다고 생각한 후 이미 앞에서 구한 값에서 +1 해주기
            # ex) AC 와 CAPC를 비교한다 했을 때 끝에 있는 C를 없다 생각한 후 A와 CAP를 비교
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(A)][len(B)])
