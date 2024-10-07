import sys

n = int(input())
info = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
ans = [[0 for _ in range(n)] for _ in range(n)]

for k in range(5):
    for i in range(n):
        for j in range(i+1, n):
            if info[i][k] == info[j][k]:
                ans[i][j] = 1
                ans[j][i] = 1
                

cnt = []
for a in ans:
    cnt.append(a.count(1))
    
print(cnt.index(max(cnt))+1)