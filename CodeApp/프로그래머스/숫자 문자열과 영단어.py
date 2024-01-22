# https://school.programmers.co.kr/learn/courses/30/lessons/81301
import re
def solution(s):
    answer = 0
    eng = {"zero":'0', "one":'1', "two":'2', "three":'3', "four":'4', "five":'5', "six":'6', "seven":'7', "eight":'8', "nine":'9'}
    
    for key in eng.keys():
        if key in s:
            s = s.replace(key,eng[key])
    
    answer = int(s)
    return answer