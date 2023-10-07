from itertools import permutations
def solution(babbling):
    answer = 0
    lst = ["aya", "ye", "woo", "ma"]

    for b in babbling:
        for l in lst:
            if l*2 not in b:
                b = b.replace(l,' ')
        if b.strip() == '':
            answer += 1
    return answer