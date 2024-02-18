n, m = map(int, input().split())
num = [int(input()) for i in range(n)]

start, end = 0, 1
num.sort()

min_diff = float('inf') 

while start <= end and end < n:
    diff = abs(num[start] - num[end])
    
    if diff >= m:
        min_diff = min(min_diff, diff)
        start += 1  # 최소 차이를 찾기 위해 start 포인터 증가
    else:
        end += 1  # 차이가 m 미만이면 end 포인터 증가하여 차이 늘림

print(min_diff)