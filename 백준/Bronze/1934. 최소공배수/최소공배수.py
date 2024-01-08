import sys

def gcd(n1,n2):
    while True:
        n2 = n2%n1
        n1, n2 = n2, n1
        if n1 == 0:
            return n2

n = int(input())

for i in range(n):
    a,b = map(int, sys.stdin.readline().strip().split())
    print(a*b // gcd(a,b))
    