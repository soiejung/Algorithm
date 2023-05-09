T = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num , stu = map(int, input().split())
    score = []
    sort_score = []
    for n in range(num):
        mid, final, hw = map(int, input().split())
        score.append(mid * 0.35 + final * 0.45 + hw * 0.2)
        sort_score.append(mid * 0.35 + final * 0.45 + hw * 0.2)

    sort_score.sort(reverse=True)
    idx = sort_score.index(score[stu-1])
    rate = (idx+1) / num
    
    if rate <= 0.1:
        g = 0
    elif rate > 0.1 and rate <= 0.2:
        g = 1
    elif rate > 0.2 and rate <= 0.3:
        g = 2
    elif rate > 0.3 and rate <= 0.4:
        g = 3
    elif rate > 0.4 and rate <= 0.5:
        g = 4
    elif rate > 0.5 and rate <= 0.6:
        g = 5
    elif rate > 0.6 and rate <= 0.7:
        g = 6
    elif rate > 0.7 and rate <= 0.8:
        g = 7
    elif rate > 0.8 and rate <= 0.9:
        g = 8
    else:
        g = 9
        
    print(f'#{test_case} {grade[g]}')
    
    
    
    
