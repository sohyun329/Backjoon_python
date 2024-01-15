import math

def solution(progresses, speeds):
    answer = []
    stack = []
    
    for i in range(0,len(progresses)):
        a = math.ceil((100-progresses[i])/speeds[i])
        stack.append(a)
        
    while stack:
        current = stack.pop(0)
        cnt = 1
        while stack and stack[0] <= current:
            cnt += 1
            stack.pop(0)
        answer.append(cnt)
        
    return answer