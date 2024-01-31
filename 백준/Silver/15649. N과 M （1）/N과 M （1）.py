n, m = map(int, input().split())
array = []

# 백트래킹 구현
def backtracking():
    if len(array) == m :
        print(' '.join(map(str,array)))
        return
    
    for i in range(1,n+1):
        if i not in array:
            array.append(i)
            backtracking()
            array.pop()

backtracking()