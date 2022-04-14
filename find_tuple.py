# https://programmers.co.kr/learn/courses/30/lessons/64065
# 100 / 100

def solution(s):
    s = s[2:-2].split("},{")
    new_s = [a.split(',') for a in s]
    answer = []
    while new_s != []:
        m = min(new_s, key=len)
        for i in range(len(m)):
            if m[i] not in answer:
                answer.append(m[i])
        new_s.remove(m)
    answer = [int(a) for a in answer]
    return answer
