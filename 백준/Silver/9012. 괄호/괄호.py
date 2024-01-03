n = int(input())

for i in range(n):
    stack = []
    bracket = input()
    ISVPS = True
    
    for s in bracket:
        if s == '(':
            stack.append('(')
        if s == ')':
            if stack :
                stack.pop()
            else :
                print('NO')
                break
    else :
        if len(stack)==0:
            print('YES')
        else:
            print('NO')