n = int(input())
arr = list(map(int,input().split()))
answer = [0]*n
stack = []

for i in range(len(arr)):
    while stack:
        if arr[stack[-1][0]] < arr[i]:
            stack.pop()
        else:
            answer[i] = stack[-1][0]+1
            break
    stack.append((i,arr[i]))

print(*answer)