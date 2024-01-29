def solution(s):
    answer = ''
    # 너무 노가다 풀이 방식인것같음
    # return ''.join(sorted(s,reverse=True)) -> 한줄로 해결 가능
    # 문자열 정렬 가능, join 함수를 통해 list의 값을 문자열로 합칠 수 있음
    dic = {'A':0,'a':27,'B':1,'b':28,'C':2,'c':29,'D':3,'d':30,'E':4,'e':31,'F':5,'f':32,'G':6,'g':33,'H':7,'h':34,'I':8,'i':35,'J':9,'j':36,'K':10,'k':37,'L':11,'l':38,'M':12,'m':39,'N':13,'n':40,'O':14,'o':41,'P':15,'p':42,'Q':16,'q':43,'R':17,'r':44,'S':18,'s':45,'T':19,'t':46,'U':20,'u':47,'V':21,'v':48,'W':22,'w':49,'X':23,'x':50,'Y':24,'y':51,'Z':25,'z':52}

    lst = []
    for i in range(len(s)):
        lst.append((dic[s[i]],s[i]))
        
    lst.sort(key = lambda x: x[0], reverse=True)
    
    for l in lst:
        answer += l[1]
    return answer