import sys
input = sys.stdin.readline

A, B = map(int, input().split())
lst = [i for i in range(10000001)]
lst[0] = 0
lst[1] = 0
for i in range(2, len(lst)):

    if lst[i] == 0:
        continue
    for j in range(2 * i, len(lst), i):
        lst[j] = 0

count = 0
for i in range(2, 10000001):
    p = lst[i] ** 2
    if p:
        while p <= B:

            if p < A:
                p *= lst[i]
                continue

            p *= lst[i]
            count += 1

print(count)