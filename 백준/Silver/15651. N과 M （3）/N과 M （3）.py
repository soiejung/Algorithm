import sys

N, M = map(int, input().split())

def recur(count):

    if count == M:
        print(*arr)
        return
    
    for i in range(1, N+1):
        arr.append(i)
        recur(count+1)
        arr.pop()

arr = []
recur(0)