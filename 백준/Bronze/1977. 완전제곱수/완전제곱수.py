m = int(input())
n = int(input())
res = []
for i in range(m, n+1):
    t = int(i**0.5) ** 2
    if i == t : res.append(i)
    
if res : 
    print(sum(res))
    print(min(res))
else : print(-1)