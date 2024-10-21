n = int(input())
sign = list(input().split())

ans = []
visited = [False]*10 # 숫자

def check_sign(i,j,sign):
    if sign <= '<':
        return i < j
    else:
        return i > j

def backtracking(index, result):
    
    if index == n+1 :
        ans.append(result)
        return
        
    for i in range(10):
        if not visited[i]:
            if index == 0 or check_sign(result[-1], str(i), sign[index-1]):
                visited[i] = True
                backtracking(index+1, result+str(i))
                visited[i] = False

backtracking(0,"")

ans.sort()
print(ans[-1])
print(ans[0])
