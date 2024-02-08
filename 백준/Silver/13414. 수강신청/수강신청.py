import sys

n, k = map(int, sys.stdin.readline().split())

dict = {}
for i in range(k):
    dict[sys.stdin.readline().rstrip()] = i
    
result = sorted(dict.items(), key=lambda x:x[1])

if (n>len(result)):
    n = len(result)

for i in range(n):
    print(result[i][0])