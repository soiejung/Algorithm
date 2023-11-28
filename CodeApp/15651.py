# https://www.acmicpc.net/problem/15651

import sys
input = sys.stdin.readline

def recur(number):

    if number == M:
        print(*arr)
        return

    for i in range(1, N+1):
        
        arr.append(i)
        recur(number+1)
        arr.pop()



N, M = map(int, input().split())
arr = []
recur(0)
