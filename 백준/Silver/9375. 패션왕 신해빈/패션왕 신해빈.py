n = int(input())

for _ in range(n):
    m = int(input())
    fashion = {}
    for _ in range(m):
        name, kind = map(str, input().split())
        if kind in fashion:
            fashion[kind] += 1 
        else:
            fashion[kind] = 1
    result = 1
    
    for key in fashion:
        result *= (fashion[key] + 1)
    
    print(result - 1)
