n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
answer = 0

for a in A:
    max_b = max(B)
    answer += a*max_b
    B.pop(B.index(max_b))

print(answer)