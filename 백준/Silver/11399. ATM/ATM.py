n = int(input())
time = sorted([int(i) for i in input().split()])

result = [time[0]]
temp = time[0]

for i in range(1,n):
    temp += time[i]
    result.append(temp)
    
print(sum(result))