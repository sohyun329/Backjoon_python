n = int(input())
rope = []

for _ in range(n):
    a = int(input())
    rope.append(a)

rope.sort()

ans = []
    
for r in rope:
    ans.append(r*n)
    n-=1

print(max(ans))