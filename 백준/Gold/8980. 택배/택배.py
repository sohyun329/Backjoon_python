n, c = map(int, input().split())
m = int(input())
boxes = []

for _ in range(m):
    boxes.append(list(map(int, input().split())))

boxes = sorted(boxes, key=lambda x:x[0])
ans = 0
vilage = [0]*(n+1)

for f,t,s in boxes:
    temp = s
    for i in range(f,t):
        if vilage[i]+temp >= c : 
            temp = c - vilage[i]
    for i in range(f,t):
        vilage[i] += temp
    ans += temp

print(ans)