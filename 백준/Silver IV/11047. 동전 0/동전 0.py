n, k = map(int, input().split())
money = []
answer = 0

for _ in range(n):
    a = int(input())
    money.append(a)

money.sort(reverse=True) # 내림차순으로 정렬

for m in money:
    if k >= m :
        answer += k // m
        k %= m
        if k <= 0 : break
        
print(answer)