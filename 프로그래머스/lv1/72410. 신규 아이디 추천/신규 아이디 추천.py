from collections import deque
def solution(new_id):
    answer = ''
    
    # 1단계: 모든 대문자느 대응되는 소문자로 치환
    new_id = new_id.lower()
    q1 = deque()
    q2 = deque()
    
    # 2단계: 알파벳 소문자, 숫자, -, _, . 를 제외한 모든 문자 제거
    for i in range(len(new_id)):
        if new_id[i].isalpha() or new_id[i].isdigit() or new_id[i] == '_' or new_id[i] == '-' or new_id[i] == '.':
            q1.append(new_id[i])
    
    # 제거할 문자가 없을 때 q1에 그대로 new_id를 받아옴
    if not q1:
        for n in new_id:
            q1.append(n)
            
    # 3단계: . 가 2번 이상 연속된 부분을 하나의 . 로 치환
    for q in q1:
        if not q2:
            q2.append(q)
        else:
            if q2[-1] == '.' and q == '.':
                continue
            else:
                q2.append(q)
            
    # 4단계: .가 처음이나 끝에 위치한다면 제거
    if q2 and q2[0] == '.':
        q2.popleft()
    if q2 and q2[-1] == '.':
        q2.pop()
        
    # 5단계: new_id가 빈 문자열이라면, new_id에 "a" 대입
    if not q2:
        q2.append("a")

            
    # 6단계: new_id의 길이가 16자 이상이면 첫 15개의 문자를 제외한 나머지 문자열 제거
    # 만약 제거 후 마침표가 끝에 위치한다면 마침표 제거
    q3 = deque()
    if len(q2) >= 16:
        for i in range(15):
            q = q2.popleft()
            q3.append(q)

        if q3[-1] == '.':
            q3.pop()
    else:
        for q in q2:
            q3.append(q)
            
    
    # 7단계: new_id의 길이가 2자 이하라면, new_id 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙인다.
    
    if len(q3) <= 2:
        last = q3[-1]
        while True:
            if len(q3) == 3:
                break
            q3.append(last)
    
    for q in q3:
        answer += q
        
    return answer