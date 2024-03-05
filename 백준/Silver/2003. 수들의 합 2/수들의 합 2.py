N, M = map(int, input().split())
num = list(map(int, input().split()))

start, end = 0, 1
cnt = 0

while end <= N and start <= end :
    sum_num = num[start:end]
    total = sum(sum_num)
    
    if total == M :
        cnt += 1
        end += 1
    elif total < M :
        end += 1
    else:
        start += 1
        
print(cnt)