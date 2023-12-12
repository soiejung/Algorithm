import sys

N, M = map(int, input().split())

def recur(count):

    if count == M:
        print(*arr)
        return

    for i in range(1, N+1):
        if i in arr:
            continue
        if arr:
            last = arr[-1]
            if i < last:
                continue
        arr.append(i)
        recur(count+1)
        arr.pop()


arr = []
recur(0)