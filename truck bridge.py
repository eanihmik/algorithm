# https://programmers.co.kr/learn/courses/30/lessons/42583
# 71.4 / 100(타임아웃)

import numpy as np
def solution(bridge_length, weight, truck_weights):
    answer = 0
    passing = np.zeros(bridge_length)
    waiting = truck_weights
    while (sum(passing) != 0 or waiting != []):
        for n in range(len(passing) - 1):
            passing[n] = passing[n+1]
        passing[-1] = 0
        if waiting != []:
            if sum(passing) + waiting[0] <= weight:
                passing[-1] = waiting[0]
                waiting.pop(0)
        answer += 1
    return answer
