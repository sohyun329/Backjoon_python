# 첫째 줄에 네 정수 H, W, X, Y 주어짐
# 크기가 H x W인 배열 A
# 크기가 (H+X)x(W+Y)인 배열 B

h,w,x,y = map(int, input().split())

ans = []
graph = []

for _ in range(h+x):
    graph.append(list(map(int,input().split())))
    
for i in range(h):
    ans.append(graph[i][:w])
    
for i in range(h):
    for j in range(w):
        if i+x<h and j+y<w :
            ans[i+x][j+y] -= ans[i][j]
            
for a in ans:
    print(' '.join(map(str,a)))