word = list(input())
stack = []
result = ''
for w in word :
    if w.isalpha():
        result += w
    else :
        if w == '(' : stack.append(w)
        elif w == '*' or w == '/' :
            while stack and (stack[-1] == '*' or stack[-1] == '/') :
                result += stack.pop()
            stack.append(w)
        elif w == '+' or w == '-' :
            while stack and stack[-1]!='(':
                result += stack.pop()
            stack.append(w)
        elif w == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
            
while stack:
    result += stack.pop()

print(result)
        