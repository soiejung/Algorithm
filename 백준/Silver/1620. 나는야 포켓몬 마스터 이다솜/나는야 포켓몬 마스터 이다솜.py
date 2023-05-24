import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pocket_dic1 = {}
pocket_dic2 = {}
for i in range(1, N+1):
    name = input().rstrip()
    pocket_dic1[str(i)] = name
    pocket_dic2[name] = str(i)

for m in range(N+1, N+M+1):
    quiz = input().rstrip()
    if quiz in pocket_dic1.keys():
        print(pocket_dic1[quiz])
    elif quiz in pocket_dic2.keys():
        print(int(pocket_dic2[quiz]))
    else:
        break
