# https://www.acmicpc.net/problem/15655
import sys
input = sys.stdin.readline

def recur(number, lst):

    if number == M:
        print(*arr)
        return

    for l in lst:

        flag = 1
        if l in arr:
            continue
        
        for a in arr:
            if l < a:
                flag = 0

        if flag:
            arr.append(l)
            recur(number+1, lst)
            arr.pop()


N, M = map(int, input().split())
arr = []

lst = list(map(int, input().split()))
lst.sort()

recur(0,lst)
    