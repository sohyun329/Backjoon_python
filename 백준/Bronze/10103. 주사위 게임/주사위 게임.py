c = s = 100
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    if a > b : s -= a
    elif a < b : c -= b 
    elif a == b : s == s, c == c 
    
print(c,s,sep='\n')