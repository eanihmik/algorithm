# https://programmers.co.kr/learn/courses/30/lessons/92334
# 66.7 / 100(타임아웃)

import numpy as np
def solution(id_list, report, k):
    report = np.unique(report)
    
    reporter = []
    reported = []
    for r in report:
        reporter.append(r.split()[0])
        reported.append(r.split()[1])
        
    d = {}
    for i in np.unique(reported):
        d[i] = reported.count(i)
        
    blocked = np.array(list(d.keys()))[np.array(list(d.values())) >= k]
    
    answer = []
    for id in id_list:
        count = 0
        for n in range(len(reporter)):
            if reported[n] in blocked and reporter[n] == id:
                count += 1
        answer.append(count)
    return answer
