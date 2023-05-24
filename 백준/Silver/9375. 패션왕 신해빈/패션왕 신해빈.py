import sys
input = sys.stdin.readline

T = int(input().rstrip())

for test_case in range(T):

    N = int(input().rstrip())
    clothes = {}
    for n in range(N):
        v, k = input().split()
        lst = []
        if k in clothes.keys():
            for c in clothes[k]:
                lst.append(c)
            lst.append(v)
            clothes[k] = lst
        else:
            lst.append(v)
            clothes[k] = lst

    key_count = len(clothes)
    count = []
    for k in clothes.keys():
        value_count = len(clothes[k])
        count.append(value_count)
    count.append(0)

    result = 1
    for i in range(len(count)):
        result *= (count[i]+1)
    print(result-1)
