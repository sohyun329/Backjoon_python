import sys

text = list(sys.stdin.readline().rstrip())
stack = []

for i in range(int(sys.stdin.readline())):
    cmd = list(sys.stdin.readline().split())
    
    if cmd[0] == 'L':
        if text:
            stack.append(text.pop())
    elif cmd[0] == 'D':
        if stack:
            text.append(stack.pop())
    elif cmd[0] == 'B':
        if text:
            text.pop()
    else:
        text.append(cmd[1])

print(''.join(text+list(reversed(stack))))            