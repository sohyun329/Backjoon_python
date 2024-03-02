n = int(input())
point = []
result = 0

for _ in range(n):
    point.append(int(input()))

for i in range(n-1,0,-1):
    if point[i] <= point[i-1]:
        result += point[i-1]-point[i]+1
        point[i-1] = point[i]-1

print(result)        