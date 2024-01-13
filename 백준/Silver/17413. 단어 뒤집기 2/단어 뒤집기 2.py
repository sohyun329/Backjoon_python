import sys

word = sys.stdin.readline().rstrip()
stack = []
check = False
res = ''

for w in word :
    if w == ' ':
        while stack :
            res += stack.pop()
        res += w
    elif w == '<':
        while stack :
            res += stack.pop()
        check = True
        res += w
    elif w == '>':
        check = False
        res += w
    elif check :
        res += w
    else :
        stack.append(w)
    
while stack:
    res += stack.pop()

print(res)