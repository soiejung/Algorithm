import sys

input = sys.stdin.readline

S_ = input().rstrip()
S = list(set(S_.upper()))
Alphabet = list(set(S))
count = [0 for _ in range(len(Alphabet))]
for s in S_:
    for i in range(len(Alphabet)):
        if s.upper() == Alphabet[i]:
            count[i] += 1

max_ = 0
idx = 0

for i in range(len(count)):
    if count[i] > max_:
        max_ = count[i]
        idx = i


max_count = count.count(max_)
if max_count != 1:
    print('?')
else:
    print(Alphabet[idx])
