import sys

n = int(input())
info = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
ans = [0]*n

for i in range(n):
    for j in range(i+1, n):
        for g in range(5):
            if info[i][g] == info[j][g]:
                ans[i]+=1
                ans[j]+=1 
                break              

    
print(ans.index(max(ans))+1)