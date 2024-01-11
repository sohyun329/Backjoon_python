n, k = map(int, input().split())
arr = [i+1 for i in range(n)]
result = []
num = 0

for i in range(n):
    num += k-1
    if num >= len(arr):
        num = num%len(arr)
        
    result.append(str(arr.pop(num)))
print('<',", ".join(result)[:],'>',sep='')