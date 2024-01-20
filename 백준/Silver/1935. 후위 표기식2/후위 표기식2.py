n = int(input())
word = list(input())
num = [int(input()) for i in range(n)]

stack = []

for w in word :
    if w.isalpha():
        stack.append(num[ord(w)-65])
    else:
        a = stack.pop()
        result = stack.pop()
        
        if w == '+':
            result += a
        elif w == '-':
            result -= a
        elif w == '*':
            result *= a
        elif w == '/':
            result /= a
        
        stack.append(result)
        
print('%.2f'%stack[-1])