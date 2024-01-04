n = int(input())

for i in range(0,n):
    s = list(map(str, input().split()))
    result = float(s[0])
    for i in range(1,len(s)):
        if s[i] == '@' : result *= 3
        elif s[i] == '%' : result += 5
        elif s[i] == '#' : result -= 7
    print('{:.2f}'.format(result))