t = int(input())

for i in range(0,t):
    r, s = input().split()
    for i in s:
        print(i*int(r),end="")
    print()