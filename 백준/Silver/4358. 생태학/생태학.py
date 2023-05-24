import sys

input = sys.stdin.readline
tree = {}
i = 0
while True:
    name = input().rstrip()
    if not name:
        break
    else:
        if name in tree.keys():
            tree[name] += 1
        else:
            tree[name] = 1
lst = []
total = 0
for v in tree.values():
    total += v

for k, v in tree.items():
    v = (v/total) * 100
    lst.append([k,v])

lst.sort(key=lambda x: x[0])
for l in lst:
    # 처음엔 round 썼는데 틀렸다고 뜸. round 함수의 동작 방식이 이상하다고 함
    # 0.5, -0.5는 0으로 된다고 함
    print("%s %.4f" %(l[0], l[1]))