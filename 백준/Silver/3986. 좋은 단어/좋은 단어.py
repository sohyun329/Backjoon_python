n = int(input())
ans = n

for i in range(n):
    text = input()
    stack = []
    for t in text :
        if stack and stack[-1] == t : stack.pop()
        else : stack.append(t)
    
    if stack : ans -= 1

print(ans)