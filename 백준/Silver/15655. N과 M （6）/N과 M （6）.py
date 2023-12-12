import sys

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

def recur(count):

    if count == M:
        print(*arr)
        return
    
    for l in lst:

        if l in arr:
            continue
        if arr:
            last = arr[-1]
            if l < last:
                continue
        arr.append(l)
        recur(count+1)
        arr.pop()
    
arr = []
recur(0)