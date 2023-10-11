def solution(a, b):
    r1 = int(str(a)+str(b))
    r2 = int(str(b)+str(a))
    return max(r1,r2)