from collections import deque

n, d, k, c = map(int, input().split())
dish = [int(input()) for _ in range(n)]
cnt = 0
queue = deque(dish[:k])

for i in range(n):
    if i != 0 :
        if i <= n/2 :
            queue.append(dish[i+k-1])
        else:
            queue.append(dish[k-(n-i)-1])
    
    kinds = set(queue)
    kinds.add(c)
    cnt = max(cnt, len(kinds))
    queue.popleft()
    
print(cnt)