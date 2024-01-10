# https://www.acmicpc.net/problem/15654

import sys
input = sys.stdin.readline

def recur(number, lst):

    if number == M:
        print(*arr)
        return

    for l in lst:
        
        if l in arr:
            continue
        arr.append(l)
        recur(number+1, lst)
        arr.pop()



N, M = map(int, input().split())
arr = []
lst = list(map(int, input().split()))
lst.sort()
recur(0, lst)
