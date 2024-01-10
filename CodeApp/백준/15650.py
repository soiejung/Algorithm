# https://www.acmicpc.net/problem/15650
import sys
input = sys.stdin.readline

def recur(number):

    if number == M:
        print(*arr)
        return

    for i in range(1, N+1):
        if i in arr:
            continue
        flag = 1
        for a in arr:
            if i < a:
                flag = 0
        if flag:
            arr.append(i)
            recur(number+1)
            arr.pop()



N, M = map(int, input().split())
arr = []
recur(0)
