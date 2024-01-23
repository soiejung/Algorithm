# https://school.programmers.co.kr/learn/courses/30/lessons/12915
def solution(strings, n):
    answer = []
    
    # 정렬하고자 하는 위치의 알파벳을 맨 앞에 붙여줌
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]
    
    # 정렬
    strings.sort()
    
    # 정렬 후 맨 앞에 추가로 붙여준 알파벳 제거
    for s in strings:
        answer.append(s[1:])
    
    return answer