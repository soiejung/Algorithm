import sys
#sys.stdin = open("복습/input.txt","r")
input = sys.stdin.readline

def recur(idx, p, f, s, v, c):

    global answer 
    global answers
    if idx == N:
        if p >= mp and f >= mf and s >= ms and v >= mv:
            answer = min(answer, c)
            # 그냥 arr로 넣으면 결과에 그냥 빈 문자열로 들어감
            # 아마 pop해서 그런듯?
            answers.append([answer,[a for a in arr]])

        return
    
    arr.append(idx+1)
    recur(idx+1, p+lst[idx][0], f+lst[idx][1], s+lst[idx][2], v+lst[idx][3], c+lst[idx][4])
    arr.pop()

    recur(idx+1, p, f, s, v, c)



N = int(input())
mp, mf, ms, mv = map(int, input().split())

lst = [list(map(int, input().split()))for _ in range(N)]

arr =[]
answers = []
answer = 99999999
recur(0,0,0,0,0,0)

if answers:
    answers.sort(key=lambda x:(x[0], x[1]))
    print(answers[0][0])
    print(*answers[0][1])

else:
    print(-1)