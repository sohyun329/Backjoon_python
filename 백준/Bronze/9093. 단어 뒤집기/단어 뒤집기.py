num = int(input())

for n in range(num):
    s = list(input().split())
    for j in s:
        print(j[::-1])