import sys
import math
import itertools

input = sys.stdin.readline

X = input().rstrip()
lst = []

for value in itertools.permutations(X, len(X)):

    s = ''
    for v in value:
        s += v
    lst.append(s)

lst.sort()
flag = 0

for l in lst:

    if l[0] != '0':
        if l != X and l > X:
            print(l)
            flag = 1
            break

if not flag:
    print(0)



