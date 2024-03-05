n, k = map(int, input().split())
arr = list(map(int, input().split()))
tap = []
cnt = 0

for this in range(k):
    if arr[this] in tap :
        continue
    
    if len(tap) < n :
        tap.append(arr[this])
        continue
    
    priority = []
    for t in tap:
        if t in arr[this:]:
            priority.append(arr[this:].index(t))
        else:
            priority.append(101)
    target = priority.index(max(priority))
    tap.remove(tap[target])
    tap.append(arr[this])
    cnt += 1

print(cnt)