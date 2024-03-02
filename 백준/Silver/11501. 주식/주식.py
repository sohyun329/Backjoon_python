t = int(input())
result = []

for _ in range(t):
    n = int(input())
    stack = list(map(int, input().split()))
    
    money = 0 # 이익
    max_Price = 0 # 최대 이익
    
    for i in range(len(stack)-1,-1,-1):
        if stack[i] > max_Price:
            max_Price = stack[i]
        else:
            money += max_Price - stack[i]
    
    result.append(money)

print(*result, sep='\n')