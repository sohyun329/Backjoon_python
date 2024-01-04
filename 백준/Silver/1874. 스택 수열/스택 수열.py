n = int(input())
stack = []
start = 1
operator = []

for i in range(n):
    num = int(input())
    while start <= num :
        stack.append(start)
        operator.append('+')
        start+=1
    
    if stack[-1] == num:
        stack.pop()
        operator.append('-')
    
    else:
        print('NO')
        break

else :
    for i in operator:
        print(i)
    